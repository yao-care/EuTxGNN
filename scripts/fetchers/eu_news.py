#!/usr/bin/env python3
"""EU Health News Fetcher

Fetches health-related news from European sources:
- EMA (European Medicines Agency) news and press releases
- ECDC (European Centre for Disease Prevention and Control)
- WHO Europe
- Major European health news RSS feeds

Usage:
    uv run python scripts/fetchers/eu_news.py

Output:
    data/news/eu_health_news.json
"""

import json
import re
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import Any

import feedparser
import requests
from bs4 import BeautifulSoup


@dataclass
class NewsItem:
    """A single news item."""
    title: str
    url: str
    source: str
    published: str
    summary: str = ""
    categories: list[str] = field(default_factory=list)
    drugs_mentioned: list[str] = field(default_factory=list)
    diseases_mentioned: list[str] = field(default_factory=list)
    fetched_at: str = field(default_factory=lambda: datetime.now().isoformat())


# European health news RSS feeds
NEWS_SOURCES = {
    "ema_news": {
        "name": "EMA News",
        "url": "https://www.ema.europa.eu/en/news/rss.xml",
        "type": "rss"
    },
    "ema_press": {
        "name": "EMA Press Releases",
        "url": "https://www.ema.europa.eu/en/news-events/press-releases/rss.xml",
        "type": "rss"
    },
    "ecdc": {
        "name": "ECDC News",
        "url": "https://www.ecdc.europa.eu/en/rss.xml",
        "type": "rss"
    },
    "who_europe": {
        "name": "WHO Europe",
        "url": "https://www.who.int/europe/rss-feeds/news-english.xml",
        "type": "rss"
    },
    "medscape_eu": {
        "name": "Medscape Europe",
        "url": "https://www.medscape.com/cx/rssfeeds/2212.xml",
        "type": "rss"
    },
    "reuters_health": {
        "name": "Reuters Health",
        "url": "https://www.reutersagency.com/feed/?best-topics=health&post_type=best",
        "type": "rss"
    }
}


def load_synonyms() -> dict:
    """Load drug and disease synonyms from synonyms.json"""
    synonyms_path = Path(__file__).parent.parent.parent / "data" / "news" / "synonyms.json"
    if synonyms_path.exists():
        with open(synonyms_path, encoding="utf-8") as f:
            return json.load(f)
    return {"indication_synonyms": {}, "drug_synonyms": {}}


def build_keyword_patterns(synonyms: dict) -> tuple[dict, dict]:
    """Build regex patterns for keyword matching."""
    disease_patterns = {}
    drug_patterns = {}

    # Build disease patterns
    for disease, syns in synonyms.get("indication_synonyms", {}).items():
        all_terms = [disease] + syns
        pattern = re.compile(
            r'\b(' + '|'.join(re.escape(t) for t in all_terms) + r')\b',
            re.IGNORECASE
        )
        disease_patterns[disease] = pattern

    # Build drug patterns
    for drug, syns in synonyms.get("drug_synonyms", {}).items():
        all_terms = [drug] + syns
        pattern = re.compile(
            r'\b(' + '|'.join(re.escape(t) for t in all_terms) + r')\b',
            re.IGNORECASE
        )
        drug_patterns[drug] = pattern

    return disease_patterns, drug_patterns


def extract_mentions(
    text: str,
    disease_patterns: dict,
    drug_patterns: dict
) -> tuple[list[str], list[str]]:
    """Extract drug and disease mentions from text."""
    diseases = []
    drugs = []

    for disease, pattern in disease_patterns.items():
        if pattern.search(text):
            diseases.append(disease)

    for drug, pattern in drug_patterns.items():
        if pattern.search(text):
            drugs.append(drug)

    return drugs, diseases


def fetch_rss_feed(source_id: str, source_config: dict) -> list[NewsItem]:
    """Fetch news items from an RSS feed."""
    items = []
    try:
        feed = feedparser.parse(source_config["url"])

        for entry in feed.entries[:50]:  # Limit to 50 most recent
            title = entry.get("title", "")
            link = entry.get("link", "")
            summary = entry.get("summary", entry.get("description", ""))

            # Clean HTML from summary
            if summary:
                soup = BeautifulSoup(summary, "html.parser")
                summary = soup.get_text(separator=" ", strip=True)[:500]

            # Parse published date
            published = ""
            if hasattr(entry, "published_parsed") and entry.published_parsed:
                try:
                    published = datetime(*entry.published_parsed[:6]).isoformat()
                except (TypeError, ValueError):
                    published = entry.get("published", "")
            elif hasattr(entry, "updated_parsed") and entry.updated_parsed:
                try:
                    published = datetime(*entry.updated_parsed[:6]).isoformat()
                except (TypeError, ValueError):
                    published = entry.get("updated", "")

            # Get categories
            categories = []
            if hasattr(entry, "tags"):
                categories = [tag.term for tag in entry.tags if hasattr(tag, "term")]

            items.append(NewsItem(
                title=title,
                url=link,
                source=source_config["name"],
                published=published,
                summary=summary,
                categories=categories
            ))

    except Exception as e:
        print(f"  Warning: Failed to fetch {source_config['name']}: {e}")

    return items


