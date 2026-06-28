# HO8 Sample 1 — Customer Lookup MCP Server

## Your task
Your team keeps customer data in a sheet or database and re-answers the same lookups all day. Build an MCP server that exposes a customer_lookup tool to Claude Desktop.

## What you will build
An MCP server that exposes tools to Claude Desktop (no API key — uses your Claude.ai subscription via Claude Desktop)

## Tools to implement
- `lookup_customer(id_or_name) -> {name, email, plan, status}`
- `list_customers() -> [{id, name, plan}]`

## Data source
CSV file or SQLite (sample data provided)

## Setup
1. pip install mcp
2. Fill in the TODO sections in server.py
3. Add your claude_desktop_config.json snippet to Claude Desktop Settings -> Developer
4. Test by asking Claude: "TODO: write a test question"

## Required
Claude Desktop (free download at claude.ai/download) + your Claude.ai subscription
