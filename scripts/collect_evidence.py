#!/usr/bin/env python3
"""Batch evidence collection for drug-indication pairs.

Collects evidence from ClinicalTrials.gov and PubMed for all drug-indication
pairs in the repurposing candidates file, evaluates evidence levels, and
stores results for website generation.
"""

import csv
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from eutxgnn.collectors import ClinicalTrialsCollector, PubMedCollector


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
    output_dir = base_dir / "data/evidence"
    output_dir.mkdir(parents=True, exist_ok=True)

    results_file = output_dir / "evidence_results.json"
    progress_file = output_dir / "progress.json"
    summary_file = output_dir / "evidence_summary.json"

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

    # Initialize collectors
    ct_collector = ClinicalTrialsCollector(max_results=20)
    pm_collector = PubMedCollector(max_results=20)

    # Process pairs
    total = len(pairs)
    skipped = 0
    errors = 0
    new_results = 0

    # Limit for this run (to avoid rate limiting)
    max_per_run = int(os.environ.get("MAX_PAIRS", "100"))

    print(f"\nProcessing up to {max_per_run} pairs this run...")
    print("-" * 60)

    for i, (drugbank_id, ingredient, indication) in enumerate(pairs):
        key = f"{drugbank_id}:{indication}"

        if key in processed:
            skipped += 1
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

    # Generate summary
    level_counts = {"L1": 0, "L2": 0, "L3": 0, "L4": 0, "L5": 0}
    for result in results.values():
        level = result.get("evidence_level", "L5")
        level_counts[level] = level_counts.get(level, 0) + 1

    summary = {
        "last_updated": datetime.now(timezone.utc).isoformat(),
        "total_pairs": total,
        "processed": len(processed),
        "remaining": total - len(processed),
        "this_run": new_results,
        "errors": errors,
        "level_distribution": level_counts,
    }

    with open(summary_file, "w") as f:
        json.dump(summary, f, indent=2)

    print("\n" + "=" * 60)
    print("Summary:")
    print(f"  Total pairs: {total}")
    print(f"  Processed: {len(processed)}")
    print(f"  This run: {new_results}")
    print(f"  Errors: {errors}")
    print(f"  Remaining: {total - len(processed)}")
    print("\nEvidence Level Distribution:")
    for level, count in sorted(level_counts.items()):
        print(f"  {level}: {count}")
    print("=" * 60)


if __name__ == "__main__":
    main()
