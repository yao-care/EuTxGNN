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


def _prune_search_index():
    """把 docs/_drugs 裡不存在、或自己標了 search_exclude 的頁面，從搜尋索引移除。

    索引是由 data/processed 的預測檔生成的，跟頁面是否存在無關，所以會出現
    指向不存在頁面的 entry（死連結），以及薄內容頁佔據搜尋結果。這裡在寫檔後
    以頁面為準做一次收斂。
    """
    import json as _json
    import re as _re
    from pathlib import Path as _Path

    idx_path = _Path("docs/data/search-index.json")
    drugs_dir = _Path("docs/_drugs")
    if not idx_path.exists() or not drugs_dir.is_dir():
        return

    try:
        idx = _json.loads(idx_path.read_text(encoding="utf-8"))
    except Exception:
        return
    if not isinstance(idx, dict) or not isinstance(idx.get("drugs"), list):
        return

    _cache = {}

    def _visible(slug):
        if not slug:
            return False
        if slug in _cache:
            return _cache[slug]
        page = drugs_dir / f"{slug}.md"
        ok = page.exists()
        if ok:
            head = page.read_text(encoding="utf-8", errors="replace")[:2000]
            if _re.search(r"^search_exclude:\s*true", head, _re.M | _re.I):
                ok = False
        _cache[slug] = ok
        return ok

    before = len(idx["drugs"])
    idx["drugs"] = [d for d in idx["drugs"] if _visible(d.get("slug"))]

    inds = idx.get("indications")
    if isinstance(inds, list):
        kept = []
        for ind in inds:
            refs = ind.get("drugs")
            if isinstance(refs, list):
                refs = [r for r in refs if _visible(r.get("slug"))]
                if not refs:
                    continue
                ind["drugs"] = refs
                ind["drug_count"] = len(refs)
            kept.append(ind)
        idx["indications"] = kept
        idx["indication_count"] = len(kept)

    idx["drug_count"] = len(idx["drugs"])
    idx_path.write_text(_json.dumps(idx, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  Pruned search index: {before} -> {len(idx['drugs'])} drugs")


_main_before_prune = main


def main():
    _main_before_prune()
    _prune_search_index()


if __name__ == "__main__":
    main()
