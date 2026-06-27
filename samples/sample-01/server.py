"""
Customer Lookup MCP Server
--------------------------
Exposes one tool: lookup_customer
Look up a customer by email or ID from a local JSON database.
"""

import json
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("customer-lookup")

CUSTOMERS = {
    "C001": {"customer_id": "C001", "name": "Alice Johnson", "email": "alice@acmecorp.com", "plan": "pro", "created_at": "2023-04-12", "open_tickets": 2},
    "C002": {"customer_id": "C002", "name": "Bob Smith", "email": "bob@startup.io", "plan": "starter", "created_at": "2024-01-08", "open_tickets": 0},
    "C003": {"customer_id": "C003", "name": "Carol White", "email": "carol@enterprise.com", "plan": "enterprise", "created_at": "2022-11-30", "open_tickets": 5},
    "C004": {"customer_id": "C004", "name": "David Lee", "email": "david@freelancer.dev", "plan": "starter", "created_at": "2024-06-01", "open_tickets": 1},
    "C005": {"customer_id": "C005", "name": "Eve Martinez", "email": "eve@bigco.net", "plan": "enterprise", "created_at": "2021-08-19", "open_tickets": 0},
}

EMAIL_INDEX = {v["email"]: k for k, v in CUSTOMERS.items()}


@mcp.tool()
def lookup_customer(customer_id: str) -> str:
    """
    Look up a customer by email or ID from a local JSON database.

    Args:
        customer_id: The customer ID (e.g. C001) or email address to look up.

    Returns:
        Customer name, plan, created_at, and open_tickets count.
    """
    query = customer_id.strip()

    if "@" in query:
        resolved_id = EMAIL_INDEX.get(query.lower())
        if not resolved_id:
            return f"No customer found with email '{query}'."
        query = resolved_id

    customer = CUSTOMERS.get(query.upper())
    if not customer:
        return f"No customer found with ID '{query}'."

    return json.dumps({
        "customer_id": customer["customer_id"],
        "name": customer["name"],
        "email": customer["email"],
        "plan": customer["plan"],
        "created_at": customer["created_at"],
        "open_tickets": customer["open_tickets"],
    }, indent=2)


if __name__ == "__main__":
    print("Starting Customer Lookup MCP server...")
    mcp.run()
