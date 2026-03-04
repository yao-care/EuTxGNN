#!/usr/bin/env python3
"""Update drug markdown files with collected evidence levels.

This script reads evidence results and updates drug reports to reflect
the best evidence level found for each drug across all its indications.
"""

import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path


def load_evidence_results(results_file: str) -> dict:
    """Load evidence results from JSON."""
    if os.path.exists(results_file):
        with open(results_file, "r") as f:
            return json.load(f)
    return {}


def aggregate_by_drug(results: dict) -> dict:
    """
    Aggregate evidence by drug, keeping best evidence level per indication.

    Returns:
        dict mapping ingredient name to list of indications with evidence
    """
    drug_evidence = defaultdict(list)

    for key, result in results.items():
        drug = result.get("drug", "").lower()
        indication = result.get("indication", "")
        level = result.get("evidence_level", "L5")
        drugbank_id = result.get("drugbank_id", "")

        drug_evidence[drug].append({
            "indication": indication,
            "evidence_level": level,
            "drugbank_id": drugbank_id,
            "ct_trial_count": result.get("ct_trial_count", 0),
            "pubmed_article_count": result.get("pubmed_article_count", 0),
            "phase3_count": result.get("phase3_count", 0),
            "phase2_count": result.get("phase2_count", 0),
            "rct_count": result.get("rct_count", 0),
            "review_count": result.get("review_count", 0),
            "summary": result.get("summary", ""),
        })

    return drug_evidence


def get_best_evidence_level(indications: list[dict]) -> str:
    """Get best (lowest L number) evidence level from list of indications."""
    level_order = {"L1": 1, "L2": 2, "L3": 3, "L4": 4, "L5": 5}
    best = 5
    for ind in indications:
        level = ind.get("evidence_level", "L5")
        if level in level_order:
            best = min(best, level_order[level])
    return f"L{best}"


def get_parent_folder(level: str) -> str:
    """Get parent folder name for evidence level."""
    level_parents = {
        "L1": "Phase 3+ Evidence (L1)",
        "L2": "Phase 2 Evidence (L2)",
        "L3": "Observational Evidence (L3)",
        "L4": "Preclinical Evidence (L4)",
        "L5": "AI Predictions (L5)",
    }
    return level_parents.get(level, "AI Predictions (L5)")


def slugify(name: str) -> str:
    """Convert drug name to file slug."""
    slug = name.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    return slug


def update_drug_file(
    drug_file: Path,
    drug_name: str,
    best_level: str,
    evidence_indications: list[dict],
) -> bool:
    """
    Update a drug markdown file with new evidence level.

    Returns:
        True if file was updated, False otherwise
    """
    if not drug_file.exists():
        return False

    content = drug_file.read_text(encoding="utf-8")

    # Check current evidence level
    current_level_match = re.search(r"evidence_level:\s*(L\d)", content)
    current_level = current_level_match.group(1) if current_level_match else "L5"

    # Only update if we have better evidence
    level_order = {"L1": 1, "L2": 2, "L3": 3, "L4": 4, "L5": 5}
    if level_order.get(best_level, 5) >= level_order.get(current_level, 5):
        return False  # No improvement

    # Update front matter
    new_content = re.sub(
        r"(evidence_level:\s*)L\d",
        f"\\g<1>{best_level}",
        content
    )

    # Update parent folder
    new_parent = get_parent_folder(best_level)
    new_content = re.sub(
        r"(parent:\s*).*",
        f"\\g<1>{new_parent}",
        new_content
    )

    # Update description
    new_content = re.sub(
        r'(description:\s*")[^"]*Evidence level L\d',
        f'\\g<1>{drug_name} drug repurposing predictions from TxGNN. Evidence level {best_level}',
        new_content
    )

    # Update inline evidence level display
    new_content = re.sub(
        r"(Evidence Level:\s*\*\*)L\d(\*\*)",
        f"\\g<1>{best_level}\\g<2>",
        new_content
    )

    # Update table evidence level
    new_content = re.sub(
        r"(\| Evidence Level \|)\s*L\d\s*(\|)",
        f"\\g<1> {best_level} \\g<2>",
        new_content
    )

    # Add or update clinical evidence section
    evidence_section = generate_evidence_section(evidence_indications)

    # Check if evidence section exists
    if "## Clinical Evidence" in new_content:
        # Replace existing section
        new_content = re.sub(
            r"## Clinical Evidence.*?(?=\n---\n|\n## About TxGNN)",
            evidence_section,
            new_content,
            flags=re.DOTALL
        )
    else:
        # Insert before "About TxGNN Predictions"
        new_content = new_content.replace(
            "## About TxGNN Predictions",
            evidence_section + "## About TxGNN Predictions"
        )

    drug_file.write_text(new_content, encoding="utf-8")
    return True


