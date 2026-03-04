#!/usr/bin/env python3
"""
Fetch health news from European sources for EuTxGNN drug monitoring.

Uses keywords.json to match drugs and diseases, with drug-disease relations.
When a disease is matched, related drugs are automatically included.

Sources:
- EMA (European Medicines Agency) RSS feeds
- ECDC (European Centre for Disease Prevention and Control)
"""

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from xml.etree import ElementTree as ET

# RSS feed URLs (verified March 2026)
RSS_FEEDS = {
    # EMA feeds
    "ema_news": "https://www.ema.europa.eu/en/news.xml",
    "ema_whats_new": "https://www.ema.europa.eu/en/whats-new.xml",
    "ema_human_medicines": "https://www.ema.europa.eu/en/human-medicine-new.xml",
    "ema_new_human_medicines": "https://www.ema.europa.eu/en/new-human-medicine-new.xml",
    # ECDC feeds
    "ecdc_news": "https://www.ecdc.europa.eu/en/taxonomy/term/1307/feed",
    "ecdc_risk": "https://www.ecdc.europa.eu/en/taxonomy/term/1295/feed",
    "ecdc_guidance": "https://www.ecdc.europa.eu/en/taxonomy/term/1301/feed",
    "ecdc_epidemiological": "https://www.ecdc.europa.eu/en/taxonomy/term/1310/feed",
}


def load_keywords():
    """Load keywords.json with drug-disease relations."""
    keywords_path = Path(__file__).parent.parent / "data" / "news" / "keywords.json"
    if keywords_path.exists():
        with open(keywords_path) as f:
            return json.load(f)
    return {"drugs": [], "indications": []}


def fetch_rss(url: str, source_name: str) -> list:
    """Fetch and parse an RSS feed."""
    items = []
    try:
        req = Request(url, headers={"User-Agent": "EuTxGNN-NewsBot/1.0"})
        with urlopen(req, timeout=30) as response:
            content = response.read()
            root = ET.fromstring(content)

            # Handle different RSS formats
            # Standard RSS 2.0
            for item in root.findall(".//item"):
                title = item.findtext("title", "")
                link = item.findtext("link", "")
                description = item.findtext("description", "")
                pub_date = item.findtext("pubDate", "")

                if title and link:
                    items.append({
                        "source": source_name,
                        "title": title.strip(),
                        "link": link.strip(),
                        "description": clean_html(description),
                        "pub_date": pub_date,
                    })

            # Atom format
            ns = {"atom": "http://www.w3.org/2005/Atom"}
            for entry in root.findall(".//atom:entry", ns):
                title = entry.findtext("atom:title", "", ns)
                link_elem = entry.find("atom:link", ns)
                link = link_elem.get("href", "") if link_elem is not None else ""
                summary = entry.findtext("atom:summary", "", ns)
                updated = entry.findtext("atom:updated", "", ns)

                if title and link:
                    items.append({
                        "source": source_name,
                        "title": title.strip(),
                        "link": link.strip(),
                        "description": clean_html(summary),
                        "pub_date": updated,
                    })

    except (URLError, HTTPError, ET.ParseError) as e:
        print(f"Warning: Failed to fetch {source_name}: {e}", file=sys.stderr)

    return items


def clean_html(text: str) -> str:
    """Remove HTML tags from text."""
    if not text:
        return ""
    # Remove HTML tags
    clean = re.sub(r'<[^>]+>', '', text)
    # Normalize whitespace
    clean = re.sub(r'\s+', ' ', clean).strip()
    return clean[:500]  # Limit description length


