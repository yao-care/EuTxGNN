#!/usr/bin/env python3
"""重建 data/processed/repurposing_candidates_merged.csv。

collect_evidence.py 與 FHIR 生成都以這個檔為輸入，但它已從 repo 遺失
（evidence_summary.json 記錄的 32,368 配對就是它的產物）。這裡從仍在的兩份
上游資料重建：

  - data/processed/txgnn_dl_predictions.csv.gz   DL 預測，有 txgnn_score
  - data/processed/repurposing_candidates.csv.gz KG 候選，無 score

合併規則與其他站的藥品頁／FHIR 一致：同藥同適應症去重（DL 優先，因為它帶分數），
每個藥依分數取前 TOP_PER_DRUG 筆。KG-only 的配對沒有模型分數，給 0.0 並保留
其 source 標記，不推算分數。

用法:
    python3 scripts/rebuild_merged_candidates.py [--apply]
"""
import csv
import gzip
import sys
from collections import defaultdict
from pathlib import Path

TOP_PER_DRUG = 50
BASE = Path(__file__).resolve().parent.parent
PROCESSED = BASE / "data" / "processed"
OUT = PROCESSED / "repurposing_candidates_merged.csv"
FIELDS = ["license_id", "brand_name", "ingredient", "drugbank_id",
          "potential_indication", "source", "score"]


def load_kg():
    """KG 候選：帶 license_id / brand_name / ingredient，但沒有分數。"""
    rows = []
    meta = {}
    p = PROCESSED / "repurposing_candidates.csv.gz"
    with gzip.open(p, "rt", encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            did = (r.get("drugbank_id") or "").strip().upper()
            ind = (r.get("potential_indication") or "").strip()
            if not did or not ind:
                continue
            meta.setdefault(did, {
                "license_id": r.get("license_id", ""),
                "brand_name": r.get("brand_name", ""),
                "ingredient": r.get("ingredient", ""),
            })
            rows.append({
                "drugbank_id": did,
                "potential_indication": ind,
                "source": r.get("source") or "TxGNN Knowledge Graph",
                "score": 0.0,
            })
    return rows, meta


def load_dl():
    """DL 預測：欄名為在地化的『潛在新適應症』『來源』，且檔頭有 BOM。"""
    rows = []
    names = {}
    p = PROCESSED / "txgnn_dl_predictions.csv.gz"
    with gzip.open(p, "rt", encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            did = (r.get("drugbank_id") or "").strip().upper()
            ind = (r.get("潛在新適應症") or "").strip()
            if not did or not ind:
                continue
            try:
                score = float(r.get("txgnn_score") or 0)
            except ValueError:
                score = 0.0
            names.setdefault(did, (r.get("drug_name") or "").strip())
            rows.append({
                "drugbank_id": did,
                "potential_indication": ind,
                "source": r.get("來源") or "TxGNN Deep Learning Model",
                "score": score,
            })
    return rows, names


def main():
    apply = "--apply" in sys.argv
    kg_rows, kg_meta = load_kg()
    dl_rows, dl_names = load_dl()
    print(f"KG 候選={len(kg_rows)} 列 / {len(kg_meta)} 藥")
    print(f"DL 預測={len(dl_rows)} 列 / {len(dl_names)} 藥")

    # DL 先放，KG 後放：同一組 (藥, 適應症) 保留先出現的那筆，讓帶分數的 DL 勝出
    per = defaultdict(list)
    seen = set()
    for r in dl_rows + kg_rows:
        key = (r["drugbank_id"], r["potential_indication"])
        if key in seen:
            continue
        seen.add(key)
        per[r["drugbank_id"]].append(r)

    out = []
    for did, rows in per.items():
        rows.sort(key=lambda x: -x["score"])
        m = kg_meta.get(did, {})
        ingredient = m.get("ingredient") or dl_names.get(did) or did
        for r in rows[:TOP_PER_DRUG]:
            out.append({
                "license_id": m.get("license_id", ""),
                "brand_name": m.get("brand_name", ""),
                "ingredient": ingredient,
                "drugbank_id": did,
                "potential_indication": r["potential_indication"],
                "source": r["source"],
                "score": f"{r['score']:.6f}",
            })

    print(f"合併後={len(out)} 列 / {len(per)} 藥（每藥上限 {TOP_PER_DRUG}）")
    if not apply:
        print("DRY-RUN（加 --apply 才寫檔）")
        return
    with open(OUT, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(out)
    print(f"已寫入 {OUT}")


main()
