#!/usr/bin/env python3
"""
Fetch health news from European sources for EuTxGNN drug monitoring.

Sources:
- Google News Health (UK, Germany, France, Spain, Italy)
- EMA (European Medicines Agency) RSS feeds
- ECDC (European Centre for Disease Prevention and Control)

Uses keywords.json to match drugs and diseases with drug-disease relations.
"""

import json
import re
import sys
import hashlib
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from xml.etree import ElementTree as ET

# === RSS Feed Configuration ===

# Google News Health RSS for European countries
GOOGLE_NEWS_FEEDS = {
    "google_uk": {
        "name": "Google News UK",
        "url": "https://news.google.com/rss/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JYcG9MVlJYS0FBUAE?hl=en-GB&gl=GB&ceid=GB:en",
    },
    "google_de": {
        "name": "Google News Germany",
        "url": "https://news.google.com/rss/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JYcG9MVlJYS0FBUAE?hl=de&gl=DE&ceid=DE:de",
    },
    "google_fr": {
        "name": "Google News France",
        "url": "https://news.google.com/rss/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JYcG9MVlJYS0FBUAE?hl=fr&gl=FR&ceid=FR:fr",
    },
    "google_es": {
        "name": "Google News Spain",
        "url": "https://news.google.com/rss/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JYcG9MVlJYS0FBUAE?hl=es&gl=ES&ceid=ES:es",
    },
    "google_it": {
        "name": "Google News Italy",
        "url": "https://news.google.com/rss/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JYcG9MVlJYS0FBUAE?hl=it&gl=IT&ceid=IT:it",
    },
}

# Official EU agency feeds
EU_AGENCY_FEEDS = {
    "ema_news": {
        "name": "EMA News",
        "url": "https://www.ema.europa.eu/en/news.xml",
    },
    "ema_human_medicines": {
        "name": "EMA Human Medicines",
        "url": "https://www.ema.europa.eu/en/human-medicine-new.xml",
    },
    "ecdc_news": {
        "name": "ECDC News",
        "url": "https://www.ecdc.europa.eu/en/taxonomy/term/1307/feed",
    },
    "ecdc_risk": {
        "name": "ECDC Risk Assessments",
        "url": "https://www.ecdc.europa.eu/en/taxonomy/term/1295/feed",
    },
}


def load_keywords():
    """Load keywords.json with drug-disease relations."""
    keywords_path = Path(__file__).parent.parent / "data" / "news" / "keywords.json"
    if keywords_path.exists():
        with open(keywords_path) as f:
            return json.load(f)
    return {"drugs": [], "indications": []}


def generate_id(title: str, link: str) -> str:
    """Generate news ID based on title and link hash"""
    content = f"{title}:{link}"
    return hashlib.sha256(content.encode()).hexdigest()[:12]


def clean_html(text: str) -> str:
    """Remove HTML tags from text."""
    if not text:
        return ""
    clean = re.sub(r'<[^>]+>', '', text)
    clean = re.sub(r'\s+', ' ', clean).strip()
    return clean[:500]


def parse_pub_date(pub_date_str: str) -> str:
    """Parse publication date to ISO format"""
    if not pub_date_str:
        return datetime.now(timezone.utc).isoformat()

    formats = [
        "%a, %d %b %Y %H:%M:%S %z",
        "%a, %d %b %Y %H:%M:%S GMT",
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%SZ",
    ]

    for fmt in formats:
        try:
            dt = datetime.strptime(pub_date_str.strip(), fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.isoformat()
        except ValueError:
            continue

    return datetime.now(timezone.utc).isoformat()


def extract_source_name(entry_element, default: str) -> str:
    """Extract source name from RSS entry (Google News includes <source> tag)"""
    source_elem = entry_element.find("source")
    if source_elem is not None and source_elem.text:
        return source_elem.text.strip()
    return default


def fetch_rss(url: str, source_key: str, source_name: str) -> list:
    """Fetch and parse an RSS feed."""
    items = []
    try:
        req = Request(url, headers={
            "User-Agent": "Mozilla/5.0 (compatible; EuTxGNN-NewsBot/1.0)"
        })
        with urlopen(req, timeout=30) as response:
            content = response.read()
            root = ET.fromstring(content)

            # Standard RSS 2.0
            for item in root.findall(".//item"):
                title = item.findtext("title", "")
                link = item.findtext("link", "")
                description = item.findtext("description", "")
                pub_date = item.findtext("pubDate", "")

                # Extract actual source (for Google News)
                actual_source = extract_source_name(item, source_name)

                if title and link:
                    items.append({
                        "id": generate_id(title, link),
                        "source": actual_source,
                        "source_feed": source_key,
                        "title": clean_html(title),
                        "link": link.strip(),
                        "description": clean_html(description),
                        "pub_date": parse_pub_date(pub_date),
                    })

            # Atom format (for some ECDC feeds)
            ns = {"atom": "http://www.w3.org/2005/Atom"}
            for entry in root.findall(".//atom:entry", ns):
                title = entry.findtext("atom:title", "", ns)
                link_elem = entry.find("atom:link", ns)
                link = link_elem.get("href", "") if link_elem is not None else ""
                summary = entry.findtext("atom:summary", "", ns)
                updated = entry.findtext("atom:updated", "", ns)

                if title and link:
                    items.append({
                        "id": generate_id(title, link),
                        "source": source_name,
                        "source_feed": source_key,
                        "title": clean_html(title),
                        "link": link.strip(),
                        "description": clean_html(summary),
                        "pub_date": parse_pub_date(updated),
                    })

    except (URLError, HTTPError, ET.ParseError) as e:
        print(f"  Warning: Failed to fetch {source_name}: {e}", file=sys.stderr)

    return items


def match_keywords(text: str, keywords: dict) -> dict:
    """
    Find matching drugs and diseases in text.
    When a disease matches, include its related_drugs.
    """
    text_lower = text.lower()
    matches = {
        "drugs": [],
        "diseases": [],
        "related_drugs": [],
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
                        "related_drugs": indication.get("related_drugs", [])[:5]
                    })
                    for drug_slug in indication.get("related_drugs", [])[:5]:
                        if drug_slug not in matches["related_drugs"]:
                            matches["related_drugs"].append(drug_slug)
                break

    return matches


