#!/usr/bin/env python3
"""Batch evidence collection for drug-indication pairs.

Collects evidence from ClinicalTrials.gov and PubMed for all drug-indication
pairs in the repurposing candidates file, evaluates evidence levels, and
stores results for website generation.

NOTE: This script filters out known/approved indications to focus on
true drug repurposing candidates.
"""

import csv
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from eutxgnn.collectors import ClinicalTrialsCollector, PubMedCollector


def load_approved_indications(csv_path: str) -> dict[str, str]:
    """Load approved indications from drug mapping file.

    Returns:
        dict mapping ingredient (uppercase) to approved indication text
    """
    approved = {}
    if os.path.exists(csv_path):
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                ingredient = row.get("ingredient", "").upper()
                indication = row.get("indication", "")
                if ingredient and indication:
                    approved[ingredient] = indication.lower()
    return approved


def is_known_indication(approved_indication: str, predicted_indication: str) -> bool:
    """Check if predicted indication overlaps with approved indication.

    Uses keyword matching to detect if the predicted indication is likely
    already approved for the drug.

    Args:
        approved_indication: EMA approved indication text (lowercase)
        predicted_indication: TxGNN predicted indication name

    Returns:
        True if predicted indication appears to be already approved
    """
    if not approved_indication or not predicted_indication:
        return False

    predicted_lower = predicted_indication.lower()

    # Extract meaningful keywords from predicted indication
    # Remove common suffixes and split
    cleaned = re.sub(r'\s*\(disease\)\s*', ' ', predicted_lower)
    cleaned = re.sub(r'\s*\(disorder\)\s*', ' ', cleaned)
    cleaned = re.sub(r'[^\w\s]', ' ', cleaned)

    words = cleaned.split()

    # Generic medical terms that are too broad for matching
    generic_terms = {
        'disease', 'disorder', 'syndrome', 'type', 'of', 'the', 'and', 'or',
        'with', 'due', 'to', 'in', 'by', 'for', 'as', 'is', 'a', 'an',
        'primary', 'secondary', 'chronic', 'acute', 'severe', 'mild',
        'familial', 'hereditary', 'congenital', 'acquired', 'idiopathic',
        # Too generic - would cause false matches
        'cancer', 'tumor', 'carcinoma', 'neoplasm', 'infection', 'infectious',
        'deficiency', 'failure', 'insufficiency', 'inflammation',
        # Body parts/systems - too generic
        'cell', 'cells', 'blood', 'bone', 'muscle', 'nerve', 'skin',
    }

    # Keep important acronyms even if short
    important_acronyms = {
        'hiv', 'aids', 'copd', 'adhd', 'als', 'ms', 'ibd', 'ibs',
        'hcv', 'hbv', 'tb', 'ra', 'sle', 'ckd', 'chf', 'cad',
    }

    # Also check for expanded forms
    expanded_terms = {
        'hiv': 'immunodeficiency virus',
        'aids': 'acquired immunodeficiency',
        'copd': 'chronic obstructive pulmonary',
        'adhd': 'attention deficit',
        'als': 'amyotrophic lateral sclerosis',
    }

    keywords = []
    acronyms_found = []
    for w in words:
        w_lower = w.lower()
        if w_lower in important_acronyms:
            keywords.append(w_lower)
            acronyms_found.append(w_lower)
        elif w_lower not in generic_terms and len(w) > 4:
            keywords.append(w_lower)

    if not keywords:
        return False

    # Check if specific keywords appear in approved indication
    # Require exact word boundary matching for better precision
    matches = 0
    for kw in keywords:
        # Use word boundary matching
        pattern = r'\b' + re.escape(kw) + r'\b'
        if re.search(pattern, approved_indication):
            matches += 1
        # Also check expanded forms for acronyms
        elif kw in expanded_terms:
            if expanded_terms[kw] in approved_indication:
                matches += 1

    # Need majority of specific keywords to match
    # Or a very specific long keyword (>8 chars) to match
    if len(keywords) >= 2 and matches >= len(keywords) * 0.6:
        return True

    # Single very specific keyword match (including acronyms with expanded form)
    for kw in keywords:
        if len(kw) > 8:
            pattern = r'\b' + re.escape(kw) + r'\b'
            if re.search(pattern, approved_indication):
                return True
        # Acronyms with expanded form are also specific
        elif kw in expanded_terms and expanded_terms[kw] in approved_indication:
            return True

    return False


def load_candidates(csv_path: str) -> list[dict]:
    """Load drug-indication pairs from CSV."""
    candidates = []
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            candidates.append({
                "license_id": row["license_id"],
                "brand_name": row["brand_name"],
                "ingredient": row["ingredient"],
                "drugbank_id": row["drugbank_id"],
                "indication": row["potential_indication"],
                "source": row["source"],
                "score": float(row["score"]),
            })
    return candidates


