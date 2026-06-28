# MCP Server: Customer Lookup
# Connects to Claude Desktop — no ANTHROPIC_API_KEY needed
# Uses your Claude.ai subscription via Claude Desktop

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("TODO: name your MCP server")

# TODO: Set up your data source here
# Example: load a CSV, connect to SQLite, or build an in-memory dict
# DATA_FILE = "sample-data/customers.csv"


@mcp.tool()
def lookup_customer(id_or_name: str) -> dict:
    """TODO: describe what this tool does and what it returns"""
    # TODO: implement this tool
    # It should accept a customer ID or name and return a dict like:
    # {"name": "...", "email": "...", "plan": "...", "status": "..."}
    raise NotImplementedError("TODO: implement lookup_customer")


@mcp.tool()
def list_customers() -> list:
    """TODO: describe what this tool does and what it returns"""
    # TODO: implement this tool
    # It should return a list of dicts like:
    # [{"id": "...", "name": "...", "plan": "..."}]
    raise NotImplementedError("TODO: implement list_customers")


if __name__ == "__main__":
    mcp.run()
