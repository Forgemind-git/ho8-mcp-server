# HO8 Sample 1 — Customer Lookup MCP Server

## What you'll build
A little "MCP server" that lets Claude look up your customers for you. Instead of you digging through a spreadsheet every time someone asks "what plan is Alice on?", Claude can answer it directly — because this server hands Claude a `lookup_customer` tool that reads your customer list. It comes with 8 example customers so it works the moment you run it; later you just swap in your own list.

## Use it with your Claude.ai subscription
No API key needed — uses your Claude.ai subscription via Claude Desktop.

1. Download **Claude Desktop** (free) from **claude.ai/download** and sign in with your normal Claude.ai account.
2. Install the one dependency: open a terminal in this folder and run `pip install mcp`.
3. (Optional sanity check) Run `python test_tool.py` — you should see "All tests passed".
4. Open **`claude_desktop_config.json`** in this folder. Change the path in `args` to the **full path** to `server.py` on your computer (right-click `server.py` → Copy Path).
5. In Claude Desktop go to **Settings → Developer → Edit Config**, paste in the `customer-lookup` block, and save.
6. **Quit and reopen Claude Desktop.** You'll see a tools/plug icon appear.
7. Use the example prompt below.

## The example prompt
Type this to Claude Desktop once the server is connected:

```
Using my customer-lookup tools, list all my customers, then tell me which ones are NOT on the "active" status and what plan each of them is on.
```

You can also ask things like "Look up customer C003" or "What plan is Alice on?".

## Make it your own
- Open **`sample-data/customers.csv`** and replace the example rows with your real customers (keep the column headers: `id,name,email,plan,status`).
- Add a new column (e.g. `renewal_date`) to the CSV and include it in the `lookup_customer` return value in `server.py`.
- Add a third tool, like `count_by_plan()`, to summarise how many customers are on each plan.

## Optional — automate it with the API (advanced)
You do **not** need this for the course. MCP servers are designed for Claude Desktop and your subscription. If you later want a script to query this data without Claude, that's a separate path that would need an Anthropic API key (which costs money and is not part of the hands-on).
