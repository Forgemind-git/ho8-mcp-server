# MCP Server: Pricing Calculator
# Connects to Claude Desktop — no ANTHROPIC_API_KEY needed.
# Uses your Claude.ai subscription via Claude Desktop.
# ---------------------------------------------------------------------------
# This is a tiny, fully-working MCP server. It gives Claude two "tools" it can
# call to do your pricing and commission math reliably. The numbers live HERE,
# in this file, so Claude doesn't have to guess or remember them.
# ---------------------------------------------------------------------------

from mcp.server.fastmcp import FastMCP

# Create the MCP server. The name is what shows up inside Claude Desktop.
mcp = FastMCP("pricing-calculator")

# -- Your pricing table -----------------------------------------------------
# Each plan has a per-seat monthly price and an annual discount (0.20 = 20% off
# when the customer pays for a full year). Edit these to match your real plans.
PRICING = {
    "starter":    {"monthly_per_seat": 12.0, "annual_discount": 0.0},
    "pro":        {"monthly_per_seat": 29.0, "annual_discount": 0.20},
    "enterprise": {"monthly_per_seat": 79.0, "annual_discount": 0.25},
}

# -- Your commission tiers --------------------------------------------------
# How much commission a rep earns, as a fraction of the deal value.
COMMISSION_TIERS = {"junior": 0.05, "senior": 0.08, "lead": 0.10}


@mcp.tool()
def get_quote(seats: int, plan: str, term_months: int) -> dict:
    """Calculate a price quote for a number of seats on a plan.

    Args:
        seats: How many user seats (must be at least 1).
        plan: One of "starter", "pro", or "enterprise" (case-insensitive).
        term_months: Length of the contract in months. 12 or more counts as
            an annual term, which applies the plan's annual discount.
    """
    # Be friendly about capitalisation: "Pro" and "pro" both work.
    plan_key = plan.lower().strip()

    # If the plan isn't one we know, tell the caller which ones are valid.
    if plan_key not in PRICING:
        return {
            "error": f"Unknown plan '{plan}'. Valid plans: "
                     + ", ".join(PRICING.keys())
        }

    # Seats has to be a real, positive number of people.
    if seats < 1:
        return {"error": "seats must be at least 1."}

    info = PRICING[plan_key]
    per_seat = info["monthly_per_seat"]
    discount = info["annual_discount"]

    # Plain monthly cost = seats x per-seat price.
    monthly = seats * per_seat

    # Yearly total before any discount, then apply the annual discount only if
    # the customer is committing to a year or more.
    yearly = monthly * 12
    if term_months >= 12:
        annual = yearly * (1 - discount)
        discount_pct = int(round(discount * 100))
    else:
        # Short term: just the months they asked for, no annual discount.
        annual = monthly * term_months
        discount_pct = 0

    return {
        "plan": plan_key,
        "seats": seats,
        "term_months": term_months,
        "monthly": round(monthly, 2),
        "annual": round(annual, 2),
        "discount": discount_pct,
    }


@mcp.tool()
def get_commission(deal_value: float, tier: str) -> dict:
    """Calculate the commission earned on a deal.

    Args:
        deal_value: The total value of the deal (e.g. the annual contract value).
        tier: One of "junior", "senior", or "lead" (case-insensitive).
    """
    # Again, accept any capitalisation.
    tier_key = tier.lower().strip()

    if tier_key not in COMMISSION_TIERS:
        return {
            "error": f"Unknown tier '{tier}'. Valid tiers: "
                     + ", ".join(COMMISSION_TIERS.keys())
        }

    pct = COMMISSION_TIERS[tier_key]

    return {
        "tier": tier_key,
        "deal_value": deal_value,
        "pct": pct * 100,                      # show as a percentage, e.g. 8.0
        "amount": round(deal_value * pct, 2),  # the actual commission earned
    }


# Start the server when run directly. Claude Desktop launches this for you.
if __name__ == "__main__":
    mcp.run()
