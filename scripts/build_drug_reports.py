#!/usr/bin/env python3
"""Generate drug report pages for EuTxGNN Jekyll site"""

import csv
import re
import shutil
from collections import defaultdict
from pathlib import Path


def normalize_drug_name(name: str) -> str:
    """Normalize drug name for URL/filename"""
    if not name:
        return "unknown"
    # Convert to lowercase, replace spaces with hyphens
    normalized = name.lower().strip()
    normalized = re.sub(r'[^a-z0-9]+', '-', normalized)
    normalized = normalized.strip('-')
    return normalized or "unknown"


def get_evidence_level(predictions: list) -> str:
    """Determine evidence level based on predictions (currently all L5)"""
    # For now, all predictions are L5 (AI only)
    # Future: integrate clinical trial data to upgrade levels
    return "L5"


def get_parent_by_evidence_level(evidence_level: str) -> str:
    """Get parent page based on evidence level"""
    if evidence_level in ('L1', 'L2'):
        return 'High Evidence (L1-L2)'
    elif evidence_level in ('L3', 'L4'):
        return 'Medium Evidence (L3-L4)'
    else:
        return 'AI Predictions (L5)'


def load_drug_mapping():
    """Load drug mapping data"""
    mapping = {}
    mapping_file = Path("data/processed/drug_mapping.csv")

    if mapping_file.exists():
        with open(mapping_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                ingredient = row.get('ingredient', '').upper()
                if ingredient:
                    mapping[ingredient] = {
                        'license_id': row.get('license_id', ''),
                        'brand_name': row.get('brand_name', ''),
                        'drugbank_id': row.get('drugbank_id', ''),
                        'indication': row.get('indication', '')
                    }
    return mapping


def load_predictions():
    """Load and group predictions by drug"""
    predictions_file = Path("data/processed/repurposing_candidates.csv")
    drugs = defaultdict(lambda: {
        'predictions': [],
        'license_ids': set(),
        'brand_names': set(),
        'drugbank_id': None
    })

    with open(predictions_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ingredient = row.get('ingredient', '').upper()
            if not ingredient:
                continue

            drugs[ingredient]['predictions'].append({
                'indication': row.get('potential_indication', ''),
                'source': row.get('source', ''),
                'score': float(row.get('score', 0))
            })
            drugs[ingredient]['license_ids'].add(row.get('license_id', ''))
            drugs[ingredient]['brand_names'].add(row.get('brand_name', ''))
            if row.get('drugbank_id'):
                drugs[ingredient]['drugbank_id'] = row.get('drugbank_id')

    return drugs


def generate_drug_page(drug_name: str, drug_data: dict, drug_info: dict, nav_order: int) -> str:
    """Generate Jekyll page content for a drug"""

    predictions = sorted(drug_data['predictions'], key=lambda x: x['score'], reverse=True)
    evidence_level = get_evidence_level(predictions)
    parent = get_parent_by_evidence_level(evidence_level)

    # Get drug info
    brand_names = ', '.join(sorted(drug_data['brand_names'] - {''}))
    drugbank_id = drug_data['drugbank_id'] or 'N/A'
    original_indication = drug_info.get('indication', 'See EMA product information')[:500]
    if len(drug_info.get('indication', '')) > 500:
        original_indication += '...'

    # Title formatting
    title = drug_name.title()

    content = f"""---
layout: default
title: {title}
description: "{title} drug repurposing predictions from TxGNN. Evidence level {evidence_level} with {len(predictions)} predicted indications."
parent: {parent}
nav_order: {nav_order}
evidence_level: {evidence_level}
indication_count: {len(predictions)}
---

# {title}
{{: .fs-9 }}

Evidence Level: **{evidence_level}** | Predicted Indications: **{len(predictions)}**
{{: .fs-6 .fw-300 }}

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | {title} |
| DrugBank ID | [{drugbank_id}](https://go.drugbank.com/drugs/{drugbank_id}) |
| Brand Names (EU) | {brand_names or 'N/A'} |
| Evidence Level | {evidence_level} |
| Predicted Indications | {len(predictions)} |
| Top Prediction Score | {predictions[0]['score']:.2%} |

---

## Approved Indication (EMA)

{original_indication}

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
"""

    # Add top 20 predictions
    for i, pred in enumerate(predictions[:20], 1):
        source_short = "KG" if "Knowledge" in pred['source'] else "DL"
        content += f"| {i} | {pred['indication']} | {pred['score']:.2%} | {source_short} |\n"

    if len(predictions) > 20:
        content += f"\n*Showing top 20 of {len(predictions)} predictions.*\n"

    content += """
---

## About TxGNN Predictions

### Prediction Sources

| Source | Description |
|--------|-------------|
| **KG** | Knowledge Graph - Network topology-based associations |
| **DL** | Deep Learning - Neural network score prediction |

### Evidence Levels

| Level | Definition |
|:-----:|------------|
| L1 | Multiple Phase 3 RCTs / Systematic Reviews |
| L2 | Single RCT or multiple Phase 2 trials |
| L3 | Observational studies / Large case series |
| L4 | Preclinical / Mechanistic / Case reports |
| **L5** | AI prediction only (current) |

---

## Clinical Validation Needed

<div style="background: #fff3cd; padding: 1rem; border-left: 4px solid #ffc107; border-radius: 4px; margin: 1rem 0;">
<strong>Research Use Only:</strong> These predictions are computational hypotheses that require clinical validation. They should NOT be used for clinical decision-making.
</div>

### Next Steps for Validation

1. **Literature Review**: Search PubMed for existing evidence
2. **Clinical Trial Search**: Check ClinicalTrials.gov for ongoing studies
3. **Mechanistic Analysis**: Evaluate biological plausibility
4. **Preclinical Studies**: Conduct in vitro/in vivo validation
5. **Clinical Trials**: Design and conduct human studies

---

## Data Access

- **FHIR API**: `/fhir/ClinicalUseDefinition/`
- **CSV Download**: [All Predictions](/downloads/)
- **GitHub**: [yao-care/EuTxGNN](https://github.com/yao-care/EuTxGNN)

---

## Citation

If using this data, please cite:

```bibtex
@article{huang2023txgnn,
  title={A foundation model for clinician-centered drug repurposing},
  author={Huang, Kexin and others},
  journal={Nature Medicine},
  year={2023},
  doi={10.1038/s41591-023-02233-x}
}
```

---

<div style="background: #f8f9fa; padding: 1rem; border-radius: 4px; font-size: 0.9rem;">
<strong>Disclaimer:</strong> This report is for research purposes only and does not constitute medical advice. Drug repurposing predictions require rigorous clinical validation before any therapeutic application.
</div>
"""

    return content


def generate_drug_list_page(drug_list: list) -> str:
    """Generate the main drug list page"""

    # Group by evidence level
    by_level = defaultdict(list)
    for drug in drug_list:
        by_level[drug['evidence_level']].append(drug)

    content = f"""---
layout: default
title: Drug List
parent: Drug Reports
nav_order: 4
description: "Complete list of {len(drug_list)} EMA drugs with TxGNN repurposing predictions"
permalink: /drugs/
---

# Drug List
{{: .fs-9 }}

{len(drug_list)} EMA drugs with repurposing predictions
{{: .fs-6 .fw-300 }}

---

## Statistics

| Evidence Level | Drugs | Description |
|:--------------:|------:|-------------|
"""

    level_desc = {
        'L1': 'Multiple RCTs / Systematic reviews',
        'L2': 'Single RCT / Phase 2 trials',
        'L3': 'Observational studies / Case series',
        'L4': 'Preclinical / Mechanistic',
        'L5': 'AI prediction only'
    }

    for level in ['L1', 'L2', 'L3', 'L4', 'L5']:
        drugs = by_level.get(level, [])
        desc = level_desc.get(level, '')
        content += f"| **{level}** | {len(drugs)} | {desc} |\n"

    content += f"""
---

## Complete Drug List

| Drug | Evidence | Indications | Report |
|------|:--------:|:-----------:|--------|
"""

    # Sort by drug name
    for drug in sorted(drug_list, key=lambda x: x['name']):
        url_name = normalize_drug_name(drug['name'])
        content += f"| {drug['title']} | {drug['evidence_level']} | {drug['indication_count']} | [View](/drugs/{url_name}/) |\n"

    content += """
---

## Data Downloads

- [CSV: All Predictions](https://github.com/yao-care/EuTxGNN/raw/main/data/processed/repurposing_candidates.csv)
- [CSV: Drug Mapping](https://github.com/yao-care/EuTxGNN/raw/main/data/processed/drug_mapping.csv)

---

<div style="background: #fff3cd; padding: 1rem; border-left: 4px solid #ffc107; border-radius: 4px;">
<strong>Disclaimer:</strong> These predictions are for research purposes only and require clinical validation before any therapeutic application.
</div>
"""

    return content


def main():
    """Main function to generate all drug reports"""
    print("Loading data...")

    # Load data
    drug_mapping = load_drug_mapping()
    drugs = load_predictions()

    print(f"Found {len(drugs)} unique drugs with predictions")

    # Create output directory
    output_dir = Path("docs/_drugs")
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    drug_list = []
    nav_order = 10

    for drug_name, drug_data in sorted(drugs.items()):
        if not drug_name or len(drug_data['predictions']) == 0:
            continue

        # Get drug info from mapping
        drug_info = drug_mapping.get(drug_name, {})

        # Generate page content
        content = generate_drug_page(drug_name, drug_data, drug_info, nav_order)

        # Write file
        filename = normalize_drug_name(drug_name)
        output_file = output_dir / f"{filename}.md"
        output_file.write_text(content, encoding='utf-8')

        evidence_level = get_evidence_level(drug_data['predictions'])

        drug_list.append({
            'name': drug_name,
            'title': drug_name.title(),
            'evidence_level': evidence_level,
            'indication_count': len(drug_data['predictions'])
        })

        nav_order += 1

    print(f"Generated {len(drug_list)} drug report pages")

    # Generate drug list page
    drug_list_content = generate_drug_list_page(drug_list)
    Path("docs/drugs.md").write_text(drug_list_content, encoding='utf-8')
    print("Updated drugs.md")

    # Print summary
    print("\nSummary:")
    print(f"  Total drugs: {len(drug_list)}")

    by_level = defaultdict(int)
    for drug in drug_list:
        by_level[drug['evidence_level']] += 1

    for level in sorted(by_level.keys()):
        print(f"  {level}: {by_level[level]} drugs")


if __name__ == "__main__":
    main()
