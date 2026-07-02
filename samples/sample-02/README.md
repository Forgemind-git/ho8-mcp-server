# Sample 02 — Customer Lookup MCP Server

**Problem:** Support agents waste time copy-pasting between tools. Give Claude direct access to your customer database so it can answer "Who is alice@acmecorp.com and do they have open tickets?" in one step.

**Tool exposed:** `lookup_customer`

> Look up a customer by email or ID from a local JSON database.

## Use it with your Claude.ai subscription
No API key needed — uses your Claude.ai subscription via Claude Desktop.

1. Download **Claude Desktop** (free) from **claude.ai/download** and sign in with your normal Claude.ai account.
2. Open a terminal in this folder and run `pip install mcp`.
3. Open **`claude_desktop_config.json`** here and set the path in `args` to the full path of `server.py` on your computer.
4. In Claude Desktop, go to **Settings → Developer → Edit Config**, paste in the `customer-lookup` block, and save.
5. **Quit and reopen Claude Desktop.**
6. Ask Claude: *"Look up customer C001 and tell me their plan and how many open tickets they have."*

The detailed walkthrough is below.

## What it returns

| Field | Example |
|---|---|
| `customer_id` | `C001` |
| `name` | `Alice Johnson` |
| `email` | `alice@acmecorp.com` |
| `plan` | `pro` |
| `created_at` | `2023-04-12` |
| `open_tickets` | `2` |

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
    "customer-lookup": {
      "command": "python",
      "args": ["/ABSOLUTE/PATH/TO/samples/sample-02/server.py"]
    }
  }
}
```

Replace `/ABSOLUTE/PATH/TO/` with the real path on your machine, then restart Claude Desktop.

## Example prompts

- "Look up customer C003"
- "Is carol@enterprise.com on the enterprise plan?"
- "How many open tickets does David Lee (C004) have?"

## Test without Claude

```bash
python test_tool.py
```

Runs 5 assertions — lookup by ID, by email, open tickets count, and two not-found cases.

## Extending this sample

- Replace `CUSTOMERS` dict with a real DB query (`psycopg2`, `sqlite3`, etc.)
- Add more tools: `create_customer`, `update_plan`, `list_open_tickets`
- Add an `EMAIL_DOMAIN_INDEX` to look up all customers at a company
