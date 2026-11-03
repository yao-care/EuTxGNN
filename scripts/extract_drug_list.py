#!/usr/bin/env python3
"""
Extract drug list from docs/_drugs/*.md files.
Creates a JSON file with drug names, evidence levels, and indication counts.
"""

import json
import re
from pathlib import Path


def parse_front_matter(content: str) -> dict:
    """Parse YAML front matter from markdown content."""
    if not content.startswith("---"):
        return {}

    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}

    front_matter = {}
    for line in parts[1].strip().split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            front_matter[key] = value

    return front_matter


def extract_predicted_indication(content: str) -> str:
    """Extract predicted indication from the drug report."""
    # Look for the pattern in the quick overview table
    match = re.search(r'\|\s*預測新適應症\s*\|\s*([^|]+)\s*\|', content)
    if match:
        return match.group(1).strip()
    return ""


def load_original_indications() -> tuple:
    """2026-11-03：原適應症（已知適應症）取自 docs/data/search-index.json 的 original 欄。

    本站該欄是 EMA 核准適應症英文原文（docs/data 產生時截到 200 字並加「...」，截掉的部分不會被排除），
    供檢查腳本把預測清單裡其實已核准的用途排除。檔案不存在或讀不到時回傳空表（排除不作用）。
    """
    path = Path(__file__).parent.parent / "docs" / "data" / "search-index.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}, {}
    by_slug, by_name = {}, {}
    for d in data.get("drugs", []):
        original = re.sub(r"\s*(\.\.\.|…)$", "", (d.get("original") or "").strip())
        if original:
            by_slug[d.get("slug", "")] = original
            by_name[(d.get("name") or "").lower()] = original
    return by_slug, by_name


def page_slug(md_file: Path, front_matter: dict) -> str:
    """與 search-index 相同的網址 slug：明寫 permalink 者以它為準，否則檔名 slugify。"""
    m = re.match(r"^/drugs/([^/]+)/?$", front_matter.get("permalink", ""))
    if m:
        return m.group(1)
    return re.sub(r"[\W_]+", "-", md_file.stem, flags=re.U).strip("-").lower()


def main():
    drugs_dir = Path(__file__).parent.parent / "docs" / "_drugs"
    output_file = Path(__file__).parent / "drug_list.json"
    original_by_slug, original_by_name = load_original_indications()

    drugs = []

    for md_file in sorted(drugs_dir.glob("*.md")):
        content = md_file.read_text(encoding="utf-8")
        front_matter = parse_front_matter(content)

        drug_name = front_matter.get("title", md_file.stem)
        evidence_level = front_matter.get("evidence_level", "")
        indication_count = front_matter.get("indication_count", "0")

        # Extract predicted indication for search queries
        predicted_indication = extract_predicted_indication(content)

        # 2026-10-16：監測改用 front matter 的英文 INN 與預測新適應症（不分語言）；
        # 沒有這兩個欄位的頁（轉址頁、無新預測頁）不監測
        try:
            predicted_indications = json.loads(front_matter.get("predicted_indications", "[]"))
        except ValueError:
            predicted_indications = []
        monitor_inn = front_matter.get("monitor_inn", "")
        if not predicted_indications or not monitor_inn:
            continue

        drugs.append({
            "name": drug_name,
            "file": md_file.name,
            "evidence_level": evidence_level,
            "indication_count": int(indication_count) if indication_count.isdigit() else 0,
            "predicted_indication": predicted_indication,
            "inn": monitor_inn,
            "predicted_indications": predicted_indications,
            "approved_indication": original_by_slug.get(page_slug(md_file, front_matter))
            or original_by_name.get(drug_name.lower(), ""),
        })

    # Save to JSON
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump({
            "total": len(drugs),
            "generated_at": __import__("datetime").datetime.now().isoformat(),
            "drugs": drugs
        }, f, indent=2, ensure_ascii=False)

    print(f"Extracted {len(drugs)} drugs to {output_file}")
    print(f"With approved_indication: {sum(1 for d in drugs if d['approved_indication'])}")

    # Print summary
    level_counts = {}
    for drug in drugs:
        level = drug["evidence_level"] or "Unknown"
        level_counts[level] = level_counts.get(level, 0) + 1

    print("\nEvidence level distribution:")
    for level in sorted(level_counts.keys()):
        print(f"  {level}: {level_counts[level]}")


if __name__ == "__main__":
    main()
