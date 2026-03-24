#!/usr/bin/env python3
"""TxGNN 深度學習預測 - 獨立腳本

此腳本不依賴本地 txgnn 套件，直接使用已安裝的 TxGNN。

使用方法:
    conda activate txgnn
    cd /Users/lightman/yao.care/EuTxGNN
    python scripts/run_txgnn_standalone.py
"""

import csv
import json
from pathlib import Path
from typing import Set

import pandas as pd
import torch
from tqdm import tqdm


def detect_device() -> str:
    """偵測最佳運算裝置"""
    if torch.cuda.is_available():
        print(f"✓ 使用 CUDA: {torch.cuda.get_device_name(0)}")
        return "cuda:0"
    else:
        print("✓ 使用 CPU 模式")
        return "cpu"


class CheckpointManager:
    """Checkpoint 管理器"""

    COLUMNS = ["drugbank_id", "drug_name", "disease_name", "txgnn_score"]

    def __init__(self, checkpoint_path: Path):
        self.checkpoint_path = Path(checkpoint_path)
        self.processed_drugs: Set[str] = set()
        self._file_exists = self.checkpoint_path.exists()

    def load(self) -> Set[str]:
        if not self._file_exists:
            return set()
        try:
            df = pd.read_csv(self.checkpoint_path)
            self.processed_drugs = set(df["drugbank_id"].unique())
            print(f"✓ 從 checkpoint 載入 {len(self.processed_drugs)} 個已處理藥物")
            return self.processed_drugs
        except Exception as e:
            print(f"⚠ 無法載入 checkpoint: {e}")
            return set()

    def append(self, predictions: list):
        if not predictions:
            return
        self.checkpoint_path.parent.mkdir(parents=True, exist_ok=True)
        write_header = not self._file_exists
        with open(self.checkpoint_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self.COLUMNS)
            if write_header:
                writer.writeheader()
                self._file_exists = True
            writer.writerows(predictions)
        for pred in predictions:
            self.processed_drugs.add(pred["drugbank_id"])

    def get_results(self) -> pd.DataFrame:
        if not self._file_exists:
            return pd.DataFrame(columns=self.COLUMNS)
        return pd.read_csv(self.checkpoint_path)

    def is_processed(self, drugbank_id: str) -> bool:
        return drugbank_id in self.processed_drugs


