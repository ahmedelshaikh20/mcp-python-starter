#!/bin/bash
# Wrapper script to run MCP server with correct Python environment
cd "$(dirname "$0")"
source .venv/bin/activate
python mcp_server.py "$@"