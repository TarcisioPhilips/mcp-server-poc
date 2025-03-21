# server.py
from mcp.server.fastmcp import FastMCP
import asyncio
from crawl4ai import AsyncWebCrawler

# Create an MCP server
mcp = FastMCP(
    name="first-mcp",
)

# Add a web crawling tool
@mcp.tool()
async def crawl_web(url: str) -> str:
    """Crawl a website and return its content as markdown"""
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=url)
        return result.markdown

# Run the server
if __name__ == "__main__":
    try:
        print("Starting server...")
        mcp.run(transport="stdio")
    except KeyboardInterrupt:
        print("Server interrupted by user")
    except Exception as e:
        print(f"Server error: {e}")
        raise e
