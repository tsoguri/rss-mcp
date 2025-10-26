from src.feed.base import Feed
from src.feed.google import GoogleFeed

COMMON_FEEDS: list[Feed] = [
    Feed(
        publication="NY Times",
        category="Technology",
        url="https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
    ),
    Feed(
        publication="WSJ",
        category="Technology",
        url="https://feeds.content.dowjones.io/public/rss/RSSWSJD",
    ),
    Feed(
        publication="Nature",
        category="Science",
        url="http://www.nature.com/nature/current_issue/rss",
    ),
    Feed(
        publication="Science",
        category="Science",
        url="http://www.sciencemag.org/rss/current.xml",
    ),
    Feed(
        publication="The Verge",
        category="Technology",
        url="https://www.theverge.com/rss/index.xml",
    ),
    Feed(
        publication="TechCrunch",
        category="Technology",
        url="https://techcrunch.com/feed/",
    ),
    Feed(
        publication="TLDR Tech",
        category="Technology",
        url="https://tldr.tech",
    ),
    GoogleFeed(
        publication="Google News",
        url="https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en",
    ),
]
