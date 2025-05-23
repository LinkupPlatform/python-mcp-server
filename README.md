# 🌟 Linkup for Claude: Internet Access for Your AI Assistant

Give Claude access to real-time knowledge and premium content. Get rid of Claude's cutoff data and transform Claude's responses with current events, and trusted, premium sources through Linkup's powerful search capability.

<a href="https://glama.ai/mcp/servers/69qbbv8hl9"><img width="380" height="200" src="https://glama.ai/mcp/servers/69qbbv8hl9/badge" alt="mcp-search-linkup MCP server" /></a>

## ⚡️ Get Started in 60 Seconds

1. [Download Linkup for Claude](https://linkup.so/linkup-for-claude)
2. Sign in to Claude Desktop
3. Open Linkup & connect your account
4. Click "*Allow for This Chat*" when prompted

Done! Claude is now supercharged with internet access. 🎉

## 🎭 Experience the Difference

Claude without Linkup stops at April 2024. With Linkup, Claude accesses current events, premium content, and trusted sources to provide up-to-date, accurate information in every conversation.

Ask Claude anything like:
```
"Why did McLaren win F1 championship 2024?" 
"What's the latest breakthrough in cancer research?"
"Can you summarize for me the latest news about the war in Ukraine ?"
"Please help me to find latest data about Global GDP growth rate"
```
## 💎 Premium Features

Linkup gives Claude access to:
- 📰 Premium content
- 🔥 Real-time news and updates

## 💬 From Our Users
```
"My use of Claude was limited by its cutoff date and lack of up-to-date information. This problem is now solved, and I can use Claude for end-to-end tasks"
- François, data engineer in a tech company
```
```
"The work the team has been doing with the MCP is absolutely mind-blowing. Making it accessible to non-developers makes it even more powerful"
- Fred, PM in a tech company
```
```
"With this installer, I was able to catch the importance of both Linkup product and the Claude's MCP"
- Elisa, VC
```

## 🤝 Community & Support

[Discord](https://discord.com/invite/9q9mCYJa86)

[X](https://x.com/Linkup_platform)

[Linkedin](https://www.linkedin.com/company/linkup-platform/)


## 📄 License

MIT License - Innovate freely! 🚀

---

<p align="center">
<strong>✨ Upgrade Claude. Get Linkup. ✨</strong><br>
<a href="https://linkup.so/linkup-for-claude">Download</a> • <a href="https://docs.linkup.so/">Docs</a>
</p>

------------------------

# Linkup MCP Server (Python)

> A Model Context Protocol (MCP) server that provides web search capabilities through Linkup's advanced search API. This server enables AI assistants and development tools to perform intelligent web searches with natural language queries.

 

---

## ✨ Why Linkup?

- 🔍 **Advanced Web Search**: Leverage Linkup's AI-powered search engine for high-quality, relevant results
- 💬 **Natural Language Queries**: Ask questions in plain English - no need for keyword optimization
- 🚀 **Real-time Information**: Access up-to-date web content and current information
- 📚 **Comprehensive Results**: Get detailed search results with source citations
- 🔧 **Easy Integration**: Works with any MCP-compatible client

---

## 🚀 Installation

### Prerequisites

* Python ≥ 3.8 and **uv** 0.6+ (or plain `pip`)
* A Linkup API key (create one for free on [linkup.so](https://linkup.so))

### Install

**Via pip**

```bash
pip install linkup-mcp-server
```

**From source**

```bash
git clone https://github.com/LinkupPlatform/python-mcp-server.git
cd python-mcp-server
pip install -e .
```

## Configuration

Set your Linkup API key as an environment variable:

```bash
export LINKUP_API_KEY="your-api-key-here"
```

Or add it to your shell configuration file (e.g., `.bashrc`, `.zshrc`):

```bash
echo 'export LINKUP_API_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

## 🔌 Using with popular MCP clients

The Linkup MCP server can be used with any MCP-compatible client. Below are setup instructions for popular integrations.

### Claude Desktop

1. Create (or open) your Claude Desktop configuration file:
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
   - Linux: `~/.config/Claude/claude_desktop_config.json`

2. Add the following block, substituting your key:

   ```json
   {
     "mcpServers": {
       "linkup": {
         "command": "uvx",
         "args": ["mcp-search-linkup"],
         "env": { "LINKUP_API_KEY": "YOUR_API_KEY" }
       }
     }
   }
   ```
3. Restart Claude, click the 🛠 hammer icon and allow **Linkup Search** when prompted.
4. You should now see the Linkup search tool available in Claude's tool menu.

### Cursor

1. Open Cursor Settings (Cmd/Ctrl + ,)

2. Navigate to Features > MCP

3. Add a new MCP server with the following configuration:

```json
   {
     "mcpServers": {
       "linkup": {
         "command": "uvx",
         "args": ["mcp-search-linkup"],
         "env": { "LINKUP_API_KEY": "YOUR_API_KEY" }
       }
     }
   }
   ```

4. Save and restart Cursor

5. The Linkup search capability will now be available in your Cursor workspace

> **Tip** – Any other MCP‑compliant client just needs to launch `mcp-search-linkup` (or hit the remote URL) and pass your `LINKUP_API_KEY`.

### Other MCP Clients

For other MCP-compatible clients, use these connection details:

- **Command**: `python -m linkup_mcp_server`
- **Required Environment Variables**: `LINKUP_API_KEY`

Consult your MCP client's documentation for specific configuration instructions.

## Example Queries

The Linkup MCP server excels at answering complex questions and finding specific information:

- "What are the latest developments in quantum computing?"
- "How does the EU AI Act affect startups?"
- "Find recent research on sustainable aviation fuel"
- "What are the current best practices for MCP server development?"


## 🛠 Developing locally

```bash
git clone https://github.com/LinkupPlatform/python-mcp-server.git
cd python-mcp-server
uv pip install -e ".[dev]"
uvx mcp-search-linkup --reload
```

## 🤝 Contributing

Pull requests are welcome! Feel free to open an issue first to discuss what you’d like to change.


## Resources

- [Linkup Documentation](https://docs.linkup.so)
- [MCP Protocol Specification](https://modelcontextprotocol.io)
- [Linkup API Reference](https://docs.linkup.so/api-reference)

## 📣 Community & Support

* Email: [support@linkup.so](mailto:support@linkup.so)
* Discord: [Join our community](https://discord.com/invite/9q9mCYJa86)
* X / Twitter: [@Linkup_platform](https://x.com/Linkup_platform)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



-------------

# Linkup MCP Server

A Model Context Protocol (MCP) server that provides web search capabilities through Linkup's advanced search API. This server enables AI assistants and development tools to perform intelligent web searches with natural language queries.

## Features

- 🔍 **Advanced Web Search**: Leverage Linkup's AI-powered search engine for high-quality, relevant results
- 💬 **Natural Language Queries**: Ask questions in plain English - no need for keyword optimization
- 🚀 **Real-time Information**: Access up-to-date web content and current information
- 📚 **Comprehensive Results**: Get detailed search results with source citations
- 🔧 **Easy Integration**: Works with any MCP-compatible client

## Installation

### Prerequisites

- Python 3.8 or higher
- A Linkup API key (get one at [linkup.so](https://linkup.so))

### Install via pip

```bash
pip install linkup-mcp-server
```

### Install from source

```bash
git clone https://github.com/LinkupPlatform/python-mcp-server.git
cd python-mcp-server
pip install -e .
```

## Configuration

Set your Linkup API key as an environment variable:

```bash
export LINKUP_API_KEY="your-api-key-here"
```

Or add it to your shell configuration file (e.g., `.bashrc`, `.zshrc`):

```bash
echo 'export LINKUP_API_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

## Usage

The Linkup MCP server can be used with any MCP-compatible client. Below are setup instructions for popular integrations.

### Claude Desktop Integration

1. Open your Claude Desktop configuration file:
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
   - Linux: `~/.config/Claude/claude_desktop_config.json`

2. Add the Linkup server configuration:

```json
{
  "mcpServers": {
    "linkup": {
      "command": "python",
      "args": ["-m", "linkup_mcp_server"],
      "env": {
        "LINKUP_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

3. Restart Claude Desktop

4. You should now see the Linkup search tool available in Claude's tool menu

### Cursor Integration

1. Open Cursor Settings (Cmd/Ctrl + ,)

2. Navigate to Features > MCP

3. Add a new MCP server with the following configuration:

```json
{
  "name": "linkup",
  "command": "python",
  "args": ["-m", "linkup_mcp_server"],
  "env": {
    "LINKUP_API_KEY": "your-api-key-here"
  }
}
```

4. Save and restart Cursor

5. The Linkup search capability will now be available in your Cursor workspace

### Other MCP Clients

For other MCP-compatible clients, use these connection details:

- **Command**: `python -m linkup_mcp_server`
- **Required Environment Variables**: `LINKUP_API_KEY`

Consult your MCP client's documentation for specific configuration instructions.

## Example Queries

The Linkup MCP server excels at answering complex questions and finding specific information:

- "What are the latest developments in quantum computing?"
- "How does the EU AI Act affect startups?"
- "Find recent research on sustainable aviation fuel"
- "What are the current best practices for MCP server development?"

## API Usage

When integrated, the server provides a `search_web` tool with the following parameters:

```typescript
{
  "name": "search_web",
  "description": "Search the web with Linkup's advanced search engine",
  "input_schema": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "Your search query in natural language"
      }
    },
    "required": ["query"]
  }
}
```

## Troubleshooting

### Common Issues

1. **"API key not found" error**
   - Ensure your `LINKUP_API_KEY` environment variable is set correctly
   - Check that the API key is valid and active

2. **"Module not found" error**
   - Verify the server is installed: `pip list | grep linkup-mcp-server`
   - Try reinstalling: `pip install --upgrade linkup-mcp-server`

3. **Connection timeouts**
   - Check your internet connection
   - Verify firewall settings allow outbound HTTPS connections

### Debug Mode

Enable debug logging by setting:

```bash
export LINKUP_MCP_DEBUG=true
```

## Development

### Running locally

```bash
# Clone the repository
git clone https://github.com/LinkupPlatform/python-mcp-server.git
cd python-mcp-server

# Install in development mode
pip install -e .

# Run the server
python -m linkup_mcp_server
```

### Running tests

```bash
pytest tests/
```

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Reporting Issues

If you encounter any problems, please [open an issue](https://github.com/LinkupPlatform/python-mcp-server/issues) with:
- Your operating system and Python version
- MCP client you're using
- Complete error messages
- Steps to reproduce the issue

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Resources

- [Linkup Documentation](https://docs.linkup.so)
- [MCP Protocol Specification](https://modelcontextprotocol.io)
- [Linkup API Reference](https://docs.linkup.so/api-reference)

## Support

- 📧 Email: support@linkup.so
- 💬 Discord: [Join our community](https://discord.gg/linkup)
- 🐦 Twitter: [@LinkupPlatform](https://twitter.com/LinkupPlatform)