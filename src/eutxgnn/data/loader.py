"""EMA 藥品資料載入與過濾

支援兩種資料格式：
1. eu_ema_drugs.json - 僅 EMA 核心藥品
2. eu_integrated_drugs.json - 整合 EMA + Article 57 + DrugBank 映射
"""

import json
from pathlib import Path
from typing import Optional

import pandas as pd
import yaml


def load_field_config() -> dict:
    """載入欄位映射設定"""
    config_path = Path(__file__).parent.parent.parent.parent / "config" / "fields.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def _clean_field_name(name: str) -> str:
    """清理欄位名稱（移除換行符）"""
    return name.replace("\n", " ").strip() if name else ""


def load_integrated_data(filepath: Optional[Path] = None) -> dict:
    """載入整合後的資料（EMA + Article 57 + DrugBank 映射）

    Args:
        filepath: JSON 檔案路徑，預設為 data/processed/eu_integrated_drugs.json

    Returns:
        整合資料字典，包含：
        - metadata: 統計摘要
        - ema_drugs: EMA 核心藥品列表
        - mapped_ingredients: 已映射至 DrugBank 的成分
        - unmapped_ingredients_sample: 未映射成分範例
    """
    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "processed" / "eu_integrated_drugs.json"

    if not filepath.exists():
        raise FileNotFoundError(
            f"找不到整合資料: {filepath}\n"
            f"請先執行: uv run python scripts/process_fda_data.py"
        )

    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def load_fda_drugs(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入 EMA 藥品資料

    Args:
        filepath: JSON 檔案路徑，預設為 data/raw/eu_ema_drugs.json

    Returns:
        包含所有藥品的 DataFrame

    Raises:
        FileNotFoundError: 找不到資料檔案時，提供下載指引
    """
    config = load_field_config()

    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "raw" / "eu_ema_drugs.json"

    if not filepath.exists():
        raise FileNotFoundError(
            f"找不到藥品資料: {filepath}\n"
            f"請先執行以下步驟：\n"
            f"1. 下載 EMA 資料:\n"
            f'   curl -L -o data/raw/ema_medicines.xlsx "https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx"\n'
            f"2. 處理資料:\n"
            f"   uv run python scripts/process_fda_data.py"
        )

    with open(filepath, "r", encoding=config.get("encoding", "utf-8")) as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    return df


def filter_active_drugs(df: pd.DataFrame) -> pd.DataFrame:
    """過濾有效藥品（排除已註銷）

    Args:
        df: 原始藥品 DataFrame

    Returns:
        僅包含有效藥品的 DataFrame
    """
    config = load_field_config()
    field_mapping = config["field_mapping"]
    active_statuses = config.get("active_statuses", ["Authorised"])

    # 取得狀態欄位名稱
    status_field = _clean_field_name(field_mapping.get("status", ""))

    if status_field and status_field in df.columns:
        # 僅保留有效狀態的藥品
        active = df[df[status_field].isin(active_statuses)].copy()
    else:
        active = df.copy()

    # 過濾有主成分的藥品（TxGNN 需要）
    ingredients_field = _clean_field_name(field_mapping.get("ingredients", ""))
    if ingredients_field and ingredients_field in df.columns:
        active = active[active[ingredients_field].notna() & (active[ingredients_field] != "")]

    # 重設索引
    active = active.reset_index(drop=True)

    return active


def get_drug_summary(df: pd.DataFrame) -> dict:
    """取得藥品資料摘要統計

    Args:
        df: 藥品 DataFrame

    Returns:
        摘要統計字典
    """
    config = load_field_config()
    field_mapping = config["field_mapping"]

    ingredients_field = _clean_field_name(field_mapping.get("ingredients", ""))
    indication_field = _clean_field_name(field_mapping.get("indication", ""))
    therapeutic_area_field = _clean_field_name(field_mapping.get("therapeutic_area", ""))
    status_field = _clean_field_name(field_mapping.get("status", ""))

    summary = {"total_count": len(df)}

    if ingredients_field and ingredients_field in df.columns:
        summary["with_ingredient"] = int(df[ingredients_field].notna().sum())
        summary["unique_ingredients"] = int(df[ingredients_field].nunique())

    if indication_field and indication_field in df.columns:
        summary["with_indication"] = int(df[indication_field].notna().sum())

    if therapeutic_area_field and therapeutic_area_field in df.columns:
        summary["with_therapeutic_area"] = int(df[therapeutic_area_field].notna().sum())

    if status_field and status_field in df.columns:
        summary["status_distribution"] = df[status_field].value_counts().to_dict()

    return summary


def get_active_drug_ingredients(df: pd.DataFrame = None) -> list[str]:
    """取得所有有效藥品的成分列表

    Args:
        df: 藥品 DataFrame，如未提供則自動載入

    Returns:
        成分名稱列表（去重）
    """
    if df is None:
        df = load_fda_drugs()
        df = filter_active_drugs(df)

    config = load_field_config()
    field_mapping = config["field_mapping"]
    ingredients_field = _clean_field_name(field_mapping.get("ingredients", ""))
    separator = config.get("ingredient_separator", ";")

    ingredients = set()
    if ingredients_field and ingredients_field in df.columns:
        for value in df[ingredients_field].dropna():
            # 處理多成分
            for ingredient in str(value).split(separator):
                ingredient = ingredient.strip()
                if ingredient:
                    ingredients.add(ingredient)

    return sorted(ingredients)


def get_mapped_ingredients() -> list[dict]:
    """取得所有已映射至 DrugBank 的成分

    Returns:
        成分列表，每個包含 ingredient 和 drugbank_id
    """
    data = load_integrated_data()
    return data.get("mapped_ingredients", [])


def get_drugbank_ids() -> list[str]:
    """取得所有已映射的 DrugBank ID

    Returns:
        DrugBank ID 列表（去重）
    """
    mapped = get_mapped_ingredients()
    return sorted(set(item["drugbank_id"] for item in mapped))


def get_integration_stats() -> dict:
    """取得整合資料統計

    Returns:
        統計資訊字典
    """
    data = load_integrated_data()
    return data.get("metadata", {})
