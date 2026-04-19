#!/usr/bin/env python3
"""
Google News EU Health Fetcher

Fetches health news from Google News for multiple European countries.
Outputs to data/news/google_news_eu.json
"""

import json
import hashlib
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from xml.etree import ElementTree as ET

# Project root
PROJECT_ROOT = Path(__file__).parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "news"

# Google News Health RSS for European countries
# Topic ID for Health: CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JYcG9MVlJYS0FBUAE
# (This is the base64 encoded topic path for health news)

GOOGLE_NEWS_FEEDS = {
    "google_uk": {
        "name": "Google News UK Health",
        "url": "https://news.google.com/rss/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JYcG9MVlJYS0FBUAE?hl=en-GB&gl=GB&ceid=GB:en",
        "language": "en"
    },
    "google_de": {
        "name": "Google News Germany Health",
        "url": "https://news.google.com/rss/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JYcG9MVlJYS0FBUAE?hl=de&gl=DE&ceid=DE:de",
        "language": "de"
    },
    "google_fr": {
        "name": "Google News France Health",
        "url": "https://news.google.com/rss/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JYcG9MVlJYS0FBUAE?hl=fr&gl=FR&ceid=FR:fr",
        "language": "fr"
    },
    "google_es": {
        "name": "Google News Spain Health",
        "url": "https://news.google.com/rss/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JYcG9MVlJYS0FBUAE?hl=es&gl=ES&ceid=ES:es",
        "language": "es"
    },
    "google_it": {
        "name": "Google News Italy Health",
        "url": "https://news.google.com/rss/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JYcG9MVlJYS0FBUAE?hl=it&gl=IT&ceid=IT:it",
        "language": "it"
    },
}

# Additional health-specific RSS feeds
HEALTH_RSS_FEEDS = {
    "medscape_eu": {
        "name": "Medscape",
        "url": "https://www.medscape.com/cx/rssfeeds/2212.xml",
        "language": "en"
    },
    "reuters_health": {
        "name": "Reuters Health",
        "url": "https://www.reutersagency.com/feed/?best-topics=health&post_type=best",
        "language": "en"
    },
}


def generate_id(title: str, link: str) -> str:
    """Generate news ID based on title and link hash"""
    content = f"{title}:{link}"
    return hashlib.sha256(content.encode()).hexdigest()[:12]


def clean_html(text: str) -> str:
    """Remove HTML tags from text"""
    if not text:
        return ""
    clean = re.sub(r'<[^>]+>', '', text)
    clean = re.sub(r'\s+', ' ', clean).strip()
    return clean[:500]


def parse_pub_date(pub_date_str: str) -> str:
    """Parse publication date to ISO format"""
    if not pub_date_str:
        return datetime.now(timezone.utc).isoformat()

    # Try common date formats
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
    """Extract source name from RSS entry"""
    # Google News includes source in <source> tag
    source_elem = entry_element.find("source")
    if source_elem is not None and source_elem.text:
        return source_elem.text.strip()
    return default


def fetch_rss(url: str, source_key: str, source_name: str) -> list:
    """Fetch and parse an RSS feed"""
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

                # Extract actual source from Google News
                actual_source = extract_source_name(item, source_name)

                if title and link:
                    items.append({
                        "id": generate_id(title, link),
                        "title": clean_html(title),
                        "published": parse_pub_date(pub_date),
                        "summary": clean_html(description),
                        "sources": [{
                            "name": actual_source,
                            "link": link
                        }],
                        "feed_source": source_key
                    })

    except (URLError, HTTPError, ET.ParseError) as e:
        print(f"  Warning: Failed to fetch {source_name}: {e}")

    return items


def main():
    print("Fetching European health news from Google News...")

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    all_items = []

    # Fetch from Google News feeds
    for source_key, config in GOOGLE_NEWS_FEEDS.items():
        print(f"Fetching {config['name']}...")
        items = fetch_rss(config["url"], source_key, config["name"])
        print(f"  Found {len(items)} items")
        all_items.extend(items)

    # Fetch from health-specific feeds
    for source_key, config in HEALTH_RSS_FEEDS.items():
        print(f"Fetching {config['name']}...")
        items = fetch_rss(config["url"], source_key, config["name"])
        print(f"  Found {len(items)} items")
        all_items.extend(items)

    # Output
    output = {
        "source": "google_news_eu",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "count": len(all_items),
        "feeds": list(GOOGLE_NEWS_FEEDS.keys()) + list(HEALTH_RSS_FEEDS.keys()),
        "news": all_items
    }

    output_path = DATA_DIR / "google_news_eu.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\nOutput: {output_path}")
    print(f"  Total items: {len(all_items)}")

    # Show sample
    if all_items:
        print("\nSample news:")
        for item in all_items[:5]:
            src = item["sources"][0]["name"] if item["sources"] else "Unknown"
            print(f"  - [{src}] {item['title'][:60]}...")


if __name__ == "__main__":
    main()
