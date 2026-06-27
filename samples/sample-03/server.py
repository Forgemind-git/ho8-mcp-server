"""
Task Manager MCP Server
-----------------------
Exposes one tool: manage_tasks
Read and write tasks from a local tasks.json file.
Supports actions: list | add | complete
"""

import json
import os
from datetime import datetime
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("task-manager")

# tasks.json lives next to this file
TASKS_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")


def _load_tasks() -> list:
    """Load tasks from disk, returning empty list if file doesn't exist."""
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def _save_tasks(tasks: list) -> None:
    """Persist tasks to disk."""
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


@mcp.tool()
def manage_tasks(action: str, task: str = "") -> str:
    """
    Read and write tasks from a local tasks.json file.

    Args:
        action: One of 'list', 'add', or 'complete'.
        task: Task description (required for 'add') or task ID/name (for 'complete').

    Returns:
        Task list or confirmation of action taken.
    """
    action = action.strip().lower()

    if action == "list":
        tasks = _load_tasks()
        if not tasks:
            return "No tasks yet. Use action='add' with a task description to create one."

        lines = []
        for t in tasks:
            status = "DONE" if t.get("completed") else "TODO"
            lines.append(f"[{t['id']}] [{status}] {t['title']} (added {t['created_at']})")
        return "\n".join(lines)

    elif action == "add":
        if not task.strip():
            return "Error: 'task' description is required for action='add'."

        tasks = _load_tasks()
        new_id = max((t["id"] for t in tasks), default=0) + 1
        new_task = {
            "id": new_id,
            "title": task.strip(),
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d"),
            "completed_at": None,
        }
        tasks.append(new_task)
        _save_tasks(tasks)
        return f"Task added: [{new_id}] {new_task['title']}"

    elif action == "complete":
        if not task.strip():
            return "Error: provide a task ID or title fragment for action='complete'."

        tasks = _load_tasks()
        query = task.strip()

        # Try matching by numeric ID first, then by title substring
        matched = None
        if query.isdigit():
            task_id = int(query)
            matched = next((t for t in tasks if t["id"] == task_id), None)
        else:
            lower_query = query.lower()
            matched = next(
                (t for t in tasks if lower_query in t["title"].lower()), None
            )

        if not matched:
            return f"No task found matching '{query}'. Use action='list' to see all tasks."

        if matched["completed"]:
            return f"Task [{matched['id']}] '{matched['title']}' is already completed."

        matched["completed"] = True
        matched["completed_at"] = datetime.now().strftime("%Y-%m-%d")
        _save_tasks(tasks)
        return f"Task completed: [{matched['id']}] {matched['title']}"

    else:
        return f"Unknown action '{action}'. Valid actions: list, add, complete."


if __name__ == "__main__":
    print("Starting Task Manager MCP server...")
    print(f"Tasks file: {TASKS_FILE}")
    mcp.run()
