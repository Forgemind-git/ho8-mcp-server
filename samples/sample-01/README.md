# HO8 Sample 1 — HO7 Connection MCP Server

## What you'll build
A little "MCP server" that connects the solution you already built in HO7 (your mid-course capstone) to Claude — so Claude can act on it live. Instead of copy-pasting from your HO7 project, Claude can answer straight from it, because this server hands Claude a `query_ho7` tool that reads your HO7 data. It comes with example rows so it works the moment you run it; later you swap in your real HO7 project's data.

## Use it with your Claude.ai subscription
No API key needed — uses your Claude.ai subscription via Claude Desktop.

1. Download **Claude Desktop** (free) from **claude.ai/download** and sign in with your normal Claude.ai account.
2. Install the one dependency: open a terminal in this folder and run `pip install mcp`.
3. (Optional sanity check) Run `python test_tool.py` — you should see "All tests passed".
4. Open **`claude_desktop_config.json`** in this folder. Change the path in `args` to the **full path** to `server.py` on your computer (right-click `server.py` → Copy Path).
5. In Claude Desktop go to **Settings → Developer → Edit Config**, paste in the `ho7-connection` block, and save.
6. **Quit and reopen Claude Desktop.** You'll see a tools/plug icon appear.
7. Use the example prompt below.

## The example prompt
Type this to Claude Desktop once the server is connected:

```
Using my HO7 tools, list everything in my HO7 project, then tell me which items are still in progress or to do and summarise what's left.
```

You can also ask things like "Query my HO7 project for P001" or "Search my HO7 solution for anything about leads".

## Make it your own — connect your real HO7 project
- Open **`sample-data/ho7_items.csv`** and replace the example rows with data from your real HO7 project (keep the column headers: `id,title,status,notes`).
- Better still, edit `server.py` so `query_ho7` reads your HO7 project directly — its database (`sqlite3`, `psycopg2`), its API, or its JSON/CSV export.
- Add a third tool that takes an **action** in your HO7 app (e.g. mark an item done), so Claude can do, not just read.

## Why this one first
This is the lead sample because it ties your two hands-on together: your MCP server (HO8) exposing your capstone (HO7). Success looks like a clip of Claude calling `query_ho7` and returning a real result from your HO7 solution — not a guess.

## Optional — automate it with the API (advanced)
You do **not** need this for the course. MCP servers are designed for Claude Desktop and your subscription. If you later want a script to query this data without Claude, that's a separate path that would need an Anthropic API key (which costs money and is not part of the hands-on).
