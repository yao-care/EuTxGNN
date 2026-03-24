#!/usr/bin/env python3
"""Merge KG and DL prediction results

Combines Knowledge Graph and Deep Learning predictions into a unified
repurposing candidates file.

Usage:
    uv run python scripts/merge_predictions.py

Input:
    data/processed/repurposing_candidates.csv (KG predictions)
    data/processed/txgnn_checkpoint.csv (DL predictions)
    data/processed/eu_integrated_drugs.json (EU drug info)

Output:
    data/processed/repurposing_candidates_merged.csv
    data/processed/repurposing_report_merged.json
"""

import json
from pathlib import Path
from datetime import datetime

import pandas as pd


def load_eu_drugs(path: Path) -> dict:
    """Load EU drug info and create drugbank_id to drug info mapping."""
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    # Build mapping from ingredient name to drug info
    drug_map = {}

    for drug in data.get("ema_drugs", []):
        active = drug.get("active_substance") or ""
        if active:
            drug_map[active.upper()] = {
                "license_id": drug.get("license_id") or "",
                "brand_name": drug.get("brand_name") or "",
                "source": "EMA"
            }

    return drug_map


def load_drug_mapping(path: Path) -> dict:
    """Load drug mapping CSV to get drugbank_id for each ingredient."""
    df = pd.read_csv(path)
    mapping = {}
    for _, row in df.iterrows():
        ingredient = str(row.get("ingredient", "")).upper()
        drugbank_id = row.get("drugbank_id", "")
        if ingredient and drugbank_id and pd.notna(drugbank_id):
            mapping[drugbank_id] = ingredient
    return mapping


def main():
    print("=" * 60)
    print("Merging KG and DL Predictions")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    processed_dir = base_dir / "data" / "processed"

    # 1. Load existing KG predictions
    print("1. Loading KG predictions...")
    kg_path = processed_dir / "repurposing_candidates.csv.gz"
    kg_df = pd.read_csv(kg_path)
    print(f"   KG predictions: {len(kg_df)} rows")

    # 2. Load DL predictions
    print("2. Loading DL predictions...")
    dl_path = processed_dir / "txgnn_checkpoint.csv"
    dl_df = pd.read_csv(dl_path)
    print(f"   DL predictions: {len(dl_df)} rows")

    # 3. Load EU drug info
    print("3. Loading EU drug info...")
    eu_drugs_path = processed_dir / "eu_integrated_drugs.json"
    eu_drugs = load_eu_drugs(eu_drugs_path)
    print(f"   EU drugs with mapping: {len(eu_drugs)}")

    # 4. Load drug mapping (drugbank_id -> ingredient)
    print("4. Loading drug mapping...")
    drug_mapping_path = processed_dir / "drug_mapping.csv"
    drugbank_to_ingredient = load_drug_mapping(drug_mapping_path)
    print(f"   DrugBank mappings: {len(drugbank_to_ingredient)}")

    # 5. Process DL predictions
    print("5. Processing DL predictions...")
    dl_records = []
    matched_count = 0

    for _, row in dl_df.iterrows():
        drugbank_id = row.get("drugbank_id", "")
        drug_name = row.get("drug_name", "")
        disease_name = row.get("disease_name", "")
        score = row.get("txgnn_score", 0.0)

        # Try to find EU drug info
        ingredient = drug_name.upper()

        # Also try from drugbank mapping
        if drugbank_id in drugbank_to_ingredient:
            ingredient = drugbank_to_ingredient[drugbank_id]

        if ingredient in eu_drugs:
            drug_info = eu_drugs[ingredient]
            dl_records.append({
                "license_id": drug_info["license_id"],
                "brand_name": drug_info["brand_name"],
                "ingredient": ingredient,
                "drugbank_id": drugbank_id,
                "potential_indication": disease_name,
                "source": "TxGNN Deep Learning",
                "score": score
            })
            matched_count += 1
        else:
            # Still include but without EMA license info
            dl_records.append({
                "license_id": "",
                "brand_name": drug_name,
                "ingredient": drug_name.upper(),
                "drugbank_id": drugbank_id,
                "potential_indication": disease_name,
                "source": "TxGNN Deep Learning",
                "score": score
            })

    print(f"   Matched to EU drugs: {matched_count}")
    dl_processed = pd.DataFrame(dl_records)

    # 6. Add score column to KG predictions
    print("6. Standardizing columns...")
    kg_df["score"] = 0.5  # Default score for KG predictions

    # Ensure same columns
    columns = ["license_id", "brand_name", "ingredient", "drugbank_id",
               "potential_indication", "source", "score"]

    kg_df = kg_df.reindex(columns=columns, fill_value="")
    dl_processed = dl_processed.reindex(columns=columns, fill_value="")

    # 7. Merge and deduplicate
    print("7. Merging predictions...")
    merged_df = pd.concat([kg_df, dl_processed], ignore_index=True)

    # Remove duplicates (same drug + indication), keeping highest score
    merged_df = merged_df.sort_values("score", ascending=False)
    merged_df = merged_df.drop_duplicates(
        subset=["drugbank_id", "potential_indication"],
        keep="first"
    )

    # Sort by score descending
    merged_df = merged_df.sort_values("score", ascending=False)

    print(f"   Merged total: {len(merged_df)} rows")

    # 8. Save merged results
    print("8. Saving results...")

    # Save merged CSV
    output_path = processed_dir / "repurposing_candidates_merged.csv"
    merged_df.to_csv(output_path, index=False)
    print(f"   Saved: {output_path}")

    # Also update the main file
    main_output = processed_dir / "repurposing_candidates.csv.gz"
    merged_df.to_csv(main_output, index=False)
    print(f"   Updated: {main_output}")

    # 9. Generate report
    print("9. Generating report...")
    report = {
        "generated_at": datetime.now().isoformat(),
        "kg_predictions": len(kg_df),
        "dl_predictions": len(dl_df),
        "dl_matched_to_eu": matched_count,
        "merged_total": len(merged_df),
        "unique_drugs": merged_df["drugbank_id"].nunique(),
        "unique_indications": merged_df["potential_indication"].nunique(),
        "source_breakdown": merged_df["source"].value_counts().to_dict(),
        "top_scores": merged_df.head(10)[["ingredient", "potential_indication", "score", "source"]].to_dict("records")
    }

    report_path = processed_dir / "repurposing_report_merged.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"   Saved: {report_path}")

    # Summary
    print()
    print("=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"  KG predictions:      {len(kg_df):,}")
    print(f"  DL predictions:      {len(dl_df):,}")
    print(f"  Merged (deduplicated): {len(merged_df):,}")
    print(f"  Unique drugs:        {merged_df['drugbank_id'].nunique():,}")
    print(f"  Unique indications:  {merged_df['potential_indication'].nunique():,}")
    print()
    print("  Source breakdown:")
    for source, count in merged_df["source"].value_counts().items():
        print(f"    - {source}: {count:,}")
    print()
    print("  Top 5 predictions by score:")
    for i, row in merged_df.head(5).iterrows():
        print(f"    {row['ingredient'][:20]:20s} → {row['potential_indication'][:30]:30s} ({row['score']:.3f})")
    print()
    print("Done!")


if __name__ == "__main__":
    main()
