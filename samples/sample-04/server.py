# MCP Server: Task Manager
# Connects to Claude Desktop — no ANTHROPIC_API_KEY needed — uses your Claude.ai subscription via Claude Desktop
#
# This server gives Claude three tools to manage a simple to-do list that
# lives in a local SQLite file (tasks.db) right next to this script.

import os
import sqlite3

from mcp.server.fastmcp import FastMCP

# The name you'll see for this server inside Claude Desktop.
mcp = FastMCP("task-manager")

# Where we keep the tasks. This file is created automatically on first run,
# sitting in the same folder as this server.py.
DB_FILE = os.path.join(os.path.dirname(__file__), "tasks.db")


def _connect():
    """Open a connection to the SQLite database.

    row_factory = sqlite3.Row lets us read columns by name (row["title"]),
    which keeps the code below nice and readable.
    """
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def _init_db():
    """Create the tasks table if it doesn't exist yet, and seed a few
    example tasks the very first time so the list isn't empty."""
    conn = _connect()
    try:
        # Create the table. Each task has an id, a title, a status
        # ('todo' or 'done'), and an optional due date stored as text.
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                status TEXT DEFAULT 'todo',
                due_date TEXT
            )
            """
        )

        # If the table is empty, drop in 3 friendly example tasks so a
        # beginner sees something the moment they connect Claude.
        count = conn.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]
        if count == 0:
            conn.executemany(
                "INSERT INTO tasks (title, status, due_date) VALUES (?, ?, ?)",
                [
                    ("Email the Q3 report to finance", "todo", "2026-07-01"),
                    ("Book flights for the Lisbon conference", "todo", "2026-07-10"),
                    ("Review pull request #42", "todo", ""),
                ],
            )

        conn.commit()
    finally:
        conn.close()


# Set up the database the moment this file is imported, so the tools below
# always have a table to work with.
_init_db()


@mcp.tool()
def list_tasks(status: str = "") -> list:
    """List your tasks. Pass status='todo' to see only open tasks,
    or status='done' to see only finished ones. Leave it empty for all.

    Returns a list of dicts like {"id", "title", "status", "due_date"}.
    """
    conn = _connect()
    try:
        if status:
            # Filter by the requested status (e.g. "todo" or "done").
            rows = conn.execute(
                "SELECT id, title, status, due_date FROM tasks WHERE status = ? ORDER BY id",
                (status,),
            ).fetchall()
        else:
            # No filter — return every task.
            rows = conn.execute(
                "SELECT id, title, status, due_date FROM tasks ORDER BY id"
            ).fetchall()

        # Turn each database row into a plain dictionary for Claude.
        return [
            {
                "id": row["id"],
                "title": row["title"],
                "status": row["status"],
                "due_date": row["due_date"],
            }
            for row in rows
        ]
    finally:
        conn.close()


@mcp.tool()
def add_task(title: str, due: str = "") -> dict:
    """Add a new task to your list. 'title' is what to do; 'due' is an
    optional due date like '2026-07-03'. New tasks start as 'todo'.

    Returns {"id": <new id>} for the task that was created.
    """
    conn = _connect()
    try:
        cursor = conn.execute(
            "INSERT INTO tasks (title, status, due_date) VALUES (?, 'todo', ?)",
            (title, due),
        )
        conn.commit()
        # lastrowid is the id SQLite gave the brand-new row.
        return {"id": cursor.lastrowid}
    finally:
        conn.close()


@mcp.tool()
def complete_task(id: int) -> str:
    """Mark a task as done by its id. Returns 'ok' when it worked, or a
    friendly note if no task has that id."""
    conn = _connect()
    try:
        cursor = conn.execute(
            "UPDATE tasks SET status = 'done' WHERE id = ?",
            (id,),
        )
        conn.commit()
        # rowcount tells us how many rows changed — 0 means no such task.
        if cursor.rowcount > 0:
            return "ok"
        return f"No task with id {id}"
    finally:
        conn.close()


if __name__ == "__main__":
    mcp.run()
