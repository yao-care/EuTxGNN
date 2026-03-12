#!/usr/bin/env python3
"""執行 TxGNN 深度學習預測 - 歐盟版

使用 TxGNN 預訓練模型進行藥物-疾病預測。

使用方法（需在 txgnn conda 環境中執行）:
    conda activate txgnn
    python scripts/run_txgnn_dl_prediction.py

前置條件:
    1. 已設定 txgnn conda 環境（含 PyTorch, DGL, TxGNN）
    2. 已執行 prepare_txgnn_dl.py 產生 drug_mapping.csv
    3. 已下載 TxGNN 預訓練模型

支援中斷續算:
    - 自動儲存進度到 checkpoint
    - 中斷後重新執行會從上次停止處繼續
    - 使用 --restart 可清除進度重新開始

產生檔案:
    data/processed/txgnn_dl_predictions.csv
"""

import argparse
import json
from pathlib import Path

import pandas as pd


def main():
    parser = argparse.ArgumentParser(description="TxGNN 深度學習預測 - 歐盟版")
    parser.add_argument(
        "--min-score",
        type=float,
        default=0.5,
        help="最低信心分數門檻 (預設: 0.5)",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=50,
        help="每個藥物保留前 k 個疾病 (預設: 50)",
    )
    parser.add_argument(
        "--restart",
        action="store_true",
        help="忽略之前的進度，重新開始",
    )
    parser.add_argument(
        "--device",
        type=str,
        choices=["cuda:0", "cpu"],
        help="運算裝置 (預設: 自動偵測)",
    )
    args = parser.parse_args()

    print("=" * 60)
    print("TxGNN 深度學習預測 - 歐盟版")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent

    # 1. 檢查依賴
    print("1. 檢查依賴套件...")
    try:
        from eutxgnn.predict.txgnn_model import (
            check_dependencies,
            detect_device,
            print_install_instructions,
            TxGNNPredictor,
            CheckpointManager,
        )
    except ImportError as e:
        print(f"   [錯誤] 無法載入 txgnn_model: {e}")
        print("   請確認已正確安裝所有依賴")
        return

    deps_ok, missing = check_dependencies()
    if not deps_ok:
        print(f"   [錯誤] 缺少套件: {', '.join(missing)}")
        device = detect_device()
        print_install_instructions(missing, device)
        return

    device = args.device or detect_device()
    print(f"   ✓ 所有依賴已安裝")
    print(f"   使用裝置: {device}")

    # 2. 載入藥品映射
    print("\n2. 載入藥品映射...")
    drug_mapping_path = base_dir / "data" / "processed" / "drug_mapping.csv"
    if not drug_mapping_path.exists():
        print(f"   [錯誤] 找不到 {drug_mapping_path}")
        print("   請先執行: uv run python scripts/prepare_txgnn_dl.py")
        return

    drug_mapping = pd.read_csv(drug_mapping_path)
    valid_drugs = drug_mapping[drug_mapping["drugbank_id"].notna()]
    print(f"   總筆數: {len(drug_mapping)}")
    print(f"   有 DrugBank ID: {len(valid_drugs)}")
    print(f"   不重複 DrugBank ID: {valid_drugs['drugbank_id'].nunique()}")

    # 3. 初始化 checkpoint 管理器
    checkpoint_path = base_dir / "data" / "processed" / "txgnn_checkpoint.csv"
    checkpoint_manager = CheckpointManager(checkpoint_path)

    if args.restart:
        checkpoint_manager.clear()
        print("\n   已清除之前的進度")
    else:
        processed = checkpoint_manager.load()
        if processed:
            print(f"\n   從 checkpoint 載入 {len(processed)} 個已處理藥物")

    # 4. 初始化預測器
    print("\n3. 初始化 TxGNN 預測器...")
    try:
        predictor = TxGNNPredictor(
            data_dir=base_dir / "data",
            model_dir=base_dir / "model_ckpt",
            device=device,
        )
        predictor.setup()
    except FileNotFoundError as e:
        print(f"   [錯誤] {e}")
        print("\n   請確認已下載以下檔案:")
        print("   - data/kg.csv")
        print("   - data/node.csv")
        print("   - data/edges.csv")
        print("   - model_ckpt/model.pt")
        return
    except Exception as e:
        print(f"   [錯誤] 初始化失敗: {e}")
        import traceback
        traceback.print_exc()
        return

    # 5. 執行預測
    print("\n4. 執行預測...")
    print(f"   最低信心分數: {args.min_score}")
    print(f"   每藥物保留前 {args.top_k} 個疾病")

    predictions = predictor.predict_batch(
        drug_mapping,
        drugbank_col="drugbank_id",
        min_score=args.min_score,
        top_k_per_drug=args.top_k,
        checkpoint_manager=checkpoint_manager,
    )

    # 6. 儲存結果
    print("\n5. 儲存結果...")
    output_dir = base_dir / "data" / "processed"
    output_path = output_dir / "txgnn_dl_predictions.csv"

    if len(predictions) > 0:
        # 重新命名欄位
        result = predictions.rename(columns={
            "disease_name": "potential_indication",
        })
        result["source"] = "TxGNN Deep Learning Model"

        result.to_csv(output_path, index=False)
        print(f"   已儲存: {output_path}")

        # 統計
        print("\n" + "=" * 60)
        print("TxGNN 深度學習預測統計")
        print("=" * 60)
        print(f"總預測數: {len(result)}")
        print(f"涉及藥物: {result['drugbank_id'].nunique()}")
        print(f"涉及疾病: {result['potential_indication'].nunique()}")
        print(f"平均信心分數: {result['txgnn_score'].mean():.4f}")
        print(f"最高信心分數: {result['txgnn_score'].max():.4f}")

        # 前 10 個預測
        print("\n前 10 個高信心預測:")
        top10 = result.nlargest(10, "txgnn_score")
        for _, row in top10.iterrows():
            print(f"  {row['drug_name']} -> {row['potential_indication']}: {row['txgnn_score']:.4f}")

        # 儲存報告
        report = {
            "total_predictions": len(result),
            "unique_drugs": int(result["drugbank_id"].nunique()),
            "unique_diseases": int(result["potential_indication"].nunique()),
            "avg_score": float(result["txgnn_score"].mean()),
            "max_score": float(result["txgnn_score"].max()),
            "min_score_threshold": args.min_score,
            "top_k_per_drug": args.top_k,
        }

        report_path = output_dir / "txgnn_dl_report.json"
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        print(f"\n報告已儲存: {report_path}")
    else:
        print("   [警告] 沒有預測結果")

    print("\n" + "=" * 60)
    print("完成！")
    print("=" * 60)


if __name__ == "__main__":
    main()
