# mcp-python-starter

A template project for learning how to build **MCP (Model Context Protocol) servers and clients** with Python. It includes both a working server and client so you can see how they interact end-to-end — but in a real project, you'd typically build **either** a server **or** a client, not both.

## What is MCP?

[MCP (Model Context Protocol)](https://modelcontextprotocol.io) is an open protocol that lets AI models interact with external tools, data sources, and services in a standardized way. It defines:

- **Tools** — functions the AI can call
- **Resources** — data the AI can read
- **Prompts** — reusable prompt templates

## What this template covers

| File | Role |
|------|------|
| `mcp_server.py` | Example MCP server with tools, resources, and prompts |
| `mcp_client.py` | Example MCP client that connects over stdio |
| `core/tools.py` | Tool discovery and execution |
| `core/chat.py` | Base chat loop with tool use |
| `core/cli_chat.py` | Extended chat with document mentions and commands |
| `core/cli.py` | Interactive CLI with tab completion |
| `main.py` | Entry point wiring everything together |

## When to build each

**Build a server** when you want to expose tools/resources/prompts to AI agents or clients (e.g., database access, file operations, internal APIs).

**Build a client** when you want to consume tools from existing MCP servers (e.g., chat apps, agents, automation workflows).

## Prerequisites

- Python 3.10+
- Anthropic API key — get one from [console.anthropic.com](https://console.anthropic.com/)
- [uv](https://github.com/astral-sh/uv) (recommended)

## Usage

### Chat

Type any message and press Enter to chat with Claude:

```
> What are the financials looking like?
```

### Mention documents with @

Use `@` followed by a document ID to include its content in your query. Tab completion is supported:

```
> Summarize @deposition.md
> Compare @financials.docx and @outlook.pdf
```

Available documents: `deposition.md`, `report.pdf`, `financials.docx`, `outlook.pdf`, `plan.md`, `spec.txt`

### Run prompts with /

Use `/` to trigger MCP prompts. Tab completion is supported:

```
> /format deposition.md
```

## Learning path

1. **Explore the server** — Open `mcp_server.py` and see how tools, resources, and prompts are defined with `FastMCP`
2. **Explore the client** — Open `mcp_client.py` and see how it connects to the server and calls tools
3. **Add a tool** — Add a new `@mcp.tool()` to `mcp_server.py` and ask Claude to use it
4. **Add a prompt** — Add a new `@mcp.prompt()` and trigger it from the CLI with `/your_prompt doc_id`
5. **Add a document** — Add a new entry to the `docs` dict in `mcp_server.py`

## Dependencies

- [anthropic](https://github.com/anthropic-ai/anthropic-sdk-python) — Claude API
- [mcp](https://github.com/modelcontextprotocol/python-sdk) — MCP Python SDK
- [prompt-toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit) — Interactive CLI
- [python-dotenv](https://github.com/theskumar/python-dotenv) — Environment variable loading
