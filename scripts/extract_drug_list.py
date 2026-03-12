#!/usr/bin/env python3
"""
Extract drug list from docs/_drugs/*.md files.
Creates a JSON file with drug names, evidence levels, indication counts,
and approved indications for filtering in evidence monitoring.
"""

import csv
import json
import re
from datetime import datetime
from pathlib import Path


def load_approved_indications(csv_path: Path) -> dict:
    """Load approved indications from drug mapping file.

    Returns:
        dict mapping ingredient (uppercase) to approved indication text
    """
    approved = {}
    if csv_path.exists():
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                ingredient = row.get("ingredient", "").upper()
                indication = row.get("indication", "")
                if ingredient and indication:
                    approved[ingredient] = indication
    return approved


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
    """Extract top predicted indication from the drug report."""
    # Look for the first indication in the predictions table
    # Format: | 1 | indication name | 99.99% | DL |
    match = re.search(r'\|\s*1\s*\|\s*([^|]+)\s*\|\s*[\d.]+%', content)
    if match:
        return match.group(1).strip()
    return ""


def main():
    base_dir = Path(__file__).parent.parent
    drugs_dir = base_dir / "docs" / "_drugs"
    mapping_file = base_dir / "data" / "processed" / "drug_mapping.csv"
    output_file = Path(__file__).parent / "drug_list.json"

    # Load approved indications for filtering
    approved_indications = load_approved_indications(mapping_file)
    print(f"Loaded approved indications for {len(approved_indications)} drugs")

    drugs = []

    for md_file in sorted(drugs_dir.glob("*.md")):
        content = md_file.read_text(encoding="utf-8")
        front_matter = parse_front_matter(content)

        drug_name = front_matter.get("title", md_file.stem)
        evidence_level = front_matter.get("evidence_level", "")
        indication_count = front_matter.get("indication_count", "0")

        # Extract predicted indication for search queries
        predicted_indication = extract_predicted_indication(content)

        # Get approved indication for filtering
        approved_indication = approved_indications.get(drug_name.upper(), "")

        drugs.append({
            "name": drug_name,
            "file": md_file.name,
            "evidence_level": evidence_level,
            "indication_count": int(indication_count) if indication_count.isdigit() else 0,
            "predicted_indication": predicted_indication,
            "approved_indication": approved_indication
        })

    # Save to JSON
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump({
            "total": len(drugs),
            "generated_at": datetime.now().isoformat(),
            "drugs": drugs
        }, f, indent=2, ensure_ascii=False)

    print(f"Extracted {len(drugs)} drugs to {output_file}")

    # Print summary
    level_counts = {}
    approved_count = 0
    for drug in drugs:
        level = drug["evidence_level"] or "Unknown"
        level_counts[level] = level_counts.get(level, 0) + 1
        if drug["approved_indication"]:
            approved_count += 1

    print("\nEvidence level distribution:")
    for level in sorted(level_counts.keys()):
        print(f"  {level}: {level_counts[level]}")
    print(f"\nDrugs with approved indications: {approved_count}")


if __name__ == "__main__":
    main()
