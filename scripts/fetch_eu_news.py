#!/usr/bin/env python3
"""
Fetch health news from European sources for EuTxGNN drug monitoring.

Sources:
- EMA (European Medicines Agency) RSS feeds
- ECDC (European Centre for Disease Prevention and Control)
- WHO Europe news
- Reuters Health (EU focused)
"""

import json
import re
import sys
from datetime import datetime, timedelta, timezone
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

def load_synonyms():
    """Load drug and disease synonyms for matching."""
    synonyms_path = Path(__file__).parent.parent / "data" / "news" / "synonyms.json"
    if synonyms_path.exists():
        with open(synonyms_path) as f:
            return json.load(f)
    return {"indication_synonyms": {}, "drug_synonyms": {}}

def load_drug_list():
    """Load the list of EuTxGNN drugs."""
    drug_list_path = Path(__file__).parent.parent / "data" / "processed" / "ema_drugs_mapped.json"
    if drug_list_path.exists():
        with open(drug_list_path) as f:
            data = json.load(f)
            # Extract drug names
            drugs = set()
            for item in data:
                if "brand_name" in item:
                    drugs.add(item["brand_name"].lower())
                if "active_substance" in item:
                    drugs.add(item["active_substance"].lower())
            return drugs
    return set()

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

def match_keywords(text: str, synonyms: dict, drugs: set) -> dict:
    """Find matching drugs and diseases in text."""
    text_lower = text.lower()
    matches = {"drugs": [], "diseases": []}

    # Match drugs
    for drug in drugs:
        if len(drug) > 3 and drug in text_lower:
            matches["drugs"].append(drug)

    # Match drug synonyms
    for drug, syns in synonyms.get("drug_synonyms", {}).items():
        for syn in [drug] + syns:
            if len(syn) > 3 and syn.lower() in text_lower:
                if drug not in matches["drugs"]:
                    matches["drugs"].append(drug)
                break

    # Match disease synonyms
    for disease, syns in synonyms.get("indication_synonyms", {}).items():
        for syn in [disease] + syns:
            if len(syn) > 3 and syn.lower() in text_lower:
                if disease not in matches["diseases"]:
                    matches["diseases"].append(disease)
                break

    return matches

def main():
    print("Fetching EU health news...")

    synonyms = load_synonyms()
    drugs = load_drug_list()
    print(f"Loaded {len(drugs)} drugs and {len(synonyms.get('indication_synonyms', {}))} disease categories")

    all_items = []

    # Fetch from all RSS feeds
    for source_name, url in RSS_FEEDS.items():
        print(f"Fetching {source_name}...")
        items = fetch_rss(url, source_name)
        print(f"  Found {len(items)} items")
        all_items.extend(items)

    # Match keywords and filter relevant items
    relevant_items = []
    for item in all_items:
        search_text = f"{item['title']} {item['description']}"
        matches = match_keywords(search_text, synonyms, drugs)

        if matches["drugs"] or matches["diseases"]:
            item["matched_drugs"] = matches["drugs"][:5]  # Limit to top 5
            item["matched_diseases"] = matches["diseases"][:5]
            relevant_items.append(item)

    # Sort by relevance (more matches = more relevant)
    relevant_items.sort(
        key=lambda x: len(x.get("matched_drugs", [])) + len(x.get("matched_diseases", [])),
        reverse=True
    )

    # Prepare output
    output = {
        "description": "EU health news aggregated from European sources",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "total_items": len(all_items),
        "relevant_items": len(relevant_items),
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
    print(f"Relevant items (matched keywords): {len(relevant_items)}")

    # Print summary of top items
    if relevant_items:
        print("\nTop relevant news:")
        for item in relevant_items[:5]:
            print(f"  - {item['title'][:80]}...")
            print(f"    Drugs: {item.get('matched_drugs', [])}")
            print(f"    Diseases: {item.get('matched_diseases', [])}")

if __name__ == "__main__":
    main()