def main():
    print("=" * 60)
    print("TxGNN 深度學習預測 - 歐盟版")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    device = detect_device()

    # 參數
    MIN_SCORE = 0.5
    TOP_K = 50

    # 1. 載入藥品映射
    print("\n1. 載入藥品映射...")
    drug_mapping_path = base_dir / "data" / "processed" / "drug_mapping.csv"
    drug_mapping = pd.read_csv(drug_mapping_path)
    valid_drugs = drug_mapping[drug_mapping["drugbank_id"].notna()]
    print(f"   有 DrugBank ID: {len(valid_drugs)}")
    print(f"   不重複 DrugBank ID: {valid_drugs['drugbank_id'].nunique()}")

    # 2. 初始化 checkpoint
    checkpoint_path = base_dir / "data" / "processed" / "txgnn_checkpoint.csv"
    checkpoint_manager = CheckpointManager(checkpoint_path)
    checkpoint_manager.load()

    # 3. 載入 TxGNN
    print("\n2. 載入 TxGNN...")
    from txgnn import TxData, TxGNN
    from txgnn.utils import convert2str

    data_dir = base_dir / "data"
    model_dir = base_dir / "model_ckpt"

    print("   載入資料集...")
    tx_data = TxData(data_folder_path=str(data_dir))
    tx_data.prepare_split(split="complex_disease", seed=42)
    print(f"   節點數: {tx_data.G.number_of_nodes()}")
    print(f"   邊數: {tx_data.G.number_of_edges()}")

    print("   載入預訓練模型...")
    model = TxGNN(
        data=tx_data,
        weight_bias_track=False,
        proj_name="EuTxGNN",
        exp_name="eu_drug_repurposing",
        device=device,
    )
    model.load_pretrained(str(model_dir))

    # 4. 建立映射
    print("\n3. 建立索引映射...")
    df = tx_data.df.copy()
    df["x_id"] = df.x_id.apply(lambda x: convert2str(x))
    df["y_id"] = df.y_id.apply(lambda x: convert2str(x))

    # 藥物映射
    drug_rows = df[df.x_type == "drug"][["x_id", "x_idx"]].drop_duplicates()
    drugbank_to_idx = dict(zip(drug_rows["x_id"], drug_rows["x_idx"].astype(int)))
    drug_rows_y = df[df.y_type == "drug"][["y_id", "y_idx"]].drop_duplicates()
    drugbank_to_idx.update(dict(zip(drug_rows_y["y_id"], drug_rows_y["y_idx"].astype(int))))

    # 藥物名稱
    nodes_df = pd.read_csv(data_dir / "node.csv", sep="\t")
    drug_nodes = nodes_df[nodes_df["node_type"] == "drug"].copy()
    drug_nodes["node_id"] = drug_nodes["node_id"].str.strip('"')
    drugbank_to_name = dict(zip(drug_nodes["node_id"], drug_nodes["node_name"]))

    # 疾病映射
    disease_rows = df[df.y_type == "disease"][["y_id", "y_idx"]].drop_duplicates()
    all_disease_indices = sorted(disease_rows["y_idx"].astype(int).unique().tolist())

    kg_df = pd.read_csv(data_dir / "kg.csv")
    kg_df["y_id"] = kg_df.y_id.apply(lambda x: convert2str(x))
    disease_names = kg_df[kg_df.y_type == "disease"][["y_id", "y_name"]].drop_duplicates()
    disease_id_to_name = dict(zip(disease_names["y_id"], disease_names["y_name"]))
    disease_idx_to_id = dict(zip(disease_rows["y_idx"].astype(int), disease_rows["y_id"]))
    disease_idx_to_name = {
        idx: disease_id_to_name.get(disease_idx_to_id.get(idx, ""), f"disease_{idx}")
        for idx in all_disease_indices
    }

    print(f"   藥物數: {len(drugbank_to_idx)}")
    print(f"   疾病數: {len(all_disease_indices)}")

    # 5. 執行預測
    print("\n4. 執行預測...")
    unique_ids = valid_drugs["drugbank_id"].unique()

    drugs_to_predict = []
    for db_id in unique_ids:
        if db_id in drugbank_to_name:
            if not checkpoint_manager.is_processed(db_id):
                drugs_to_predict.append({
                    "drugbank_id": db_id,
                    "drug_name": drugbank_to_name[db_id],
                })

    print(f"   待處理藥物: {len(drugs_to_predict)}")

    for drug_info in tqdm(drugs_to_predict, desc="預測中"):
        drug_predictions = []
        try:
            db_id = drug_info["drugbank_id"]
            if db_id not in drugbank_to_idx:
                continue

            drug_idx = drugbank_to_idx[db_id]

            # 建立預測 DataFrame
            df_predict = pd.DataFrame({
                "x_idx": [drug_idx] * len(all_disease_indices),
                "relation": ["indication"] * len(all_disease_indices),
                "y_idx": all_disease_indices,
            })

            # 預測
            with torch.no_grad():
                pred_scores = model.predict(df_predict)

            etype = ("drug", "indication", "disease")
            if etype not in pred_scores:
                continue

            scores = torch.sigmoid(pred_scores[etype]).cpu().numpy()

            # 排序取 top-k
            scored_diseases = [
                (disease_idx_to_name.get(all_disease_indices[i], f"disease_{i}"), float(scores[i]))
                for i in range(len(all_disease_indices))
            ]
            scored_diseases.sort(key=lambda x: x[1], reverse=True)

            for disease_name, score in scored_diseases[:TOP_K]:
                if score >= MIN_SCORE:
                    drug_predictions.append({
                        "drugbank_id": db_id,
                        "drug_name": drug_info["drug_name"],
                        "disease_name": disease_name,
                        "txgnn_score": score,
                    })

            checkpoint_manager.append(drug_predictions)

        except Exception as e:
            print(f"\n錯誤 {drug_info['drug_name']}: {e}")
            continue

    # 6. 儲存結果
    print("\n5. 儲存結果...")
    result_df = checkpoint_manager.get_results()

    if len(result_df) > 0:
        result_df = result_df.sort_values("txgnn_score", ascending=False)
        result_df["rank"] = range(1, len(result_df) + 1)
        result_df["source"] = "TxGNN Deep Learning Model"

        output_path = base_dir / "data" / "processed" / "txgnn_dl_predictions.csv.gz"
        result_df.to_csv(output_path, index=False)
        print(f"   已儲存: {output_path}")

        print("\n" + "=" * 60)
        print("TxGNN 深度學習預測統計")
        print("=" * 60)
        print(f"總預測數: {len(result_df)}")
        print(f"涉及藥物: {result_df['drugbank_id'].nunique()}")
        print(f"涉及疾病: {result_df['disease_name'].nunique()}")
        print(f"平均信心分數: {result_df['txgnn_score'].mean():.4f}")
        print(f"最高信心分數: {result_df['txgnn_score'].max():.4f}")

        print("\n前 10 個高信心預測:")
        for _, row in result_df.head(10).iterrows():
            print(f"  {row['drug_name']} -> {row['disease_name']}: {row['txgnn_score']:.4f}")

        # 儲存報告
        report = {
            "total_predictions": len(result_df),
            "unique_drugs": int(result_df["drugbank_id"].nunique()),
            "unique_diseases": int(result_df["disease_name"].nunique()),
            "avg_score": float(result_df["txgnn_score"].mean()),
            "max_score": float(result_df["txgnn_score"].max()),
        }
        report_path = base_dir / "data" / "processed" / "txgnn_dl_report.json"
        with open(report_path, "w") as f:
            json.dump(report, f, indent=2)

    print("\n完成！")


if __name__ == "__main__":
    main()
