# Sample 04 — Pricing Calculator MCP Server

**Problem:** Sales and support teams ask "how much would 15 Pro seats on an annual plan cost?" dozens of times a day. Give Claude a live pricing calculator so it can answer instantly and accurately.

**Tool exposed:** `calculate_quote`

> Calculate a product quote given plan, seats, and billing period.

## Use it with your Claude.ai subscription
No API key needed — uses your Claude.ai subscription via Claude Desktop.

1. Download **Claude Desktop** (free) from **claude.ai/download** and sign in with your normal Claude.ai account.
2. Open a terminal in this folder and run `pip install mcp`.
3. Open **`claude_desktop_config.json`** here and set the path in `args` to the full path of `server.py` on your computer.
4. In Claude Desktop, go to **Settings → Developer → Edit Config**, paste in the `pricing-calculator` block, and save.
5. **Quit and reopen Claude Desktop.**
6. Ask Claude: *"Quote 10 Pro seats on annual billing, and tell me how much we save versus paying monthly."*

The detailed walkthrough is below.

## Plans & pricing

| Plan | Per seat/month | Annual discount | Max seats |
|---|---|---|---|
| Starter | $12 | — | 5 |
| Pro | $29 | 20% off | 50 |
| Enterprise | $79 | 25% off | 10,000 |

## What it returns

| Field | Example |
|---|---|
| `plan` | `Pro` |
| `seats` | `10` |
| `billing` | `annual` |
| `unit_price_per_seat_per_month` | `23.20` |
| `subtotal` | `2784.00` |
| `discount_pct` | `20` |
| `discount_amount` | `696.00` |
| `total` | `2784.00` |
| `savings_vs_monthly` | `696.00` |
| `billing_note` | `Billed as $2784.00/year` |

## Quick start

```bash
pip install mcp
python server.py
```

## Connect to Claude Desktop

```json
{
  "mcpServers": {
    "pricing-calculator": {
      "command": "python",
      "args": ["/ABSOLUTE/PATH/TO/samples/sample-04/server.py"]
    }
  }
}
```

## Example prompts

- "Calculate a quote for 10 Pro seats on annual billing"
- "How much would 3 starter seats cost per month?"
- "What's the savings on 25 enterprise seats if we go annual?"

## Test without Claude

```bash
python test_tool.py
```

Runs 7 assertions: monthly/annual pricing math, discounts, edge cases, and case-insensitive inputs.

## Extending this sample

- Pull pricing from a database or external pricing API
- Add currency conversion
- Add a `compare_plans` tool that returns all three plans side by side
- Add volume discounts (e.g. 5% extra off for 100+ seats)
