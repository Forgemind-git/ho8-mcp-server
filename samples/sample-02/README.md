# HO8 Sample 2 — Weather MCP Server

## What you'll build
A little "MCP server" that gives Claude a live `get_weather` and `get_forecast` tool, backed by the free Open-Meteo API. Instead of guessing or telling you it doesn't have real-time data, Claude can fetch the actual current weather and a multi-day forecast for any city you name. It works the moment you run it — no signup, no API key, nothing to pay for.

## Use it with your Claude.ai subscription
No API key needed — uses your Claude.ai subscription via Claude Desktop.

1. Download **Claude Desktop** (free) from **claude.ai/download** and sign in with your normal Claude.ai account.
2. Install the one dependency: open a terminal in this folder and run `pip install mcp`.
3. (Optional sanity check) Run `python test_tool.py` — you should see real weather print out and "All tests passed".
4. Open **`claude_desktop_config.json`** in this folder. Change the path in `args` to the **full path** to `server.py` on your computer (right-click `server.py` → Copy Path).
5. In Claude Desktop go to **Settings → Developer → Edit Config**, paste in the `weather` block, and save.
6. **Quit and reopen Claude Desktop.** You'll see a tools/plug icon appear.
7. Use the example prompt below.

## The example prompt
Type this to Claude Desktop once the server is connected:

```
Using my weather tools, what's the weather right now in Lisbon, and give me the 3-day forecast — should I pack a raincoat?
```

You can also ask things like "What's the weather in Mumbai?" or "Give me a 5-day forecast for Tokyo."

## Make it your own
- Change the default in `get_forecast(city, days=3)` to however many days you usually want.
- Add a new tool, like `compare_cities(city_a, city_b)`, that calls `get_weather` twice and tells you which is warmer.
- Browse the Open-Meteo docs to pull in more data (wind, UV index, sunrise/sunset): [open-meteo.com/en/docs](https://open-meteo.com/en/docs).

## Optional — automate it with the API (advanced)
You do **not** need this for the course. MCP servers are designed for Claude Desktop and your subscription — that's the whole hands-on. If you later want a standalone script that calls Claude without Claude Desktop, that's a separate path that needs a paid Anthropic API key (which is separate from your Claude.ai subscription and costs money).
