"""
HO7 Connection MCP Server
-------------------------
Exposes one tool: query_ho7

Connect the solution you already built in HO7 (your mid-course capstone) to Claude.
This server exposes your HO7 project's data as a real, queryable tool so Claude can
answer questions or take actions straight from it — no guessing.

HOW TO MAKE IT YOURS
--------------------
The HO7_DATA dictionary below is placeholder data standing in for your HO7 solution.
Replace it with a real query into your own HO7 project:
  - reading rows from your HO7 database (sqlite3, psycopg2, ...)
  - calling your HO7 project's API or reading its JSON/CSV export
  - triggering an action your HO7 app exposes
Keep the tool signature the same and Claude will call it exactly as-is.
"""

import json
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ho7-connection")

# --- Placeholder for YOUR HO7 solution's data. Replace with a real query. ---
HO7_DATA = {
    "items": [
        {"id": "P001", "title": "Weekly report generator", "status": "done", "owner": "you", "notes": "Built in HO7 — produces the Monday summary."},
        {"id": "P002", "title": "Lead follow-up drafts", "status": "in_progress", "owner": "you", "notes": "HO7 capstone module that drafts replies."},
        {"id": "P003", "title": "Invoice reconciliation", "status": "todo", "owner": "you", "notes": "Planned extension of the HO7 project."},
    ],
    "summary": {"total": 3, "done": 1, "in_progress": 1, "todo": 1},
}


@mcp.tool()
def query_ho7(query: str) -> str:
    """
    Query the solution you built in HO7 (your mid-course capstone).

    Args:
        query: What to look up. Use "summary" for an overview, an id like "P001",
               or any keyword to search titles and notes in your HO7 project.

    Returns:
        A JSON result pulled live from your HO7 solution (not a guess).
    """
    q = query.strip().lower()

    if q in ("summary", "overview", "status", "all"):
        return json.dumps(HO7_DATA["summary"], indent=2)

    # Match by id
    for item in HO7_DATA["items"]:
        if item["id"].lower() == q:
            return json.dumps(item, indent=2)

    # Keyword search over titles and notes
    hits = [
        item for item in HO7_DATA["items"]
        if q in item["title"].lower() or q in item["notes"].lower()
    ]
    if hits:
        return json.dumps(hits, indent=2)

    return f"Nothing in your HO7 solution matched '{query}'. Try 'summary' or an id like P001."


if __name__ == "__main__":
    print("Starting HO7 Connection MCP server...")
    mcp.run()
