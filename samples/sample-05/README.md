# Sample 05 — Document Search MCP Server

**Problem:** You have a folder of internal docs, README files, or knowledge-base articles, and you want Claude to search them for you — "What does our docs say about rate limits?" — without having to copy-paste file contents.

**Tool exposed:** `search_docs`

> Search a folder of `.txt` and `.md` files for matching passages.

## Use it with your Claude.ai subscription
No API key needed — uses your Claude.ai subscription via Claude Desktop.

1. Download **Claude Desktop** (free) from **claude.ai/download** and sign in with your normal Claude.ai account.
2. Open a terminal in this folder and run `pip install mcp`.
3. Open **`claude_desktop_config.json`** here and set the path in `args` to the full path of `server.py` on your computer.
4. In Claude Desktop, go to **Settings → Developer → Edit Config**, paste in the `doc-search` block, and save.
5. **Quit and reopen Claude Desktop.**
6. Ask Claude: *"Search my docs for the refund policy, then summarise it in two sentences."*

The detailed walkthrough is below.

## What it returns

```json
{
  "query": "rate limit",
  "folder": "/path/to/docs",
  "result_count": 2,
  "results": [
    {
      "file": "api-reference.txt",
      "line": 15,
      "excerpt": "Rate limits\n-----------\nStarter: 100 requests/minute\n..."
    }
  ]
}
```

Each result includes ±3 lines of context around the matching line.

## Quick start

```bash
# 1. Install dependencies
pip install mcp

# 2. Add some .txt or .md files to the docs/ folder (samples included)

# 3. Run the server
python server.py
```

The `docs/` folder next to `server.py` is the default search location.
Pass a different `folder` argument to search elsewhere.

## Connect to Claude Desktop

```json
{
  "mcpServers": {
    "doc-search": {
      "command": "python",
      "args": ["/ABSOLUTE/PATH/TO/samples/sample-05/server.py"]
    }
  }
}
```

## Example prompts

- "Search my docs for 'authentication'"
- "What do our docs say about cancellation?"
- "Find all mentions of 'webhook' in the API reference"
- "Search /Users/me/projects/docs for 'deployment'"

## Included sample docs

| File | Content |
|---|---|
| `docs/getting-started.md` | Onboarding walkthrough |
| `docs/billing.md` | Plans, pricing, and invoices |
| `docs/api-reference.txt` | REST API endpoints and auth |
| `docs/faq.txt` | Common questions and answers |

## Test without Claude

```bash
python test_tool.py
```

Runs 7 assertions: found/not-found, case-insensitivity, context lines, empty query, bad folder.

## Extending this sample

- Add fuzzy / semantic search using `sentence-transformers` + a vector store
- Walk subdirectories (already supported via `os.walk`)
- Add support for PDF files using `pypdf`
- Highlight the exact matching phrase in the excerpt
- Return a `relevance_score` and sort by it
