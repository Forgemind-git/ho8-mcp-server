# HO8 Sample 5 — Document Search MCP Server

## What you'll build

This sample points Claude at a folder of your own notes or documents and gives
it two tools — `search_docs` and `read_doc`. With them, Claude can find the
right document and quote from it for you, instead of you hunting through files
yourself. Just ask a question in plain English and Claude searches your docs,
opens the best match, and answers using what it finds. It comes with 4 example
docs (for a make-believe product called "Acme Cloud") so you can try it right
away, then swap in your own files.

## Use it with your Claude.ai subscription

No API key needed — uses your Claude.ai subscription via Claude Desktop.

1. Download **Claude Desktop** from https://claude.ai/download and sign in with
   your Claude.ai account.
2. Install the MCP library:
   ```
   pip install mcp
   ```
3. (Optional) Make sure everything works by running the included test:
   ```
   python test_tool.py
   ```
   You should see "All tests passed."
4. Open `claude_desktop_config.json` and change the path in `"args"` to the
   full path of `server.py` on your computer (where you saved this folder).
5. In Claude Desktop, go to **Settings → Developer → Edit Config**, paste in
   the `doc-search` block from `claude_desktop_config.json`, and save.
6. **Quit and reopen** Claude Desktop so it picks up the new server.
7. Ask Claude the example prompt below.

## The example prompt

```
Using my doc-search tools, find where our docs talk about refunds, then read
the relevant document and summarise our refund policy in two sentences.
```

## Make it your own

- Drop your own `.txt` or `.md` files into the `docs/` folder — Claude will be
  able to search them right away.
- Point `DOCS_FOLDER` in `server.py` at a different folder (for example, a
  notes folder on your computer).
- Add a third tool that lists all the document filenames, so you can ask Claude
  "what documents do I have?"

## Optional — automate it with the API (advanced)

You don't need this for the course. If you ever want to run document search
from a standalone script (outside Claude Desktop), you'd use the Anthropic API,
which needs a paid Anthropic API key — that's separate from your Claude.ai
subscription. For this sample, stick with Claude Desktop; no key required.