def generate_evidence_section(indications: list[dict]) -> str:
    """Generate clinical evidence section for drug report."""
    # Sort by evidence level (best first), then by number of trials/articles
    sorted_ind = sorted(
        indications,
        key=lambda x: (
            {"L1": 1, "L2": 2, "L3": 3, "L4": 4, "L5": 5}.get(x["evidence_level"], 5),
            -(x.get("ct_trial_count", 0) + x.get("pubmed_article_count", 0))
        )
    )

    # Only show indications with actual evidence (L1-L4)
    with_evidence = [i for i in sorted_ind if i["evidence_level"] != "L5"]

    if not with_evidence:
        return ""

    lines = [
        "## Clinical Evidence",
        "",
        "The following indications have supporting clinical evidence:",
        "",
        "| Indication | Level | Trials | Articles | Summary |",
        "|------------|:-----:|:------:|:--------:|---------|",
    ]

    for ind in with_evidence[:20]:  # Top 20
        indication = ind["indication"]
        level = ind["evidence_level"]
        trials = ind.get("ct_trial_count", 0)
        articles = ind.get("pubmed_article_count", 0)
        summary = ind.get("summary", "")[:50]

        lines.append(f"| {indication} | {level} | {trials} | {articles} | {summary} |")

    if len(with_evidence) > 20:
        lines.append("")
        lines.append(f"*Showing top 20 of {len(with_evidence)} indications with evidence.*")

    lines.append("")
    lines.append("---")
    lines.append("")

    return "\n".join(lines)


def main():
    """Run evidence update."""
    base_dir = Path(__file__).parent.parent

    # Paths
    results_file = base_dir / "data/evidence/evidence_results.json"
    drugs_dir = base_dir / "docs/_drugs"

    if not results_file.exists():
        print(f"No evidence results found at {results_file}")
        print("Run collect_evidence.py first.")
        sys.exit(1)

    # Load results
    print(f"Loading evidence from {results_file}...")
    results = load_evidence_results(results_file)
    print(f"Loaded {len(results)} evidence records")

    # Aggregate by drug
    drug_evidence = aggregate_by_drug(results)
    print(f"Found evidence for {len(drug_evidence)} unique drugs")

    # Update drug files
    updated = 0
    not_found = 0
    no_improvement = 0

    for drug_name, indications in drug_evidence.items():
        best_level = get_best_evidence_level(indications)

        if best_level == "L5":
            no_improvement += 1
            continue

        # Find drug file
        drug_slug = slugify(drug_name)
        drug_file = drugs_dir / f"{drug_slug}.md"

        if not drug_file.exists():
            # Try without hyphens
            alt_slug = drug_slug.replace("-", "")
            drug_file = drugs_dir / f"{alt_slug}.md"

        if not drug_file.exists():
            not_found += 1
            continue

        if update_drug_file(drug_file, drug_name, best_level, indications):
            print(f"  Updated {drug_name}: -> {best_level}")
            updated += 1
        else:
            no_improvement += 1

    print("\n" + "=" * 60)
    print("Summary:")
    print(f"  Updated: {updated}")
    print(f"  No improvement needed: {no_improvement}")
    print(f"  Drug files not found: {not_found}")
    print("=" * 60)


if __name__ == "__main__":
    main()
