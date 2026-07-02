# Sample 03 — GitHub Stats MCP Server

**Problem:** You want to ask Claude "Which of these repos is most active?" or "How popular is this library?" without leaving the conversation to open a browser.

**Tool exposed:** `get_repo_stats`

> Get star count, open issue count, and last commit date for any public GitHub repo.

## Use it with your Claude.ai subscription
No API key needed — uses your Claude.ai subscription via Claude Desktop. (The GitHub public API it calls also needs no key.)

1. Download **Claude Desktop** (free) from **claude.ai/download** and sign in with your normal Claude.ai account.
2. Open a terminal in this folder and run `pip install mcp`.
3. Open **`claude_desktop_config.json`** here and set the path in `args` to the full path of `server.py` on your computer.
4. In Claude Desktop, go to **Settings → Developer → Edit Config**, paste in the `github-stats` block, and save.
5. **Quit and reopen Claude Desktop.**
6. Ask Claude: *"Get the GitHub stats for anthropics/anthropic-sdk-python — is it actively maintained?"*

The detailed walkthrough is below.

## What it returns

| Field | Example |
|---|---|
| `repo` | `anthropics/anthropic-sdk-python` |
| `stars` | `4821` |
| `open_issues` | `37` |
| `last_commit_date` | `2024-06-15` |
| `language` | `Python` |

## Quick start

```bash
# 1. Install dependencies
pip install mcp

# 2. Run the server
python server.py
```

No API key required — uses the GitHub public REST API (60 requests/hour unauthenticated).

## Connect to Claude Desktop

Edit `claude_desktop_config.json` with your real path, then add it to `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or `%APPDATA%\Claude\claude_desktop_config.json` (Windows).

```json
{
  "mcpServers": {
    "github-stats": {
      "command": "python",
      "args": ["/ABSOLUTE/PATH/TO/samples/sample-03/server.py"]
    }
  }
}
```

### Optional: raise the rate limit

Add a `GITHUB_TOKEN` env var in `claude_desktop_config.json` to get 5,000 requests/hour instead of 60:

```json
"env": { "GITHUB_TOKEN": "ghp_yourtoken" }
```

Then update `server.py` to read it:
```python
import os
token = os.environ.get("GITHUB_TOKEN")
if token:
    headers["Authorization"] = f"Bearer {token}"
```

## Example prompts

- "Get stats for anthropics/anthropic-sdk-python"
- "How many stars does microsoft/vscode have?"
- "When was the last commit to python/cpython?"

## Test without Claude

```bash
python test_tool.py
```

Makes 4 real API calls — tests valid repos, field types, invalid format, and not-found handling.

## Extending this sample

- Add `GITHUB_TOKEN` support for private repos and higher rate limits
- Add a `list_contributors` tool
- Add a `compare_repos` tool that calls `get_repo_stats` twice and returns the winner by stars
