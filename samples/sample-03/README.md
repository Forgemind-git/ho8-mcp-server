# Sample 03 — Task Manager MCP Server

**Problem:** You want to manage a to-do list directly in Claude — add tasks, check what's pending, and mark things done — without switching to a separate app.

**Tool exposed:** `manage_tasks`

> Read and write tasks from a local `tasks.json` file.

## Use it with your Claude.ai subscription
No API key needed — uses your Claude.ai subscription via Claude Desktop.

1. Download **Claude Desktop** (free) from **claude.ai/download** and sign in with your normal Claude.ai account.
2. Open a terminal in this folder and run `pip install mcp`.
3. Open **`claude_desktop_config.json`** here and set the path in `args` to the full path of `server.py` on your computer.
4. In Claude Desktop, go to **Settings → Developer → Edit Config**, paste in the `task-manager` block, and save.
5. **Quit and reopen Claude Desktop.**
6. Ask Claude: *"List my tasks, then add a new task 'Prepare slides for Monday standup' and confirm it was added."*

The detailed walkthrough is below.

## Supported actions

| `action` | `task` param | What happens |
|---|---|---|
| `list` | — | Returns all tasks with status |
| `add` | Task description | Appends a new TODO task |
| `complete` | Task ID or title fragment | Marks the matching task as done |

## Quick start

```bash
# 1. Install dependencies
pip install mcp

# 2. Run the server
python server.py
```

Tasks are stored in `tasks.json` next to `server.py`. The file is created automatically on first use.

## Connect to Claude Desktop

```json
{
  "mcpServers": {
    "task-manager": {
      "command": "python",
      "args": ["/ABSOLUTE/PATH/TO/samples/sample-03/server.py"]
    }
  }
}
```

Replace the path and restart Claude Desktop.

## Example prompts

- "List all my tasks"
- "Add a task: Review the pull request"
- "Mark task 3 as complete"
- "Complete the task about the pull request"

## Test without Claude

```bash
python test_tool.py
```

Runs 10 assertions covering all three actions, error cases, and the complete-by-title-fragment feature.
The test backs up and restores `tasks.json` so your real tasks are safe.

## tasks.json format

```json
[
  {
    "id": 1,
    "title": "Write the course README",
    "completed": false,
    "created_at": "2024-06-27",
    "completed_at": null
  }
]
```

## Extending this sample

- Add a `delete` action
- Add a `due_date` field and a `list_overdue` action
- Sync to a real task manager (Linear, Notion, Jira) via their APIs
