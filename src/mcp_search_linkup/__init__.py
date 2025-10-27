import asyncio
import warnings

from . import server

warnings.warn(
    "mcp-search-linkup is deprecated and no longer maintained. "
    "Please use the TypeScript/Node.js version instead: "
    "https://github.com/LinkupPlatform/linkup-mcp-server",
    DeprecationWarning,
    stacklevel=2,
)


def main() -> None:
    asyncio.run(server.main())


__all__ = ["main", "server"]
