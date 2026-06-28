# MCP Server: Pricing Calculator
# Connects to Claude Desktop — no ANTHROPIC_API_KEY needed
# Uses your Claude.ai subscription via Claude Desktop

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("TODO: name your MCP server")

# TODO: Set up your pricing table here (hardcoded in Python)
# Example structure:
# PRICING = {
#     "starter": {"monthly_per_seat": 10, "annual_discount": 0.0},
#     "pro":     {"monthly_per_seat": 25, "annual_discount": 0.20},
# }
#
# COMMISSION_TIERS = {
#     "junior": 0.05,
#     "senior": 0.08,
# }


@mcp.tool()
def get_quote(seats: int, plan: str, term_months: int) -> dict:
    """TODO: describe what this tool does and what it returns"""
    # TODO: implement this tool
    # It should use the pricing table above to calculate and return:
    # {"monthly": ..., "annual": ..., "discount": ...}
    raise NotImplementedError("TODO: implement get_quote")


@mcp.tool()
def get_commission(deal_value: float, tier: str) -> dict:
    """TODO: describe what this tool does and what it returns"""
    # TODO: implement this tool
    # It should calculate commission based on deal value and tier:
    # {"amount": ..., "pct": ...}
    raise NotImplementedError("TODO: implement get_commission")


if __name__ == "__main__":
    mcp.run()
