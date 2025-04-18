import asyncio
import logging

import mcp.server.stdio
import mcp.types as types
from linkup import LinkupClient
from mcp.server import NotificationOptions, Server
from mcp.server.models import InitializationOptions

server = Server("mcp-search-linkup")
logger = logging.getLogger("mcp-search-linkup")
logger.setLevel(logging.INFO)


@server.set_logging_level()  # type: ignore
async def set_logging_level(level: types.LoggingLevel) -> types.EmptyResult:
    logger.setLevel(level.upper())
    await server.request_context.session.send_log_message(
        level="info",
        data=f"Log level set to {level}",
        logger="mcp-search-linkup",
    )
    return types.EmptyResult()


@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """List available search tools."""
    return [
        types.Tool(
            name="search-web",
            description="Performs an online search using Linkup search engine and retrieves the "
            "top results as a string. This function is useful for accessing real-time information, "
            "including news, articles, and other relevant web content.",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query to perform.",
                    },
                    "depth": {
                        "type": "string",
                        "description": "The search depth to perform. Use 'standard' for "
                        "straightforward queries with likely direct answers (e.g., facts, "
                        "definitions, simple explanations). Use 'deep' for: 1) complex queries "
                        "requiring comprehensive analysis or information synthesis, 2) queries "
                        "containing uncommon terms, specialized jargon, or abbreviations that may "
                        "need additional context, or 3) questions likely requiring up-to-date or "
                        "specialized web search results to answer effectively.",
                        "enum": ["standard", "deep"],
                    },
                },
                "required": ["query", "depth"],
            },
        )
    ]


@server.call_tool()
async def handle_call_tool(
    name: str,
    arguments: dict | None,
) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle search tool execution requests."""
    if name != "search-web":
        raise ValueError(f"Unknown tool: {name}")
    if not arguments:
        raise ValueError("Missing arguments")

    query = arguments.get("query")
    if not query:
        raise ValueError("Missing query")
    depth = arguments.get("depth")
    if not depth:
        raise ValueError("Missing depth")

    client = LinkupClient()
    search_response = client.search(
        query=query,
        depth=depth,
        output_type="searchResults",
    )

    return [
        types.TextContent(
            type="text",
            text=str(search_response),
        )
    ]


async def main() -> None:
    """Run the server using stdin/stdout streams."""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="mcp-search-linkup",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )


if __name__ == "__main__":
    asyncio.run(main())
