# MCP Server: Customer Lookup
# Connects to Claude Desktop — no ANTHROPIC_API_KEY needed
# Uses your Claude.ai subscription via Claude Desktop
#
# This is a WORKING example. Clone it, run it, see it work — then swap in your
# own data (sample-data/customers.csv) and adapt the tools for your use case.

import csv
import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("customer-lookup")

# The CSV that holds our customer data. It lives in the sample-data/ folder
# right next to this file, so the server finds it no matter where you run it.
DATA_FILE = os.path.join(os.path.dirname(__file__), "sample-data", "customers.csv")


def _load_customers() -> list[dict]:
    """Read every row of the CSV into a list of dictionaries."""
    with open(DATA_FILE, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


@mcp.tool()
def lookup_customer(id_or_name: str) -> dict:
    """Look up one customer by their ID (e.g. 'C001') or by name (e.g. 'Alice').

    Returns the customer's name, email, plan and status. Matching is
    case-insensitive and also works on partial names.
    """
    query = id_or_name.strip().lower()
    for row in _load_customers():
        if row["id"].lower() == query or query in row["name"].lower():
            return {
                "id": row["id"],
                "name": row["name"],
                "email": row["email"],
                "plan": row["plan"],
                "status": row["status"],
            }
    return {"error": f"No customer found matching '{id_or_name}'."}


@mcp.tool()
def list_customers() -> list:
    """List every customer with their ID, name and plan."""
    return [
        {"id": row["id"], "name": row["name"], "plan": row["plan"]}
        for row in _load_customers()
    ]


if __name__ == "__main__":
    mcp.run()