def fetch_ema_safety_updates() -> list[NewsItem]:
    """Fetch EMA safety communications (HTML scraping fallback)."""
    items = []
    url = "https://www.ema.europa.eu/en/medicines/ema_group_types/ema_medicine/field_ema_web_categories%253Aname_field/Human"

    try:
        headers = {
            "User-Agent": "EuTxGNN-NewsFetcher/1.0 (Research Project)"
        }
        response = requests.get(url, headers=headers, timeout=30)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            # Look for medicine updates
            for article in soup.select("article, .views-row")[:20]:
                title_elem = article.select_one("h2, h3, .title, a")
                if title_elem:
                    title = title_elem.get_text(strip=True)
                    link = title_elem.get("href", "")
                    if link and not link.startswith("http"):
                        link = "https://www.ema.europa.eu" + link

                    items.append(NewsItem(
                        title=title,
                        url=link,
                        source="EMA Safety Updates",
                        published=datetime.now().isoformat(),
                        summary=""
                    ))
    except Exception as e:
        print(f"  Warning: Failed to fetch EMA safety updates: {e}")

    return items


def main():
    print("=" * 60)
    print("EU Health News Fetcher")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent.parent
    output_dir = base_dir / "data" / "news"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load synonyms for keyword matching
    print("1. Loading synonyms...")
    synonyms = load_synonyms()
    disease_patterns, drug_patterns = build_keyword_patterns(synonyms)
    print(f"   Loaded {len(disease_patterns)} disease patterns, {len(drug_patterns)} drug patterns")

    # Fetch from all sources
    print()
    print("2. Fetching news from sources...")
    all_items = []

    for source_id, source_config in NEWS_SOURCES.items():
        print(f"   Fetching: {source_config['name']}...")
        if source_config["type"] == "rss":
            items = fetch_rss_feed(source_id, source_config)
        else:
            items = []

        print(f"   Got {len(items)} items")
        all_items.extend(items)

    # Also try EMA safety updates
    print("   Fetching: EMA Safety Updates...")
    safety_items = fetch_ema_safety_updates()
    print(f"   Got {len(safety_items)} items")
    all_items.extend(safety_items)

    # Extract drug/disease mentions
    print()
    print("3. Extracting drug and disease mentions...")
    for item in all_items:
        text = f"{item.title} {item.summary}"
        drugs, diseases = extract_mentions(text, disease_patterns, drug_patterns)
        item.drugs_mentioned = drugs
        item.diseases_mentioned = diseases

    # Filter to items with relevant mentions
    relevant_items = [
        item for item in all_items
        if item.drugs_mentioned or item.diseases_mentioned
    ]
    print(f"   Found {len(relevant_items)} items with drug/disease mentions")

    # Remove duplicates by URL
    seen_urls = set()
    unique_items = []
    for item in all_items:
        if item.url not in seen_urls:
            seen_urls.add(item.url)
            unique_items.append(item)

    # Sort by published date (newest first)
    unique_items.sort(
        key=lambda x: x.published if x.published else "1970-01-01",
        reverse=True
    )

    # Save results
    print()
    print("4. Saving results...")
    output_data = {
        "description": "EU health news aggregated from European sources",
        "fetched_at": datetime.now().isoformat(),
        "total_items": len(unique_items),
        "relevant_items": len(relevant_items),
        "sources": list(NEWS_SOURCES.keys()) + ["ema_safety_updates"],
        "items": [asdict(item) for item in unique_items]
    }

    output_path = output_dir / "eu_health_news.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print(f"   Saved to: {output_path}")

    # Summary
    print()
    print("=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"  Total news items:    {len(unique_items)}")
    print(f"  With drug mentions:  {sum(1 for i in unique_items if i.drugs_mentioned)}")
    print(f"  With disease mentions: {sum(1 for i in unique_items if i.diseases_mentioned)}")
    print()

    # Show top mentioned
    drug_counts = {}
    disease_counts = {}
    for item in unique_items:
        for drug in item.drugs_mentioned:
            drug_counts[drug] = drug_counts.get(drug, 0) + 1
        for disease in item.diseases_mentioned:
            disease_counts[disease] = disease_counts.get(disease, 0) + 1

    if drug_counts:
        print("  Top mentioned drugs:")
        for drug, count in sorted(drug_counts.items(), key=lambda x: -x[1])[:5]:
            print(f"    - {drug}: {count}")

    if disease_counts:
        print()
        print("  Top mentioned diseases:")
        for disease, count in sorted(disease_counts.items(), key=lambda x: -x[1])[:5]:
            print(f"    - {disease}: {count}")

    print()
    print("Done!")


if __name__ == "__main__":
    main()
