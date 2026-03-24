#!/usr/bin/env python3
"""Generate search index and drug stats for EuTxGNN website"""

import csv
import json
import re
from collections import defaultdict
from datetime import date
from pathlib import Path


def normalize_slug(name: str) -> str:
    """Convert drug name to URL slug"""
    if not name:
        return "unknown"
    slug = name.lower().strip()
    slug = re.sub(r'[^a-z0-9]+', '-', slug)
    return slug.strip('-') or "unknown"


def load_predictions():
    """Load prediction data"""
    predictions_file = Path("data/processed/repurposing_candidates.csv.gz")
    drugs = defaultdict(lambda: {
        'indications': [],
        'brands': set(),
        'drugbank_id': None
    })

    with open(predictions_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ingredient = row.get('ingredient', '').upper()
            if not ingredient:
                continue

            drugs[ingredient]['indications'].append({
                'name': row.get('potential_indication', ''),
                'score': round(float(row.get('score', 0)) * 100, 2),
                'level': 'L5'  # Currently all L5
            })
            if row.get('brand_name'):
                drugs[ingredient]['brands'].add(row.get('brand_name'))
            if row.get('drugbank_id'):
                drugs[ingredient]['drugbank_id'] = row.get('drugbank_id')

    return drugs


def load_drug_mapping():
    """Load drug mapping for original indications"""
    mapping = {}
    mapping_file = Path("data/processed/drug_mapping.csv")

    if mapping_file.exists():
        with open(mapping_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                ingredient = row.get('ingredient', '').upper()
                if ingredient and row.get('indication'):
                    # Truncate long indications
                    indication = row.get('indication', '')[:200]
                    if len(row.get('indication', '')) > 200:
                        indication += '...'
                    mapping[ingredient] = indication

    return mapping


def generate_search_index(drugs, drug_mapping):
    """Generate search index for drug lookup"""
    drug_list = []
    indication_index = defaultdict(lambda: {'drugs': [], 'level': 'L5'})

    for drug_name, data in sorted(drugs.items()):
        if not drug_name or len(data['indications']) == 0:
            continue

        # Sort indications by score
        sorted_inds = sorted(data['indications'], key=lambda x: x['score'], reverse=True)

        # Get best evidence level (currently all L5)
        level = 'L5'

        drug_entry = {
            'name': drug_name.title(),
            'slug': normalize_slug(drug_name),
            'brands': list(data['brands'] - {''}),
            'original': drug_mapping.get(drug_name, ''),
            'level': level,
            'indications': sorted_inds[:10]  # Top 10 indications
        }
        drug_list.append(drug_entry)

        # Build indication index
        for ind in sorted_inds[:20]:  # Top 20 indications per drug
            ind_name = ind['name']
            indication_index[ind_name]['drugs'].append({
                'name': drug_name.title(),
                'slug': normalize_slug(drug_name),
                'score': ind['score'],
                'level': level,
                'original': drug_mapping.get(drug_name, '')[:100]
            })

    # Convert indication index to list
    indication_list = []
    for ind_name, ind_data in indication_index.items():
        # Sort drugs by score
        sorted_drugs = sorted(ind_data['drugs'], key=lambda x: x['score'], reverse=True)
        indication_list.append({
            'name': ind_name,
            'level': 'L5',  # Currently all L5
            'drugs': sorted_drugs[:10]  # Top 10 drugs per indication
        })

    search_index = {
        'generated': str(date.today()),
        'drug_count': len(drug_list),
        'indication_count': len(indication_list),
        'drugs': drug_list,
        'indications': indication_list
    }

    return search_index


def generate_drug_stats(drugs, drug_mapping):
    """Generate drug stats for D3 charts"""
    all_drugs = []

    for drug_name, data in sorted(drugs.items()):
        if not drug_name or len(data['indications']) == 0:
            continue

        level = 'L5'  # Currently all L5
        indication_count = len(data['indications'])

        all_drugs.append({
            'name': drug_name.title(),
            'slug': normalize_slug(drug_name),
            'level': level,
            'indication_count': min(indication_count, 50)  # Cap at 50 for display
        })

    # Count by level
    level_counts = defaultdict(int)
    for drug in all_drugs:
        level_counts[drug['level']] += 1

    drug_stats = {
        'generated': str(date.today()),
        'total_drugs': len(all_drugs),
        'level_counts': dict(level_counts),
        'all_drugs': all_drugs
    }

    return drug_stats


def main():
    print("Loading data...")
    drugs = load_predictions()
    drug_mapping = load_drug_mapping()

    print(f"Found {len(drugs)} drugs")

    # Generate search index
    print("Generating search index...")
    search_index = generate_search_index(drugs, drug_mapping)

    search_index_path = Path("docs/data/search-index.json")
    search_index_path.parent.mkdir(parents=True, exist_ok=True)
    with open(search_index_path, 'w', encoding='utf-8') as f:
        json.dump(search_index, f, ensure_ascii=False, indent=2)
    print(f"Written {search_index_path}")

    # Generate drug stats
    print("Generating drug stats...")
    drug_stats = generate_drug_stats(drugs, drug_mapping)

    stats_path = Path("docs/_data/drug_stats.json")
    stats_path.parent.mkdir(parents=True, exist_ok=True)
    with open(stats_path, 'w', encoding='utf-8') as f:
        json.dump(drug_stats, f, ensure_ascii=False, indent=2)
    print(f"Written {stats_path}")

    print("\nSummary:")
    print(f"  Drugs: {search_index['drug_count']}")
    print(f"  Indications: {search_index['indication_count']}")
    print(f"  Level counts: {drug_stats['level_counts']}")


if __name__ == "__main__":
    main()
