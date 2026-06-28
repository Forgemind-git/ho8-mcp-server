# HO8 Sample 4 — Pricing Calculator MCP Server

## Your task
Sales reps keep pinging you for the same pricing numbers. Build an MCP server exposing your pricing and commission calculator.

## What you will build
An MCP server that exposes tools to Claude Desktop (no API key — uses your Claude.ai subscription via Claude Desktop)

## Tools to implement
- `get_quote(seats, plan, term_months) -> {monthly, annual, discount}`
- `get_commission(deal_value, tier) -> {amount, pct}`

## Data source
Hardcoded pricing table in Python

## Setup
1. pip install mcp
2. Fill in the TODO sections in server.py
3. Add your claude_desktop_config.json snippet to Claude Desktop Settings -> Developer
4. Test by asking Claude: "TODO: write a test question"

## Required
Claude Desktop (free download at claude.ai/download) + your Claude.ai subscription
