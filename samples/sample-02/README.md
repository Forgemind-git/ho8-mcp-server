# HO8 Sample 2 — API Wrapper MCP Server

## Your task
You rely on a public API but copy-pasting output into chat is clunky. Build an MCP server that wraps a free public API as a Claude tool.

## What you will build
An MCP server that exposes tools to Claude Desktop (no API key — uses your Claude.ai subscription via Claude Desktop)

## Tools to implement
- `get_weather(city) -> {temp, condition, humidity}`
- `get_forecast(city, days) -> [{date, high, low}]`

## Data source
Open-Meteo free weather API (no key)

## Setup
1. pip install mcp
2. Fill in the TODO sections in server.py
3. Add your claude_desktop_config.json snippet to Claude Desktop Settings -> Developer
4. Test by asking Claude: "TODO: write a test question"

## Required
Claude Desktop (free download at claude.ai/download) + your Claude.ai subscription