def load_progress(progress_file: str) -> set:
    """Load already processed drug-indication pairs."""
    if os.path.exists(progress_file):
        with open(progress_file, "r") as f:
            return set(json.load(f))
    return set()


def save_progress(progress_file: str, processed: set):
    """Save processed drug-indication pairs."""
    with open(progress_file, "w") as f:
        json.dump(list(processed), f)


def get_unique_pairs(candidates: list[dict]) -> list[tuple[str, str, str]]:
    """Extract unique (drugbank_id, ingredient, indication) pairs."""
    seen = set()
    pairs = []
    for c in candidates:
        key = (c["drugbank_id"], c["ingredient"], c["indication"])
        if key not in seen:
            seen.add(key)
            pairs.append(key)
    return pairs


def evaluate_combined_evidence(
    ct_evidence: str,
    pubmed_evidence: str,
    ct_trials: list[dict],
    pubmed_articles: list[dict]
) -> dict:
    """
    Combine evidence from ClinicalTrials.gov and PubMed.

    Returns:
        dict with evidence_level, summary, and details
    """
    # Map evidence strings to numeric scores
    level_scores = {"L1": 1, "L2": 2, "L3": 3, "L4": 4, "L5": 5}

    ct_score = level_scores.get(ct_evidence, 5)
    pm_score = level_scores.get(pubmed_evidence, 5)

    # Take the best (lowest) evidence level
    best_score = min(ct_score, pm_score)

    # Build summary
    summary_parts = []

    # Count trial phases
    phase3_count = sum(1 for t in ct_trials if "phase 3" in t.get("phase", "").lower() or "phase3" in t.get("phase", "").lower())
    phase2_count = sum(1 for t in ct_trials if "phase 2" in t.get("phase", "").lower() or "phase2" in t.get("phase", "").lower())

    if phase3_count > 0:
        summary_parts.append(f"{phase3_count} Phase 3 trial(s)")
    if phase2_count > 0:
        summary_parts.append(f"{phase2_count} Phase 2 trial(s)")

    # Count publication types
    rct_count = 0
    review_count = 0
    for article in pubmed_articles:
        pub_types = article.get("publication_types", [])
        for pt in pub_types:
            pt_lower = pt.lower()
            if "randomized" in pt_lower or "controlled" in pt_lower:
                rct_count += 1
                break
            if "systematic review" in pt_lower or "meta-analysis" in pt_lower:
                review_count += 1
                break

    if rct_count > 0:
        summary_parts.append(f"{rct_count} RCT(s)")
    if review_count > 0:
        summary_parts.append(f"{review_count} review(s)/meta-analysis")

    final_level = f"L{best_score}"
    summary = ", ".join(summary_parts) if summary_parts else "AI prediction only"

    return {
        "evidence_level": final_level,
        "ct_evidence": ct_evidence,
        "pubmed_evidence": pubmed_evidence,
        "summary": summary,
        "ct_trial_count": len(ct_trials),
        "pubmed_article_count": len(pubmed_articles),
        "phase3_count": phase3_count,
        "phase2_count": phase2_count,
        "rct_count": rct_count,
        "review_count": review_count,
    }


def collect_evidence_for_pair(
    drug: str,
    indication: str,
    ct_collector: ClinicalTrialsCollector,
    pm_collector: PubMedCollector,
) -> dict:
    """Collect evidence for a single drug-indication pair."""

    # Query ClinicalTrials.gov
    ct_result = ct_collector.search(drug, indication)
    ct_trials = ct_result.data if ct_result.success else []
    ct_evidence = ct_collector.evaluate_evidence_level(ct_trials)

    # Query PubMed
    pm_result = pm_collector.search(drug, indication)
    pm_articles = pm_result.data if pm_result.success else []
    pm_evidence = pm_collector.evaluate_evidence_level(pm_articles)

    # Combine evidence
    combined = evaluate_combined_evidence(
        ct_evidence, pm_evidence, ct_trials, pm_articles
    )

    return {
        "drug": drug,
        "indication": indication,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        **combined,
        "clinicaltrials": {
            "success": ct_result.success,
            "error": ct_result.error_message,
            "trials": ct_trials[:5],  # Keep top 5 for reference
        },
        "pubmed": {
            "success": pm_result.success,
            "error": pm_result.error_message,
            "articles": pm_articles[:5],  # Keep top 5 for reference
        },
    }


