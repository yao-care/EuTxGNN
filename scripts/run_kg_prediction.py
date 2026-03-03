#!/usr/bin/env python3
"""執行知識圖譜方法預測 - 歐盟版

使用 TxGNN 知識圖譜進行老藥新用預測。

使用方法:
    uv run python scripts/run_kg_prediction.py

前置條件:
    1. 已執行 process_fda_data.py
    2. 已執行 prepare_external_data.py

產生檔案:
    data/processed/repurposing_candidates.csv
    data/processed/indication_mapping.csv
"""

import json
from pathlib import Path

import pandas as pd

from txgnn.data.loader import load_integrated_data, load_fda_drugs
from txgnn.mapping.disease_mapper import (
    load_disease_vocab,
    build_disease_index,
    map_fda_indications_to_diseases,
)
from txgnn.predict.repurposing import (
    find_repurposing_candidates_eu,
    generate_repurposing_report,
    load_drug_disease_relations,
)


def main():
    print("=" * 60)
    print("執行知識圖譜方法預測 - 歐盟版")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent

    # 1. 載入整合資料
    print("1. 載入整合資料...")
    integrated_data = load_integrated_data()
    ema_drugs = integrated_data["ema_drugs"]
    mapped_ingredients = integrated_data["mapped_ingredients"]
    metadata = integrated_data["metadata"]

    print(f"   EMA 核心藥品: {metadata['ema_drugs_count']}")
    print(f"   已映射成分: {metadata['mapped_to_drugbank']}")

    # 2. 載入疾病詞彙
    print("\n2. 載入疾病詞彙...")
    disease_df = load_disease_vocab()
    print(f"   疾病詞彙數: {len(disease_df)}")

    # 3. 執行疾病映射
    print("\n3. 執行疾病映射...")
    ema_df = pd.DataFrame(ema_drugs)
    indication_mapping = map_fda_indications_to_diseases(
        ema_df,
        disease_df=disease_df,
        indication_field="therapeutic_indication",
        license_field="license_id",
        brand_field="brand_name",
    )

    mapped_indications = indication_mapping["disease_id"].notna().sum()
    total_indications = len(indication_mapping)
    mapping_rate = mapped_indications / total_indications if total_indications > 0 else 0

    print(f"   總適應症數: {total_indications}")
    print(f"   映射成功: {mapped_indications} ({mapping_rate*100:.1f}%)")

    # 儲存適應症映射
    output_dir = base_dir / "data" / "processed"
    output_dir.mkdir(parents=True, exist_ok=True)

    indication_output = output_dir / "indication_mapping.csv"
    indication_mapping.to_csv(indication_output, index=False)
    print(f"   已儲存: {indication_output.name}")

    # 4. 載入 TxGNN 關係
    print("\n4. 載入 TxGNN 藥物-疾病關係...")
    relations_df = load_drug_disease_relations()
    indication_relations = relations_df[relations_df["relation"].isin(["indication", "off-label use"])]
    print(f"   適應症關係數: {len(indication_relations)}")

    # 5. 尋找老藥新用候選
    print("\n5. 尋找老藥新用候選...")
    candidates = find_repurposing_candidates_eu(
        mapped_ingredients=mapped_ingredients,
        ema_drugs=ema_drugs,
        indication_mapping_df=indication_mapping,
        relations_df=relations_df,
    )
    print(f"   候選數: {len(candidates)}")

    # 6. 生成報告
    print("\n6. 生成統計報告...")
    report = generate_repurposing_report(candidates, region="EU")

    print(f"   總候選數: {report['total_candidates']}")
    print(f"   涉及藥物: {report['unique_drugs']}")
    print(f"   涉及疾病: {report['unique_diseases']}")

    if report['top_diseases']:
        print("\n   最常見潛在新適應症:")
        for disease, count in list(report['top_diseases'].items())[:5]:
            print(f"     - {disease}: {count}")

    if report['top_drugs']:
        print("\n   最多新適應症的藥物:")
        for drug, count in list(report['top_drugs'].items())[:5]:
            print(f"     - {drug}: {count}")

    # 7. 儲存結果
    print("\n7. 儲存結果...")
    candidates_output = output_dir / "repurposing_candidates.csv"
    candidates.to_csv(candidates_output, index=False)
    print(f"   已儲存: {candidates_output}")

    # 儲存報告 JSON
    report_output = output_dir / "repurposing_report.json"
    with open(report_output, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print(f"   已儲存: {report_output}")

    print("\n" + "=" * 60)
    print("完成！")
    print("=" * 60)

    print("\n下一步: 生成 FHIR 資源")
    print("  uv run python scripts/generate_fhir_resources.py")


if __name__ == "__main__":
    main()
