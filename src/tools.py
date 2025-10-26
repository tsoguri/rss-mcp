from datetime import datetime, timedelta
from typing import Optional

from src.feed.base import Feed
from src.feed.constants import COMMON_FEEDS


def get_feeds_for_mcp(category: Optional[str] = None) -> list[dict]:
    """Get all RSS feeds with optional category filtering"""
    feeds = COMMON_FEEDS

    if category:
        feeds = [feed for feed in feeds if feed.category == category]

    return [
        {
            "publication": feed.publication,
            "category": feed.category,
            "url": feed.url,
            "frequency": feed.frequency,
            "name": feed.name,
        }
        for feed in feeds
    ]


def parse_feed_for_mcp(url: str, max_chars_per_entry: int = 200) -> dict:
    """Parse an RSS feed from a given URL and return its content"""
    feed = Feed(publication="Custom", url=url)
    content = feed.parse_feed(max_chars_per_entry)
    return content.model_dump()


def validate_feed_url_for_mcp(url: str) -> dict:
    """Check if RSS feed URL is valid and accessible"""
    try:
        feed = Feed(publication="Test", url=url)
        content = feed.parse_feed()
        return {
            "valid": True,
            "title": content.title,
            "entry_count": len(content.entries) if content.entries else 0,
            "last_updated": (
                content.updated_datetime.isoformat()
                if content.updated_datetime
                else None
            ),
        }
    except Exception as e:
        return {"valid": False, "error": str(e)}


def get_feed_categories_for_mcp() -> list[str]:
    """Get all available categories from COMMON_FEEDS"""
    categories = set()
    for feed in COMMON_FEEDS:
        if feed.category:
            categories.add(feed.category)
    return sorted(list(categories))


def get_publications_for_mcp() -> list[str]:
    """Get all available publication names from COMMON_FEEDS"""
    publications = set()
    for feed in COMMON_FEEDS:
        publications.add(feed.publication)
    return sorted(list(publications))


def get_recent_entries_for_mcp(
    url: str, hours: int = 24, max_chars_per_entry: int = 200
) -> list[dict]:
    """Get only entries published within the last N hours"""
    feed = Feed(publication="Custom", url=url)
    content = feed.parse_feed(max_chars_per_entry)

    if not content.entries:
        return []

    cutoff_time = datetime.now() - timedelta(hours=hours)
    recent_entries = []

    for entry in content.entries:
        if entry.published_datetime and entry.published_datetime >= cutoff_time:
            recent_entries.append(entry.model_dump())

    return recent_entries


def filter_entries_by_keywords_for_mcp(
    url: str, keywords: list[str], exclude: bool = False, max_chars_per_entry: int = 200
) -> list[dict]:
    """Filter entries containing (or excluding) specific keywords"""
    feed = Feed(publication="Custom", url=url)
    content = feed.parse_feed(max_chars_per_entry)

    if not content.entries:
        return []

    filtered_entries = []
    keywords_lower = [k.lower() for k in keywords]

    for entry in content.entries:
        text_to_search = []
        if entry.title:
            text_to_search.append(entry.title.lower())
        if entry.summary:
            text_to_search.append(entry.summary.lower())
        if entry.description:
            text_to_search.append(entry.description.lower())

        search_text = " ".join(text_to_search)
        has_keyword = any(keyword in search_text for keyword in keywords_lower)
        if has_keyword != exclude:
            filtered_entries.append(entry.model_dump())

    return filtered_entries