def match_keywords(text: str, keywords: dict) -> dict:
    """
    Find matching drugs and diseases in text.
    When a disease matches, include its related_drugs.
    """
    text_lower = text.lower()
    matches = {
        "drugs": [],           # Directly matched drugs
        "diseases": [],        # Matched diseases
        "related_drugs": [],   # Drugs related to matched diseases
    }

    # Match drugs directly
    for drug in keywords.get("drugs", []):
        drug_name = drug.get("name", "")
        drug_slug = drug.get("slug", "")

        for kw in drug.get("keywords", []):
            if len(kw) > 3 and kw.lower() in text_lower:
                if drug_slug not in [d["slug"] for d in matches["drugs"]]:
                    matches["drugs"].append({
                        "name": drug_name,
                        "slug": drug_slug,
                        "url": drug.get("url", f"/drugs/{drug_slug}/")
                    })
                break

    # Match diseases and include related drugs
    for indication in keywords.get("indications", []):
        ind_name = indication.get("name", "")

        for kw in indication.get("keywords", []):
            if len(kw) > 3 and kw.lower() in text_lower:
                if ind_name not in [d["name"] for d in matches["diseases"]]:
                    matches["diseases"].append({
                        "name": ind_name,
                        "keyword": kw,
                        "related_drugs": indication.get("related_drugs", [])[:5]  # Top 5
                    })
                    # Add related drugs
                    for drug_slug in indication.get("related_drugs", [])[:5]:
                        if drug_slug not in matches["related_drugs"]:
                            matches["related_drugs"].append(drug_slug)
                break

    return matches


def main():
    print("Fetching EU health news...")

    keywords = load_keywords()
    print(f"Loaded {keywords.get('drug_count', 0)} drugs and {keywords.get('indication_count', 0)} disease categories")

    all_items = []

    # Fetch from all RSS feeds
    for source_name, url in RSS_FEEDS.items():
        print(f"Fetching {source_name}...")
        items = fetch_rss(url, source_name)
        print(f"  Found {len(items)} items")
        all_items.extend(items)

    # Match keywords and filter relevant items
    relevant_items = []
    drug_disease_pairs = []  # News with BOTH drug and disease

    for item in all_items:
        search_text = f"{item['title']} {item['description']}"
        matches = match_keywords(search_text, keywords)

        # Check if we have drug-disease pairs
        has_drug = len(matches["drugs"]) > 0 or len(matches["related_drugs"]) > 0
        has_disease = len(matches["diseases"]) > 0

        if has_drug or has_disease:
            item["matched_drugs"] = matches["drugs"]
            item["matched_diseases"] = matches["diseases"]
            item["related_drugs"] = matches["related_drugs"]
            relevant_items.append(item)

            # Track drug-disease pairs
            if has_drug and has_disease:
                drug_disease_pairs.append(item)

    # Sort by relevance (drug-disease pairs first, then by match count)
    relevant_items.sort(
        key=lambda x: (
            len(x.get("matched_drugs", [])) > 0 and len(x.get("matched_diseases", [])) > 0,
            len(x.get("matched_drugs", [])) + len(x.get("matched_diseases", [])) + len(x.get("related_drugs", []))
        ),
        reverse=True
    )

    # Prepare output
    output = {
        "description": "EU health news with drug-disease relations from EuTxGNN",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "total_items": len(all_items),
        "relevant_items": len(relevant_items),
        "drug_disease_pairs": len(drug_disease_pairs),
        "sources": list(RSS_FEEDS.keys()),
        "items": relevant_items[:50],  # Keep top 50 relevant items
    }

    # Save to file
    output_path = Path(__file__).parent.parent / "data" / "news" / "eu_health_news.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nResults saved to {output_path}")
    print(f"Total items fetched: {len(all_items)}")
    print(f"Relevant items: {len(relevant_items)}")
    print(f"Drug-disease pairs: {len(drug_disease_pairs)}")

    # Print summary of drug-disease pairs
    if drug_disease_pairs:
        print("\nDrug-disease pair news:")
        for item in drug_disease_pairs[:5]:
            print(f"  - {item['title'][:70]}...")
            drugs = [d['name'] for d in item.get('matched_drugs', [])]
            diseases = [d['name'] for d in item.get('matched_diseases', [])]
            related = item.get('related_drugs', [])[:3]
            print(f"    Drugs: {drugs}")
            print(f"    Diseases: {diseases}")
            if related:
                print(f"    Related drugs: {related}")


if __name__ == "__main__":
    main()
