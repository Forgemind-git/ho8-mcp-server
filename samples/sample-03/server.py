# MCP Server: Task Manager
# Connects to Claude Desktop — no ANTHROPIC_API_KEY needed
# Uses your Claude.ai subscription via Claude Desktop

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("TODO: name your MCP server")

# TODO: Set up your data source here
# This sample uses SQLite to store tasks locally
# Example: import sqlite3; DB_FILE = "tasks.db"
# Create a tasks table with columns: id, title, status, due_date


@mcp.tool()
def list_tasks(status: str = "") -> list:
    """TODO: describe what this tool does and what it returns"""
    # TODO: implement this tool
    # It should query the SQLite DB and return a list like:
    # [{"id": 1, "title": "...", "status": "todo"}]
    # If status is provided, filter by it (e.g. "todo", "done")
    raise NotImplementedError("TODO: implement list_tasks")


@mcp.tool()
def add_task(title: str, due: str = "") -> dict:
    """TODO: describe what this tool does and what it returns"""
    # TODO: implement this tool
    # It should insert a new task and return {"id": <new_id>}
    raise NotImplementedError("TODO: implement add_task")


@mcp.tool()
def complete_task(id: int) -> str:
    """TODO: describe what this tool does and what it returns"""
    # TODO: implement this tool
    # It should mark the task as done and return "ok" or an error message
    raise NotImplementedError("TODO: implement complete_task")


if __name__ == "__main__":
    mcp.run()
