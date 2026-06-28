# HO8 Sample 4 — Pricing Calculator MCP Server

## What you'll build
This little server gives Claude two new tools — `get_quote` and `get_commission` — so it can do your pricing and commission math correctly every time. The actual numbers (your plans, prices, discounts, and commission rates) live inside the server, not in Claude's head, so the answers are always consistent and you can update them in one place. It works the moment you connect it — there's nothing to fill in.

## Use it with your Claude.ai subscription
No API key needed — uses your Claude.ai subscription via Claude Desktop.

1. Download Claude Desktop from [claude.ai/download](https://claude.ai/download) and sign in with your Claude.ai account.
2. Install the MCP library: `pip install mcp`
3. (Optional) Make sure everything works: `python test_tool.py` — you should see "All tests passed."
4. Open `claude_desktop_config.json` and change the path in `args` so it points to **your** copy of `server.py` (the full path on your computer).
5. In Claude Desktop, go to **Settings → Developer → Edit Config**, paste in the `pricing-calculator` block from `claude_desktop_config.json`, and save.
6. Quit Claude Desktop completely and reopen it.
7. Try the example prompt below.

## The example prompt
```
Using my pricing tools, quote 10 seats on the pro plan billed annually
(12 months), and then tell me the senior-tier commission on that annual
deal value.
```

## Make it your own
- Edit the `PRICING` dict in `server.py` to use your real plan names, prices, and annual discounts.
- Add a volume discount — e.g. a few percent off when `seats` is above 50.
- Add or rename tiers in `COMMISSION_TIERS` to match how your team is paid.

## Optional — automate it with the API (advanced)
You don't need this for the course. If you later want a standalone script that calls Claude on its own (without Claude Desktop open), that uses the Anthropic API and needs a paid API key, which is separate from your Claude.ai subscription.
