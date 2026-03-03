#!/usr/bin/env python3
"""處理歐盟藥品資料

整合兩個資料來源：
1. EMA Medicines Report - 集中授權藥品（有完整適應症）
2. Article 57 Database - 所有 EEA 藥品（僅成分，無適應症）

使用方法:
    uv run python scripts/process_fda_data.py

前置條件:
    需要先下載資料檔案到 data/raw/ 目錄：
    1. EMA: https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx
    2. Article 57: https://www.ema.europa.eu/documents/other/article-57-product-data_en.xlsx

產生檔案:
    data/raw/eu_ema_drugs.json - EMA 核心藥品
    data/raw/eu_article57_ingredients.json - Article 57 成分清單
    data/processed/eu_integrated_drugs.json - 整合後的資料
"""

import json
from pathlib import Path

import pandas as pd
import yaml


def load_field_config() -> dict:
    """載入欄位映射設定"""
    config_path = Path(__file__).parent.parent / "config" / "fields.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def process_ema_medicines(raw_dir: Path, config: dict) -> list:
    """處理 EMA Medicines Report

    Returns:
        EMA 藥品列表
    """
    print("\n" + "=" * 60)
    print("步驟 1/3: 處理 EMA Medicines Report")
    print("=" * 60)

    # 尋找 EMA Excel 檔案
    ema_files = list(raw_dir.glob("*ema*.xlsx")) + list(raw_dir.glob("*medicines*.xlsx"))
    ema_files = [f for f in ema_files if "article57" not in f.name.lower()]

    if not ema_files:
        print("  [警告] 找不到 EMA Medicines Report，跳過")
        return []

    input_path = ema_files[0]
    print(f"  檔案: {input_path.name}")
    print(f"  大小: {input_path.stat().st_size / 1024:.1f} KB")

    # 讀取 Excel
    header_row = config.get("data_source", {}).get("header_row", 8)
    df = pd.read_excel(input_path, header=header_row)
    print(f"  原始筆數: {len(df)}")

    # 篩選人用藥品
    category_filter = config.get("category_filter", "Human")
    if "Category" in df.columns:
        df = df[df["Category"] == category_filter].copy()
        print(f"  篩選人用藥品: {len(df)}")

    # 清理欄位名稱
    df.columns = [col.replace("\n", " ").strip() for col in df.columns]

    # 篩選有效藥品
    if "Medicine status" in df.columns:
        active_df = df[df["Medicine status"] == "Authorised"].copy()
        print(f"  有效藥品 (Authorised): {len(active_df)}")
    else:
        active_df = df.copy()

    # 轉換為字典列表
    data = []
    for _, row in active_df.iterrows():
        record = {
            "source": "EMA",
            "license_id": row.get("EMA product number"),
            "brand_name": row.get("Name of medicine"),
            "inn_name": row.get("International non-proprietary name (INN) / common name"),
            "active_substance": row.get("Active substance"),
            "therapeutic_indication": row.get("Therapeutic indication"),
            "therapeutic_area_mesh": row.get("Therapeutic area (MeSH)"),
            "atc_code": row.get("ATC code (human)"),
            "status": row.get("Medicine status"),
            "authorization_date": None,
            "url": row.get("Medicine URL"),
        }

        # 處理日期
        auth_date = row.get("Marketing authorisation date")
        if pd.notna(auth_date):
            if hasattr(auth_date, "strftime"):
                record["authorization_date"] = auth_date.strftime("%Y-%m-%d")
            else:
                record["authorization_date"] = str(auth_date)

        # 清理 None 值
        record = {k: (v if pd.notna(v) else None) for k, v in record.items()}
        data.append(record)

    # 儲存 EMA 資料
    output_path = raw_dir / "eu_ema_drugs.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  儲存: {output_path.name}")

    return data


def process_article57(raw_dir: Path) -> list:
    """處理 Article 57 Database

    Returns:
        Article 57 成分列表
    """
    print("\n" + "=" * 60)
    print("步驟 2/3: 處理 Article 57 Database")
    print("=" * 60)

    # 尋找 Article 57 檔案
    art57_files = list(raw_dir.glob("*article57*.xlsx"))

    if not art57_files:
        print("  [警告] 找不到 Article 57 資料，跳過")
        return []

    input_path = art57_files[0]
    print(f"  檔案: {input_path.name}")
    print(f"  大小: {input_path.stat().st_size / 1024 / 1024:.1f} MB")

    # 讀取 Excel（標題在第 19 行）
    df = pd.read_excel(input_path, header=19)
    df.columns = [c.split("\n")[0].strip() for c in df.columns]
    print(f"  總筆數: {len(df):,}")

    # 提取所有不重複成分
    all_ingredients = {}
    for _, row in df.iterrows():
        substance = row.get("Active substance", "")
        country = row.get("Product authorisation country", "")
        route = row.get("Route of administration", "")

        if not substance or pd.isna(substance):
            continue

        # 分割多成分（用 | 分隔）
        for ing in str(substance).split("|"):
            ing = ing.strip()
            if not ing:
                continue

            if ing not in all_ingredients:
                all_ingredients[ing] = {
                    "active_substance": ing,
                    "countries": set(),
                    "routes": set(),
                    "count": 0,
                }

            all_ingredients[ing]["count"] += 1
            if country and pd.notna(country):
                all_ingredients[ing]["countries"].add(country)
            if route and pd.notna(route):
                all_ingredients[ing]["routes"].add(route)

    # 轉換為列表
    data = []
    for ing, info in all_ingredients.items():
        data.append({
            "source": "Article57",
            "active_substance": info["active_substance"],
            "countries": sorted(info["countries"]),
            "routes": sorted(info["routes"]),
            "product_count": info["count"],
        })

    print(f"  不重複成分數: {len(data):,}")

    # 儲存 Article 57 成分清單
    output_path = raw_dir / "eu_article57_ingredients.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  儲存: {output_path.name}")

    return data


