#!/usr/bin/env python3
"""
Generate news monitoring keywords for EuTxGNN

Extracts from existing data:
- 642 drug names (generic + brand names)
- Disease keywords with related_drugs mapping
- Multi-language synonyms (EN, DE, FR, ES, IT)

Output: data/news/keywords.json
"""

import json
import re
from datetime import datetime
from pathlib import Path

# Project root
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
DOCS_DATA_DIR = PROJECT_ROOT / "docs" / "data"


def load_json(path: Path) -> dict | list:
    """Load JSON file"""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def slugify(text: str) -> str:
    """Convert text to URL-safe slug"""
    slug = re.sub(r"[^\w\s-]", "", text.lower())
    slug = re.sub(r"[\s_]+", "-", slug)
    return slug.strip("-")


# Generic keyword patterns for disease categories
GENERIC_KEYWORD_PATTERNS = {
    "cancer": [
        "cancer", "carcinoma", "tumor", "tumour", "neoplasm", "malignant",
        "leukemia", "lymphoma", "melanoma", "sarcoma", "myeloma", "oncology"
    ],
    "heart disease": [
        "heart disease", "heart failure", "cardiac", "myocardial",
        "arrhythmia", "angina", "cardiomyopathy", "cardiovascular"
    ],
    "diabetes mellitus": [
        "diabetes", "diabetic", "hyperglycemia", "insulin resistance"
    ],
    "hypertension": [
        "hypertension", "high blood pressure", "elevated blood pressure"
    ],
    "stroke": [
        "stroke", "cerebrovascular", "ischemic stroke", "hemorrhagic stroke"
    ],
    "alzheimer disease": [
        "alzheimer", "dementia", "cognitive impairment", "neurodegeneration"
    ],
    "depression": [
        "depression", "depressive", "major depression", "mood disorder"
    ],
    "arthritis": [
        "arthritis", "rheumatoid", "osteoarthritis", "joint inflammation"
    ],
    "asthma": [
        "asthma", "bronchial", "respiratory", "wheezing"
    ],
    "multiple sclerosis": [
        "multiple sclerosis", "MS", "demyelinating"
    ],
}


def build_indication_index(search_index: dict, synonyms: dict) -> dict:
    """Build indication index mapping each indication to related drugs"""
    indication_map = {}
    indication_synonyms = synonyms.get("indication_synonyms", {})

    # First, add all synonym entries
    for disease_name, synonym_list in indication_synonyms.items():
        key = disease_name.lower()
        if key not in indication_map:
            indication_map[key] = {
                "name": disease_name,
                "keywords": [disease_name] + synonym_list,
                "related_drugs": []
            }

    # Process drugs and their predicted indications
    for drug in search_index.get("drugs", []):
        drug_slug = drug.get("slug", "")

        for ind in drug.get("indications", []):
            ind_name = ind.get("name", "")
            ind_key = ind_name.lower()

            if not ind_name:
                continue

            # Check if this indication matches any of our tracked diseases
            matched_disease = None
            for disease_name, synonym_list in indication_synonyms.items():
                disease_key = disease_name.lower()
                all_keywords = [disease_name.lower()] + [s.lower() for s in synonym_list]

                # Check if indication matches any keyword
                for kw in all_keywords:
                    if kw in ind_key or ind_key in kw:
                        matched_disease = disease_key
                        break
                if matched_disease:
                    break

            # Also check generic patterns
            if not matched_disease:
                for disease_name, patterns in GENERIC_KEYWORD_PATTERNS.items():
                    for pattern in patterns:
                        if pattern.lower() in ind_key:
                            matched_disease = disease_name.lower()
                            break
                    if matched_disease:
                        break

            if matched_disease and matched_disease in indication_map:
                if drug_slug not in indication_map[matched_disease]["related_drugs"]:
                    indication_map[matched_disease]["related_drugs"].append(drug_slug)

    return indication_map


def main():
    print("Loading data files...")

    # Load data
    search_index = load_json(DOCS_DATA_DIR / "search-index.json")
    synonyms = load_json(DATA_DIR / "news" / "synonyms.json")

    print(f"  - search-index.json: {search_index.get('drug_count', 0)} drugs")
    print(f"  - synonyms.json: {len(synonyms.get('indication_synonyms', {}))} disease categories")
    print(f"  - synonyms.json: {len(synonyms.get('drug_synonyms', {}))} drug synonyms")

    # Build drug keywords list
    drugs_keywords = []
    drug_synonyms = synonyms.get("drug_synonyms", {})

    for drug in search_index.get("drugs", []):
        drug_name = drug.get("name", "")
        drug_slug = drug.get("slug", "")

        # Build keywords list
        keywords = [drug_name.lower()]

        # Add brand names from search-index
        for brand in drug.get("brands", []):
            if brand.lower() not in keywords:
                keywords.append(brand.lower())

        # Add synonyms from synonyms.json
        drug_key = drug_name.lower()
        if drug_key in drug_synonyms:
            for syn in drug_synonyms[drug_key]:
                if syn.lower() not in keywords:
                    keywords.append(syn.lower())

        drugs_keywords.append({
            "slug": drug_slug,
            "name": drug_name,
            "keywords": keywords,
            "url": f"/drugs/{drug_slug}/"
        })

    print(f"\nProcessed drug keywords: {len(drugs_keywords)} drugs")

    # Build indication keywords with related_drugs
    indication_map = build_indication_index(search_index, synonyms)

    # Convert to list format (only keep indications with related drugs)
    indications_keywords = []
    for key, data in indication_map.items():
        if data["related_drugs"]:  # Only include if has related drugs
            indications_keywords.append({
                "name": data["name"],
                "keywords": data["keywords"],
                "related_drugs": data["related_drugs"]
            })

    print(f"Processed indication keywords: {len(indications_keywords)} indications with related drugs")

    # Show stats
    total_relations = sum(len(ind["related_drugs"]) for ind in indications_keywords)
    print(f"Total drug-disease relations: {total_relations}")

    # Output
    output = {
        "generated": datetime.now().strftime("%Y-%m-%d"),
        "drug_count": len(drugs_keywords),
        "indication_count": len(indications_keywords),
        "drugs": drugs_keywords,
        "indications": indications_keywords
    }

    output_path = DATA_DIR / "news" / "keywords.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\nOutput: {output_path}")
    print(f"  - Drug keywords: {len(drugs_keywords)}")
    print(f"  - Indication keywords: {len(indications_keywords)}")

    # Show sample
    print("\n=== Sample indications with related drugs ===")
    for ind in indications_keywords[:5]:
        print(f"  {ind['name']}: {len(ind['related_drugs'])} drugs")
        print(f"    Keywords: {ind['keywords'][:3]}...")
        print(f"    Drugs: {ind['related_drugs'][:3]}...")


if __name__ == "__main__":
    main()