def deduplicate_news(items: list) -> list:
    """Remove duplicate news based on title similarity"""
    seen_titles = {}
    unique_items = []

    for item in items:
        # Normalize title for comparison
        title_key = re.sub(r'\W+', '', item["title"].lower())[:50]

        if title_key not in seen_titles:
            seen_titles[title_key] = True
            unique_items.append(item)

    return unique_items


def main():
    print("Fetching EU health news...")

    keywords = load_keywords()
    print(f"Loaded {keywords.get('drug_count', 0)} drugs and {keywords.get('indication_count', 0)} disease categories")

    all_items = []

    # Fetch from Google News feeds (main source for media news)
    print("\n=== Google News Health ===")
    for source_key, config in GOOGLE_NEWS_FEEDS.items():
        print(f"Fetching {config['name']}...")
        items = fetch_rss(config["url"], source_key, config["name"])
        print(f"  Found {len(items)} items")
        all_items.extend(items)

    # Fetch from EU agency feeds (official sources)
    print("\n=== EU Official Sources ===")
    for source_key, config in EU_AGENCY_FEEDS.items():
        print(f"Fetching {config['name']}...")
        items = fetch_rss(config["url"], source_key, config["name"])
        print(f"  Found {len(items)} items")
        all_items.extend(items)

    # Deduplicate
    print(f"\nTotal items before dedup: {len(all_items)}")
    all_items = deduplicate_news(all_items)
    print(f"After dedup: {len(all_items)}")

    # Match keywords and filter relevant items
    relevant_items = []

    for item in all_items:
        search_text = f"{item['title']} {item['description']}"
        matches = match_keywords(search_text, keywords)

        has_disease = len(matches["diseases"]) > 0

        if has_disease:  # Only include news with disease matches (which have related drugs)
            item["matched_drugs"] = matches["drugs"]
            item["matched_diseases"] = matches["diseases"]
            item["related_drugs"] = matches["related_drugs"]
            relevant_items.append(item)

    # Sort by date (newest first)
    relevant_items.sort(key=lambda x: x.get("pub_date", ""), reverse=True)

    # Prepare output
    output = {
        "description": "EU health news with drug-disease relations from EuTxGNN",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "total_items": len(all_items),
        "relevant_items": len(relevant_items),
        "sources": list(GOOGLE_NEWS_FEEDS.keys()) + list(EU_AGENCY_FEEDS.keys()),
        "items": relevant_items[:100],  # Keep top 100 relevant items
    }

    # Save to file
    output_path = Path(__file__).parent.parent / "data" / "news" / "eu_health_news.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\n=== Results ===")
    print(f"Output: {output_path}")
    print(f"Total items fetched: {len(all_items)}")
    print(f"Disease-related items: {len(relevant_items)}")

    # Print summary
    if relevant_items:
        print("\nSample disease-related news:")
        for item in relevant_items[:5]:
            diseases = [d['name'] for d in item.get('matched_diseases', [])]
            related = item.get('related_drugs', [])[:3]
            print(f"  - [{item['source']}] {item['title'][:60]}...")
            print(f"    Diseases: {diseases}")
            print(f"    Related drugs: {related}")


if __name__ == "__main__":
    main()
