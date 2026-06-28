# HO8 Sample 3 — Task Manager MCP Server

## Your task
Your tasks live in a tracker and you context-switch constantly. Build an MCP server that lets Claude read and write your task list.

## What you will build
An MCP server that exposes tools to Claude Desktop (no API key — uses your Claude.ai subscription via Claude Desktop)

## Tools to implement
- `list_tasks(status?) -> [{id, title, status}]`
- `add_task(title, due?) -> {id}`
- `complete_task(id) -> ok`

## Data source
SQLite local file

## Setup
1. pip install mcp
2. Fill in the TODO sections in server.py
3. Add your claude_desktop_config.json snippet to Claude Desktop Settings -> Developer
4. Test by asking Claude: "TODO: write a test question"

## Required
Claude Desktop (free download at claude.ai/download) + your Claude.ai subscription
