"""疾病映射模組 - EMA 英文適應症映射至 TxGNN 疾病本體

由於 EMA 資料本身就是英文，不需要翻譯表。
主要功能是從適應症文字中提取疾病關鍵詞並映射到 TxGNN 疾病 ID。
"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd


# EMA 資料是英文，不需要翻譯表
# 但保留結構以便未來擴展其他語言
DISEASE_DICT: Dict[str, str] = {}


def load_disease_vocab(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入 TxGNN 疾病詞彙表"""
    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "external" / "disease_vocab.csv"
    return pd.read_csv(filepath)


def build_disease_index(disease_df: pd.DataFrame) -> Dict[str, Tuple[str, str]]:
    """建立疾病名稱索引（關鍵詞 -> (disease_id, disease_name)）"""
    index = {}

    for _, row in disease_df.iterrows():
        disease_id = row["disease_id"]
        disease_name = row["disease_name"]
        name_upper = row["disease_name_upper"]

        # 完整名稱
        index[name_upper] = (disease_id, disease_name)

        # 提取關鍵詞（按空格和逗號分割）
        keywords = re.split(r"[,\s\-]+", name_upper)
        for kw in keywords:
            kw = kw.strip()
            if len(kw) > 3 and kw not in index:
                index[kw] = (disease_id, disease_name)

    return index


def extract_indications(indication_str: str) -> List[str]:
    """從適應症文字提取個別適應症

    EMA 適應症格式為英文完整句子，例如：
    "Treatment of epilepsy in adults and children over 2 years"
    """
    if not indication_str:
        return []

    text = indication_str.strip()

    # 按句號、分號分割
    parts = re.split(r"[.;]", text)

    indications = []
    for part in parts:
        part = part.strip()
        if part and len(part) >= 5:
            indications.append(part)

    return indications


def translate_indication(indication: str) -> List[str]:
    """從英文適應症中提取疾病關鍵詞

    EMA 資料已是英文，直接提取關鍵詞即可。
    """
    keywords = []

    # 常見疾病關鍵詞模式
    disease_patterns = [
        # 癌症
        r"\b(\w+\s+)?cancer\b",
        r"\b(\w+\s+)?carcinoma\b",
        r"\b(\w+\s+)?lymphoma\b",
        r"\b(\w+\s+)?leukemia\b",
        r"\b(\w+\s+)?melanoma\b",
        r"\b(\w+\s+)?myeloma\b",
        r"\b(\w+\s+)?tumor\b",
        r"\b(\w+\s+)?tumour\b",
        # 感染
        r"\b(\w+\s+)?infection\b",
        r"\b(hiv|aids)\b",
        r"\bhepatitis\s*[a-c]?\b",
        # 心血管
        r"\bhypertension\b",
        r"\bheart\s+failure\b",
        r"\batrial\s+fibrillation\b",
        r"\bcoronary\s+artery\s+disease\b",
        # 神經
        r"\bepilepsy\b",
        r"\bparkinson\b",
        r"\balzheimer\b",
        r"\bmultiple\s+sclerosis\b",
        r"\bmigraine\b",
        # 精神
        r"\bdepression\b",
        r"\bschizophrenia\b",
        r"\bbipolar\b",
        r"\banxiety\b",
        # 代謝/內分泌
        r"\bdiabetes\b",
        r"\bobesity\b",
        r"\bhyperlipidemia\b",
        r"\bhypothyroidism\b",
        # 自身免疫/風濕
        r"\brheumatoid\s+arthritis\b",
        r"\bpsoriasis\b",
        r"\blupus\b",
        r"\bcrohn\b",
        r"\bulcerative\s+colitis\b",
        # 呼吸
        r"\basthma\b",
        r"\bcopd\b",
        r"\bpulmonary\s+fibrosis\b",
        # 其他
        r"\bhemophilia\b",
        r"\bcystic\s+fibrosis\b",
        r"\bosteoporosis\b",
        r"\bglaucoma\b",
    ]

    indication_lower = indication.lower()

    for pattern in disease_patterns:
        matches = re.findall(pattern, indication_lower)
        for match in matches:
            if isinstance(match, tuple):
                kw = " ".join(m for m in match if m).strip().upper()
            else:
                kw = match.strip().upper()
            if kw:
                keywords.append(kw)

    return keywords