def integrate_and_map(ema_data: list, article57_data: list, base_dir: Path) -> dict:
    """整合資料並執行 DrugBank 映射

    Returns:
        整合後的資料統計
    """
    print("\n" + "=" * 60)
    print("步驟 3/3: 整合資料與 DrugBank 映射")
    print("=" * 60)

    # 載入 DrugBank 詞彙表
    drugbank_path = base_dir / "data" / "external" / "drugbank_vocab.csv"
    if not drugbank_path.exists():
        print("  [警告] DrugBank 詞彙表不存在，請先執行 prepare_external_data.py")
        return {}

    from txgnn.mapping.drugbank_mapper import load_drugbank_vocab, build_name_index, map_ingredient_to_drugbank

    drugbank_df = load_drugbank_vocab(drugbank_path)
    name_index = build_name_index(drugbank_df)
    print(f"  DrugBank 詞彙: {len(drugbank_df)} 種藥物")

    # 收集所有成分並映射
    all_ingredients = set()

    # EMA 成分
    for drug in ema_data:
        substance = drug.get("active_substance", "")
        if substance:
            for ing in str(substance).split(";"):
                all_ingredients.add(ing.strip())

    # Article 57 成分
    for item in article57_data:
        substance = item.get("active_substance", "")
        if substance:
            all_ingredients.add(substance)

    print(f"  總成分數: {len(all_ingredients):,}")

    # 執行映射
    mapped_ingredients = []
    unmapped_ingredients = []

    for ing in all_ingredients:
        if not ing:
            continue
        drugbank_id = map_ingredient_to_drugbank(ing, name_index)
        if drugbank_id:
            mapped_ingredients.append({
                "ingredient": ing,
                "drugbank_id": drugbank_id,
            })
        else:
            unmapped_ingredients.append(ing)

    print(f"  成功映射: {len(mapped_ingredients)} ({100*len(mapped_ingredients)/len(all_ingredients):.1f}%)")
    print(f"  未映射: {len(unmapped_ingredients)}")

    # 建立整合資料
    integrated_data = {
        "metadata": {
            "ema_drugs_count": len(ema_data),
            "article57_ingredients_count": len(article57_data),
            "total_unique_ingredients": len(all_ingredients),
            "mapped_to_drugbank": len(mapped_ingredients),
            "mapping_rate": len(mapped_ingredients) / len(all_ingredients) if all_ingredients else 0,
        },
        "ema_drugs": ema_data,
        "mapped_ingredients": mapped_ingredients,
        "unmapped_ingredients_sample": sorted(unmapped_ingredients)[:100],
    }

    # 儲存整合資料
    output_path = base_dir / "data" / "processed" / "eu_integrated_drugs.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(integrated_data, f, ensure_ascii=False, indent=2)
    print(f"  儲存: {output_path}")

    return integrated_data["metadata"]


def print_summary(stats: dict):
    """列印最終摘要"""
    print("\n" + "=" * 60)
    print("整合結果摘要")
    print("=" * 60)

    if not stats:
        print("  無資料")
        return

    print(f"  EMA 核心藥品: {stats.get('ema_drugs_count', 0):,}")
    print(f"  Article 57 成分: {stats.get('article57_ingredients_count', 0):,}")
    print(f"  總不重複成分: {stats.get('total_unique_ingredients', 0):,}")
    print(f"  DrugBank 映射成功: {stats.get('mapped_to_drugbank', 0):,}")
    print(f"  映射率: {stats.get('mapping_rate', 0)*100:.1f}%")


def main():
    print("=" * 60)
    print("處理歐盟藥品資料 (EMA + Article 57)")
    print("=" * 60)

    base_dir = Path(__file__).parent.parent
    raw_dir = base_dir / "data" / "raw"

    # 確保目錄存在
    raw_dir.mkdir(parents=True, exist_ok=True)

    # 載入設定
    config = load_field_config()

    # 處理兩個資料來源
    ema_data = process_ema_medicines(raw_dir, config)
    article57_data = process_article57(raw_dir)

    # 整合並映射
    if ema_data or article57_data:
        stats = integrate_and_map(ema_data, article57_data, base_dir)
        print_summary(stats)
    else:
        print("\n[錯誤] 無資料可處理")

    print("\n下一步: 執行知識圖譜預測")
    print("  uv run python scripts/run_kg_prediction.py")


if __name__ == "__main__":
    main()
