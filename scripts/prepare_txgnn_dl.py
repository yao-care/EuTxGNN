#!/usr/bin/env python3
"""準備 TxGNN 深度學習預測所需的資料

將 EU 藥品映射轉換為 TxGNN DL 可用的格式。

使用方法:
    uv run python scripts/prepare_txgnn_dl.py

產生檔案:
    data/processed/drug_mapping.csv - TxGNN DL 所需的藥品映射
"""

import json
from pathlib import Path

import pandas as pd

from eutxgnn.data.loader import load_integrated_data


def main():
    print("=" * 60)
    print("準備 TxGNN 深度學習預測資料")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent

    # 1. 載入整合資料
    print("1. 載入整合資料...")
    integrated_data = load_integrated_data()
    mapped_ingredients = integrated_data["mapped_ingredients"]
    ema_drugs = integrated_data["ema_drugs"]
    metadata = integrated_data["metadata"]

    print(f"   已映射成分: {len(mapped_ingredients)}")
    print(f"   EMA 核心藥品: {len(ema_drugs)}")

    # 2. 建立藥品映射表
    print("\n2. 建立藥品映射表...")

    # 建立成分 -> DrugBank ID 對照
    ingredient_to_drugbank = {
        item["ingredient"]: item["drugbank_id"]
        for item in mapped_ingredients
    }

    # 展開 EMA 藥品的成分
    rows = []
    for drug in ema_drugs:
        license_id = drug.get("license_id", "")
        brand_name = drug.get("brand_name", "")
        active_substance = drug.get("active_substance", "")
        indication = drug.get("therapeutic_indication", "")

        if not active_substance:
            continue

        for ingredient in str(active_substance).split(";"):
            ingredient = ingredient.strip()
            if not ingredient:
                continue

            drugbank_id = ingredient_to_drugbank.get(ingredient)

            rows.append({
                "license_id": license_id,
                "brand_name": brand_name,
                "original_ingredient": ingredient,
                "normalized_ingredient": ingredient,
                "synonyms": "",
                "drugbank_id": drugbank_id,
                "mapping_success": drugbank_id is not None,
                "mapping_source": "drugbank" if drugbank_id else "failed",
            })

    drug_mapping_df = pd.DataFrame(rows)

    # 統計
    total = len(drug_mapping_df)
    mapped = drug_mapping_df["drugbank_id"].notna().sum()
    print(f"   總筆數: {total}")
    print(f"   有 DrugBank ID: {mapped} ({100*mapped/total:.1f}%)")
    print(f"   不重複 DrugBank ID: {drug_mapping_df['drugbank_id'].dropna().nunique()}")

    # 3. 儲存
    print("\n3. 儲存藥品映射表...")
    output_dir = base_dir / "data" / "processed"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / "drug_mapping.csv"
    drug_mapping_df.to_csv(output_path, index=False)
    print(f"   已儲存: {output_path}")

    # 4. 檢查 TxGNN 相容性
    print("\n4. 檢查 TxGNN 相容性...")

    # 載入 TxGNN node.csv 檢查藥物覆蓋率
    node_path = base_dir / "data" / "node.csv"
    if node_path.exists():
        nodes_df = pd.read_csv(node_path, sep="\t")
        drug_nodes = nodes_df[nodes_df["node_type"] == "drug"]
        drug_nodes["node_id"] = drug_nodes["node_id"].str.strip('"')
        txgnn_drugs = set(drug_nodes["node_id"])

        # 計算覆蓋率
        our_drugs = set(drug_mapping_df["drugbank_id"].dropna())
        overlap = our_drugs & txgnn_drugs

        print(f"   TxGNN 藥物數: {len(txgnn_drugs)}")
        print(f"   EU 映射藥物數: {len(our_drugs)}")
        print(f"   重疊藥物數: {len(overlap)} ({100*len(overlap)/len(our_drugs):.1f}%)")
    else:
        print("   [跳過] node.csv 不存在")

    print("\n" + "=" * 60)
    print("準備完成！")
    print("=" * 60)

    print("\n下一步: 設定 conda 環境執行 TxGNN 深度學習預測")
    print("""
# 建立 conda 環境
conda create -n txgnn python=3.11 -y
conda activate txgnn

# 安裝 PyTorch (CPU 版本，適用於 macOS)
pip install torch==2.2.2 torchvision==0.17.2

# 安裝 DGL
pip install dgl==1.1.3

# 安裝 TxGNN
pip install git+https://github.com/mims-harvard/TxGNN.git

# 安裝其他依賴
pip install pandas tqdm pyyaml pydantic ogb gdown

# 下載預訓練模型
python -c "from eutxgnn.predict.txgnn_model import download_pretrained_model; download_pretrained_model()"

# 執行深度學習預測
python scripts/run_txgnn_dl_prediction.py
""")


if __name__ == "__main__":
    main()
