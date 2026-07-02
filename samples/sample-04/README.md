# HO8 Sample 4 — Task Manager MCP Server

## What you'll build
This gives Claude a couple of simple tools to read and add to your to-do list, which is stored in a small local file (SQLite) on your own computer. Once it's connected, you can say things like "add buy milk to my tasks" or "what's still open?" right inside Claude, and it just works. To get you started, your list comes pre-loaded with 3 example tasks.

## Use it with your Claude.ai subscription
No API key needed — uses your Claude.ai subscription via Claude Desktop.

1. Download Claude Desktop from [claude.ai/download](https://claude.ai/download) and sign in with your Claude.ai account.
2. Install the one library this needs: `pip install mcp`
3. (Optional) Make sure everything works by running the included test: `python test_tool.py` — you should see "All tests passed."
4. Open `claude_desktop_config.json` and change the path so it points to *your* copy of `server.py` (replace `/Users/you/...` with the real location on your computer).
5. In Claude Desktop, go to **Settings → Developer → Edit Config**, paste in the `task-manager` block from `claude_desktop_config.json`, and save.
6. Fully quit Claude Desktop and reopen it (this is what loads your new tools).
7. Try the example prompt below.

## The example prompt
```
Using my task-manager tools, show me my open tasks, then add a new task
'Prepare slides for Monday standup' due 2026-07-03, and confirm it was
added by listing my tasks again.
```

## Make it your own
- Change the 3 seeded example tasks in `server.py` (look inside `_init_db()`) to your own real tasks.
- Add a `delete_task` tool so you can remove tasks too, not just complete them.
- Add a `priority` column (e.g. high/medium/low) so Claude can sort or filter by it.

## Optional — automate it with the API (advanced)
You don't need this for the course. The setup above runs entirely through your Claude.ai subscription. If you later wanted a standalone script to call these tools without Claude Desktop open, that would require a separate, paid Anthropic API key — which is different from your subscription.
