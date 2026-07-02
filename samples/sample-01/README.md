# Sample 01 — HO7 Connection MCP Server

**Problem:** You already built a solution in HO7 (your mid-course capstone). Now let Claude act on it live. This server exposes your HO7 project's data or actions as a real MCP tool, so Claude can answer questions or take actions straight from it — your two hands-on connected end-to-end.

**Tool exposed:** `query_ho7`

> Query the solution you built in HO7 (your mid-course capstone).

## Use it with your Claude.ai subscription
No API key needed — uses your Claude.ai subscription via Claude Desktop.

1. Download **Claude Desktop** (free) from **claude.ai/download** and sign in with your normal Claude.ai account.
2. Open a terminal in this folder and run `pip install mcp`.
3. Open **`claude_desktop_config.json`** here and set the path in `args` to the full path of `server.py` on your computer.
4. In Claude Desktop, go to **Settings → Developer → Edit Config**, paste in the `ho7-connection` block, and save.
5. **Quit and reopen Claude Desktop.**
6. Ask Claude: *"Use the HO7 tool to give me a summary of my project, then tell me what's still to do."*

The detailed walkthrough is below.

## Make it yours

The `HO7_DATA` dictionary in `server.py` is placeholder data standing in for your HO7 solution. Replace it with a **real** query into your own HO7 project:

- read rows from your HO7 database (`sqlite3`, `psycopg2`, …)
- call your HO7 project's API, or read its JSON/CSV export
- trigger an action your HO7 app already exposes

Keep the `query_ho7` signature the same and Claude will call it exactly as-is.

## Quick start

```bash
# 1. Install dependencies
pip install mcp

# 2. Run the server (stdio mode — used by Claude Desktop)
python server.py
```

## Connect to Claude Desktop

Add to your `claude_desktop_config.json` (see `claude_desktop_config.json` in this folder for the snippet):

```json
{
  "mcpServers": {
    "ho7-connection": {
      "command": "python",
      "args": ["/ABSOLUTE/PATH/TO/samples/sample-01/server.py"]
    }
  }
}
```

Replace `/ABSOLUTE/PATH/TO/` with the real path on your machine, then restart Claude Desktop.

## Example prompts

- "Give me a summary of my HO7 project."
- "What's the status of P002?"
- "Search my HO7 solution for anything about leads."

## Test without Claude

```bash
python test_tool.py
```

Runs 4 assertions — summary, lookup by id, keyword search, and a no-match case.

## Success looks like

A clip of Claude calling `query_ho7` and returning a **real result from your HO7 solution**, not a guess — proving your MCP server (HO8) and your capstone (HO7) now work together end-to-end.
