"""老藥新用預測 - 基於 TxGNN 知識圖譜

支援多地區藥品資料格式（EU、TW 等）。
"""

from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

import pandas as pd


def load_drug_disease_relations(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入 TxGNN 藥物-疾病關係

    Args:
        filepath: CSV 檔案路徑

    Returns:
        藥物-疾病關係 DataFrame
    """
    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "external" / "drug_disease_relations.csv"

    return pd.read_csv(filepath)


def build_drug_indication_map(relations_df: pd.DataFrame) -> Dict[str, Set[str]]:
    """建立藥物 -> 適應症集合的映射

    Args:
        relations_df: 藥物-疾病關係 DataFrame

    Returns:
        {drug_name: {disease1, disease2, ...}}
    """
    # 只取 indication 和 off-label use
    indications = relations_df[relations_df["relation"].isin(["indication", "off-label use"])]

    drug_map = {}
    for _, row in indications.iterrows():
        drug = row["x_name"].upper()
        disease = row["y_name"]

        if drug not in drug_map:
            drug_map[drug] = set()
        drug_map[drug].add(disease)

    return drug_map


def find_repurposing_candidates_eu(
    mapped_ingredients: List[dict],
    ema_drugs: List[dict],
    indication_mapping_df: pd.DataFrame,
    relations_df: Optional[pd.DataFrame] = None,
) -> pd.DataFrame:
    """找出歐盟藥品老藥新用候選

    Args:
        mapped_ingredients: 已映射至 DrugBank 的成分列表
        ema_drugs: EMA 核心藥品列表
        indication_mapping_df: 適應症疾病映射結果
        relations_df: TxGNN 藥物-疾病關係

    Returns:
        老藥新用候選 DataFrame
    """
    if relations_df is None:
        relations_df = load_drug_disease_relations()

    # 建立 TxGNN 藥物適應症映射
    kg_drug_map = build_drug_indication_map(relations_df)

    # 建立成分 -> DrugBank ID 映射
    ingredient_to_drugbank = {
        item["ingredient"].upper(): item["drugbank_id"]
        for item in mapped_ingredients
    }

    # 建立 EMA 藥品的現有適應症
    existing_diseases = {}
    if len(indication_mapping_df) > 0:
        valid_mappings = indication_mapping_df[
            indication_mapping_df["disease_name"].notna()
        ]
        for _, row in valid_mappings.iterrows():
            license_id = row.get("license_id", "")
            if license_id not in existing_diseases:
                existing_diseases[license_id] = set()
            existing_diseases[license_id].add(row["disease_name"].lower())

    candidates = []

    # 遍歷 EMA 藥品
    for drug in ema_drugs:
        license_id = drug.get("license_id", "")
        brand_name = drug.get("brand_name", "")
        active_substance = drug.get("active_substance", "")

        if not active_substance:
            continue

        # 處理多成分（用分號分隔）
        for ingredient in str(active_substance).split(";"):
            ingredient = ingredient.strip().upper()
            if not ingredient:
                continue

            # 取得 DrugBank ID
            drugbank_id = ingredient_to_drugbank.get(ingredient)
            if not drugbank_id:
                continue

            # 查詢 TxGNN 中該藥物的所有適應症
            kg_diseases = kg_drug_map.get(ingredient, set())
            if not kg_diseases:
                continue

            # 取得現有適應症
            current_diseases = existing_diseases.get(license_id, set())

            # 找出潛在新適應症
            for disease in kg_diseases:
                disease_lower = disease.lower()

                # 檢查是否已存在
                is_new = all(
                    curr_d not in disease_lower and disease_lower not in curr_d
                    for curr_d in current_diseases
                )

                if is_new:
                    candidates.append({
                        "license_id": license_id,
                        "brand_name": brand_name,
                        "ingredient": ingredient,
                        "drugbank_id": drugbank_id,
                        "potential_indication": disease,
                        "source": "TxGNN Knowledge Graph",
                    })

    result_df = pd.DataFrame(candidates)

    # 去重
    if len(result_df) > 0:
        result_df = result_df.drop_duplicates(
            subset=["license_id", "ingredient", "potential_indication"]
        )

    return result_df


def find_repurposing_candidates(
    drug_mapping_df: pd.DataFrame,
    indication_mapping_df: pd.DataFrame,
    relations_df: Optional[pd.DataFrame] = None,
) -> pd.DataFrame:
    """找出老藥新用候選（台灣版）

    比較台灣藥品的現有適應症與 TxGNN 知識圖譜中的適應症，
    找出可能的新適應症。

    Args:
        drug_mapping_df: 藥品 DrugBank 映射結果
        indication_mapping_df: 適應症疾病映射結果
        relations_df: TxGNN 藥物-疾病關係

    Returns:
        老藥新用候選 DataFrame
    """
    if relations_df is None:
        relations_df = load_drug_disease_relations()

    # 建立 TxGNN 藥物適應症映射
    kg_drug_map = build_drug_indication_map(relations_df)

    # 建立台灣藥品的現有適應症（向量化操作）
    tw_diseases_df = indication_mapping_df[
        indication_mapping_df["disease_name"].notna()
    ][["許可證字號", "disease_name"]].copy()
    tw_diseases_df["disease_lower"] = tw_diseases_df["disease_name"].str.lower()
    tw_drug_diseases = tw_diseases_df.groupby("許可證字號")["disease_lower"].apply(set).to_dict()

    # 建立藥品資訊索引（向量化）
    valid_drugs = drug_mapping_df[drug_mapping_df["drugbank_id"].notna()].copy()
    drug_info_map = valid_drugs.groupby(["許可證字號", "標準化成分"]).first().to_dict("index")

    # 取得唯一的 (許可證字號, 藥物成分) 組合
    unique_pairs = valid_drugs[["許可證字號", "標準化成分", "中文品名", "drugbank_id"]].drop_duplicates()

    candidates = []

    for _, row in unique_pairs.iterrows():
        license_no = row["許可證字號"]
        drug_name = row["標準化成分"]

        # 查詢 TxGNN 中該藥物的所有適應症
        kg_diseases = kg_drug_map.get(drug_name, set())
        if not kg_diseases:
            continue

        # 取得台灣現有適應症
        tw_diseases = tw_drug_diseases.get(license_no, set())

        # 找出潛在新適應症
        for disease in kg_diseases:
            disease_lower = disease.lower()

            # 快速檢查是否已存在
            is_new = all(
                tw_d not in disease_lower and disease_lower not in tw_d
                for tw_d in tw_diseases
            )

            if is_new:
                candidates.append({
                    "許可證字號": license_no,
                    "中文品名": row["中文品名"],
                    "藥物成分": drug_name,
                    "drugbank_id": row["drugbank_id"],
                    "潛在新適應症": disease,
                    "來源": "TxGNN Knowledge Graph",
                })

    result_df = pd.DataFrame(candidates)

    # 去重
    if len(result_df) > 0:
        result_df = result_df.drop_duplicates(
            subset=["許可證字號", "藥物成分", "潛在新適應症"]
        )

    return result_df


def generate_repurposing_report(candidates_df: pd.DataFrame, region: str = "TW") -> dict:
    """生成老藥新用報告統計

    Args:
        candidates_df: 候選藥物 DataFrame
        region: 地區代碼 ("TW" 或 "EU")

    Returns:
        統計報告字典
    """
    if len(candidates_df) == 0:
        return {
            "total_candidates": 0,
            "unique_drugs": 0,
            "unique_diseases": 0,
            "top_diseases": [],
            "top_drugs": [],
        }

    # 根據地區選擇欄位名稱
    if region == "EU":
        drug_col = "ingredient"
        disease_col = "potential_indication"
    else:
        drug_col = "藥物成分"
        disease_col = "潛在新適應症"

    unique_drugs = candidates_df[drug_col].nunique()
    unique_diseases = candidates_df[disease_col].nunique()

    # 最常見的潛在新適應症
    top_diseases = candidates_df[disease_col].value_counts().head(10).to_dict()

    # 最多潛在新適應症的藥物
    drug_counts = candidates_df.groupby(drug_col)[disease_col].nunique()
    top_drugs = drug_counts.sort_values(ascending=False).head(10).to_dict()

    return {
        "total_candidates": len(candidates_df),
        "unique_drugs": unique_drugs,
        "unique_diseases": unique_diseases,
        "top_diseases": top_diseases,
        "top_drugs": top_drugs,
    }
