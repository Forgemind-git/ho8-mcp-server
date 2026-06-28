# HO8 Sample 5 — Doc Search MCP Server

## Your task
Your important documents are scattered in a folder and finding the right one wastes time. Build an MCP server that searches them for Claude.

## What you will build
An MCP server that exposes tools to Claude Desktop (no API key — uses your Claude.ai subscription via Claude Desktop)

## Tools to implement
- `search_docs(query) -> [{filename, snippet, path}]`
- `read_doc(filename) -> {content}`

## Data source
Local folder of .txt / .md files

## Setup
1. pip install mcp
2. Add your documents to the sample-data/ folder
3. Fill in the TODO sections in server.py
4. Add your claude_desktop_config.json snippet to Claude Desktop Settings -> Developer
5. Test by asking Claude: "TODO: write a test question"

## Required
Claude Desktop (free download at claude.ai/download) + your Claude.ai subscription
