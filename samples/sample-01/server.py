# MCP Server: HO7 Connection
# Connects to Claude Desktop — no ANTHROPIC_API_KEY needed
# Uses your Claude.ai subscription via Claude Desktop
#
# This is a WORKING example that connects the solution you built in HO7
# (your mid-course capstone) to Claude. Clone it, run it, see it work — then
# swap in your own HO7 data (sample-data/ho7_items.csv) or point the tools at
# your real HO7 database / API so Claude acts on your capstone live.

import csv
import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ho7-connection")

# The CSV that stands in for YOUR HO7 solution's data. It lives in the
# sample-data/ folder next to this file. Replace it with a real query into your
# HO7 project (database, API, or export) and keep the tools the same.
DATA_FILE = os.path.join(os.path.dirname(__file__), "sample-data", "ho7_items.csv")


def _load_items() -> list[dict]:
    """Read every row of the CSV into a list of dictionaries."""
    with open(DATA_FILE, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


@mcp.tool()
def query_ho7(query: str) -> dict:
    """Query the solution you built in HO7 (your mid-course capstone).

    Look up one item by its ID (e.g. 'P001') or by a keyword in its title or
    notes. Matching is case-insensitive and works on partial text. Returns the
    matching item pulled live from your HO7 solution — not a guess.
    """
    q = query.strip().lower()
    for row in _load_items():
        if row["id"].lower() == q or q in row["title"].lower() or q in row["notes"].lower():
            return {
                "id": row["id"],
                "title": row["title"],
                "status": row["status"],
                "notes": row["notes"],
            }
    return {"error": f"Nothing in your HO7 solution matched '{query}'."}


@mcp.tool()
def list_ho7() -> list:
    """List every item in your HO7 solution with its ID, title and status."""
    return [
        {"id": row["id"], "title": row["title"], "status": row["status"]}
        for row in _load_items()
    ]


if __name__ == "__main__":
    mcp.run()