def main():
    """Run batch evidence collection."""
    base_dir = Path(__file__).parent.parent

    # Paths
    candidates_csv = base_dir / "data/processed/repurposing_candidates_merged.csv"
    drug_mapping_csv = base_dir / "data/processed/drug_mapping.csv"
    output_dir = base_dir / "data/evidence"
    output_dir.mkdir(parents=True, exist_ok=True)

    results_file = output_dir / "evidence_results.json"
    progress_file = output_dir / "progress.json"
    summary_file = output_dir / "evidence_summary.json"
    skipped_file = output_dir / "skipped_known_indications.json"

    # Load approved indications for filtering
    print(f"Loading approved indications from {drug_mapping_csv}...")
    approved_indications = load_approved_indications(drug_mapping_csv)
    print(f"Loaded approved indications for {len(approved_indications)} drugs")

    # Load candidates
    print(f"Loading candidates from {candidates_csv}...")
    candidates = load_candidates(candidates_csv)
    print(f"Loaded {len(candidates)} total candidate records")

    # Get unique pairs
    pairs = get_unique_pairs(candidates)
    print(f"Found {len(pairs)} unique drug-indication pairs")

    # Load existing progress
    processed = load_progress(progress_file)
    print(f"Already processed: {len(processed)} pairs")

    # Load existing results
    if results_file.exists():
        with open(results_file, "r") as f:
            results = json.load(f)
    else:
        results = {}

    # Load skipped indications
    if skipped_file.exists():
        with open(skipped_file, "r") as f:
            skipped_known = set(json.load(f))
    else:
        skipped_known = set()

    # Initialize collectors
    ct_collector = ClinicalTrialsCollector(max_results=20)
    pm_collector = PubMedCollector(max_results=20)

    # Process pairs
    total = len(pairs)
    skipped_progress = 0
    skipped_known_count = 0
    errors = 0
    new_results = 0

    # Limit for this run (to avoid rate limiting)
    max_per_run = int(os.environ.get("MAX_PAIRS", "100"))

    print(f"\nProcessing up to {max_per_run} pairs this run...")
    print("(Filtering out known/approved indications)")
    print("-" * 60)

    for i, (drugbank_id, ingredient, indication) in enumerate(pairs):
        key = f"{drugbank_id}:{indication}"

        if key in processed:
            skipped_progress += 1
            continue

        if key in skipped_known:
            continue

        # Check if this is a known indication
        approved = approved_indications.get(ingredient.upper(), "")
        if is_known_indication(approved, indication):
            skipped_known.add(key)
            skipped_known_count += 1
            print(f"[{i+1}/{total}] {ingredient} - {indication[:40]}... SKIP (known indication)")
            continue

        if new_results >= max_per_run:
            print(f"\nReached limit of {max_per_run} pairs. Run again to continue.")
            break

        try:
            print(f"[{i+1}/{total}] {ingredient} - {indication[:50]}...", end=" ", flush=True)

            result = collect_evidence_for_pair(
                ingredient, indication, ct_collector, pm_collector
            )
            result["drugbank_id"] = drugbank_id
            result["is_repurposing"] = True  # Mark as true repurposing candidate

            results[key] = result
            processed.add(key)
            new_results += 1

            level = result["evidence_level"]
            ct_count = result["ct_trial_count"]
            pm_count = result["pubmed_article_count"]
            print(f"-> {level} (CT:{ct_count}, PM:{pm_count})")

            # Save progress every 10 pairs
            if new_results % 10 == 0:
                save_progress(progress_file, processed)
                with open(results_file, "w") as f:
                    json.dump(results, f, indent=2)
                with open(skipped_file, "w") as f:
                    json.dump(list(skipped_known), f)

            # Rate limiting (be nice to APIs)
            time.sleep(0.5)

        except Exception as e:
            print(f"ERROR: {e}")
            errors += 1
            continue

    # Final save
    save_progress(progress_file, processed)
    with open(results_file, "w") as f:
        json.dump(results, f, indent=2)
    with open(skipped_file, "w") as f:
        json.dump(list(skipped_known), f)

    # Generate summary
    level_counts = {"L1": 0, "L2": 0, "L3": 0, "L4": 0, "L5": 0}
    for result in results.values():
        level = result.get("evidence_level", "L5")
        level_counts[level] = level_counts.get(level, 0) + 1

    total_skipped_known = len(skipped_known)
    effective_total = total - total_skipped_known

    summary = {
        "last_updated": datetime.now(timezone.utc).isoformat(),
        "total_pairs": total,
        "skipped_known_indications": total_skipped_known,
        "effective_pairs": effective_total,
        "processed": len(processed),
        "remaining": effective_total - len(processed),
        "this_run": new_results,
        "this_run_skipped_known": skipped_known_count,
        "errors": errors,
        "level_distribution": level_counts,
    }

    with open(summary_file, "w") as f:
        json.dump(summary, f, indent=2)

    print("\n" + "=" * 60)
    print("Summary:")
    print(f"  Total pairs: {total}")
    print(f"  Skipped (known indications): {total_skipped_known}")
    print(f"  Effective pairs: {effective_total}")
    print(f"  Processed: {len(processed)}")
    print(f"  This run: {new_results}")
    print(f"  This run skipped (known): {skipped_known_count}")
    print(f"  Errors: {errors}")
    print(f"  Remaining: {effective_total - len(processed)}")
    print("\nEvidence Level Distribution (repurposing only):")
    for level, count in sorted(level_counts.items()):
        print(f"  {level}: {count}")
    print("=" * 60)


if __name__ == "__main__":
    main()