def map_indication_to_disease(
    indication: str,
    disease_index: Dict[str, Tuple[str, str]],
) -> List[Tuple[str, str, float]]:
    """將單一適應症映射到 TxGNN 疾病

    Returns:
        [(disease_id, disease_name, confidence), ...]
    """
    results = []

    # 提取疾病關鍵詞
    keywords = translate_indication(indication)

    # 同時嘗試從適應症文字直接搜尋
    indication_upper = indication.upper()

    for kw in keywords:
        # 完全匹配
        if kw in disease_index:
            disease_id, disease_name = disease_index[kw]
            results.append((disease_id, disease_name, 1.0))
            continue

        # 部分匹配
        for index_kw, (disease_id, disease_name) in disease_index.items():
            if kw in index_kw or index_kw in kw:
                results.append((disease_id, disease_name, 0.8))

    # 額外：直接在疾病索引中搜尋適應症文字
    for index_kw, (disease_id, disease_name) in disease_index.items():
        if len(index_kw) > 5 and index_kw in indication_upper:
            results.append((disease_id, disease_name, 0.7))

    # 去重並按信心度排序
    seen = set()
    unique_results = []
    for disease_id, disease_name, conf in sorted(results, key=lambda x: -x[2]):
        if disease_id not in seen:
            seen.add(disease_id)
            unique_results.append((disease_id, disease_name, conf))

    return unique_results[:5]


def map_fda_indications_to_diseases(
    fda_df: pd.DataFrame,
    disease_df: Optional[pd.DataFrame] = None,
    indication_field: str = "Therapeutic indication",
    license_field: str = "EMA product number",
    brand_field: str = "Name of medicine",
) -> pd.DataFrame:
    """將 EMA 藥品適應症映射到 TxGNN 疾病"""
    if disease_df is None:
        disease_df = load_disease_vocab()

    disease_index = build_disease_index(disease_df)

    results = []

    for _, row in fda_df.iterrows():
        indication_str = row.get(indication_field, "")
        if not indication_str or pd.isna(indication_str):
            continue

        # 提取個別適應症
        indications = extract_indications(str(indication_str))

        for ind in indications:
            # 映射
            matches = map_indication_to_disease(ind, disease_index)

            if matches:
                for disease_id, disease_name, confidence in matches:
                    results.append({
                        "license_id": row.get(license_field, ""),
                        "brand_name": row.get(brand_field, ""),
                        "original_indication": str(indication_str)[:200],
                        "extracted_indication": ind[:100],
                        "disease_id": disease_id,
                        "disease_name": disease_name,
                        "confidence": confidence,
                    })
            else:
                results.append({
                    "license_id": row.get(license_field, ""),
                    "brand_name": row.get(brand_field, ""),
                    "original_indication": str(indication_str)[:200],
                    "extracted_indication": ind[:100],
                    "disease_id": None,
                    "disease_name": None,
                    "confidence": 0,
                })

    return pd.DataFrame(results)


def get_indication_mapping_stats(mapping_df: pd.DataFrame) -> dict:
    """計算適應症映射統計"""
    total = len(mapping_df)
    mapped = mapping_df["disease_id"].notna().sum()
    unique_indications = mapping_df["extracted_indication"].nunique()
    unique_diseases = mapping_df[mapping_df["disease_id"].notna()]["disease_id"].nunique()

    return {
        "total_indications": total,
        "mapped_indications": int(mapped),
        "mapping_rate": mapped / total if total > 0 else 0,
        "unique_indications": unique_indications,
        "unique_diseases": unique_diseases,
    }
