# RSS MCP Server

A Model Context Protocol (MCP) server for RSS feed management and analysis. This server provides tools to discover, parse, filter, and analyze RSS feeds.

## Features

- **Feed Discovery**: Browse predefined RSS feeds from various sources
- **Feed Parsing**: Parse any RSS feed URL and extract content
- **Content Filtering**: Filter articles by keywords, publication date, or categories
- **Feed Validation**: Check if RSS URLs are accessible and valid
- **Metadata Access**: Get available publications and categories

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd rss-mcp
   ```

2. **Install dependencies**:
   ```bash
   # Using uv (recommended)
   uv sync

   # Or using pip
   pip install -r requirements.txt
   ```

3. **Test the server**:
   ```bash
   # Using uv
   uv run python -m src/server.py

   # Or using python directly
   python -m src/server.py
   ```

## Setup with Claude Desktop

### 1. Configure Claude Desktop

Add the RSS MCP server to your Claude Desktop configuration:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

**Windows**: `%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "rss-feed": {
      "command": "uv",
      "args": ["run", "python", "/absolute/path/to/rss-mcp/src/server.py"],
      "env": {}
    }
  }
}
```

> **Note**: Replace `/absolute/path/to/rss-mcp` with the actual path to your project directory.

### 2. Alternative Setup (without uv)

If you're not using `uv`, you can run with Python directly:

```json
{
  "mcpServers": {
    "rss-feed": {
      "command": "python",
      "args": ["/absolute/path/to/rss-mcp/src/server.py"],
      "env": {}
    }
  }
}
```

### 3. Restart Claude Desktop

After updating the configuration, restart Claude Desktop to load the MCP server.

## Available Tools

The RSS MCP server provides 7 tools:

| Tool | Description |
|------|-------------|
| `get_feeds` | Get all available RSS feeds with optional category filtering |
| `parse_feed` | Parse any RSS feed URL and return structured content |
| `validate_feed_url` | Check if an RSS feed URL is valid and accessible |
| `get_feed_categories` | Get all available categories from predefined feeds |
| `get_publications` | Get all available publication names |
| `get_recent_entries` | Filter feed entries by publication time (last N hours) |
| `filter_entries_by_keywords` | Filter entries by keywords (include/exclude) |

## Sample Prompts

Here are some example prompts you can use with Claude Desktop once the MCP server is configured:

```
Find the top RSS feeds that publish technology / scientific papers using the web and then use those feeds to get me the top 5 emerging technology breakthroughs in the last week. Give me a short summary and cite your sources.
```

```
What are the top trending technology topics this week from various feeds? Cite your sources.
```

```
Get top stories from Google News in the last hour. Cite your sources.
```


## Development

### Project Structure

```
rss-mcp/
├── src/
│   ├── feed/
│   │   ├── base.py          # Core Feed class and parsing logic
│   │   ├── constants.py     # Predefined RSS feeds
│   │   ├── models.py        # Pydantic data models
│   │   └── google.py        # Google News specific implementation
│   ├── tools.py             # MCP business logic functions
│   └── server.py            # MCP server and tool definitions
├── pyproject.toml           # Project dependencies
└── README.md
```

### Adding New Feeds

To add new RSS feeds, edit `src/feed/constants.py`:

```python
Feed(
    publication="New Source",
    category="Technology",
    url="https://newsource.com/rss.xml",
),
```

