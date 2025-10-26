from mcp.server.fastmcp import FastMCP
from typing import Optional
from src.tools import (
    get_feeds_for_mcp,
    parse_feed_for_mcp,
    validate_feed_url_for_mcp,
    get_feed_categories_for_mcp,
    get_publications_for_mcp,
    get_recent_entries_for_mcp,
    filter_entries_by_keywords_for_mcp,
)

mcp = FastMCP("rss-feed")


@mcp.tool()
def get_feeds(category: Optional[str] = None) -> list[dict]:
    """
    Get all RSS feeds with optional category filtering.

    Args:
        category: Optional category to filter feeds by. Valid categories include:
                 "Top Stories", "World", "NY", "US", "Politics", "Technology",
                 "Science", "Business", "Economy"

    Returns:
        List of feed dictionaries containing publication, category, url, and frequency
    """
    return get_feeds_for_mcp(category)


@mcp.tool()
def parse_feed(url: str, max_chars_per_entry: int = 200) -> dict:
    """
    Parse an RSS feed from a given URL and return its content.

    Args:
        url: The RSS feed URL to parse
        max_chars_per_entry: An optional parameter for the maximum number of characters to return per feed entry. This is to make sure we don't exceed the context window of LLMs.

    Returns:
        Dictionary containing the parsed feed content including entries, metadata, etc.
    """
    return parse_feed_for_mcp(url, max_chars_per_entry)


@mcp.tool()
def validate_feed_url(url: str) -> dict:
    """Check if RSS feed URL is valid and accessible"""
    return validate_feed_url_for_mcp(url)


@mcp.tool()
def get_feed_categories() -> list[str]:
    """Get all available categories from COMMON_FEEDS"""
    return get_feed_categories_for_mcp()


@mcp.tool()
def get_publications() -> list[str]:
    """Get all available publication names from COMMON_FEEDS"""
    return get_publications_for_mcp()


@mcp.tool()
def get_recent_entries(url: str, hours: int = 24, max_chars_per_entry: int = 200) -> list[dict]:
    """Get only entries published within the last N hours"""
    return get_recent_entries_for_mcp(url, hours, max_chars_per_entry)


@mcp.tool()
def filter_entries_by_keywords(
    url: str, keywords: list[str], exclude: bool = False, max_chars_per_entry: int = 200
) -> list[dict]:
    """Filter entries containing (or excluding) specific keywords"""
    return filter_entries_by_keywords_for_mcp(url, keywords, exclude, max_chars_per_entry)


def main():
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
