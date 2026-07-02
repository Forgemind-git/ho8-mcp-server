"""
Pricing Calculator MCP Server
------------------------------
Exposes one tool: calculate_quote
Calculate a product quote given plan, seats, and billing period.
"""

import json
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("pricing-calculator")

# ---------------------------------------------------------------------------
# Pricing configuration
# ---------------------------------------------------------------------------
PLANS = {
    "starter": {
        "display_name": "Starter",
        "monthly_price_per_seat": 12.00,
        "annual_discount_pct": 0.0,   # no annual discount on starter
        "max_seats": 5,
    },
    "pro": {
        "display_name": "Pro",
        "monthly_price_per_seat": 29.00,
        "annual_discount_pct": 0.20,  # 20% off for annual billing
        "max_seats": 50,
    },
    "enterprise": {
        "display_name": "Enterprise",
        "monthly_price_per_seat": 79.00,
        "annual_discount_pct": 0.25,  # 25% off for annual billing
        "max_seats": 10000,
    },
}


@mcp.tool()
def calculate_quote(plan: str, seats: int, billing: str) -> str:
    """
    Calculate a product quote given plan, seats, and billing period.

    Args:
        plan: Plan tier — 'starter', 'pro', or 'enterprise'.
        seats: Number of seats (must be a positive integer).
        billing: Billing period — 'monthly' or 'annual'.

    Returns:
        unit_price, subtotal, discount, total, and savings_vs_monthly as JSON.
    """
    plan = plan.strip().lower()
    billing = billing.strip().lower()

    # Validate plan
    if plan not in PLANS:
        valid = ", ".join(PLANS.keys())
        return f"Unknown plan '{plan}'. Valid plans: {valid}."

    # Validate billing
    if billing not in ("monthly", "annual"):
        return f"Unknown billing period '{billing}'. Use 'monthly' or 'annual'."

    # Validate seats
    if not isinstance(seats, int) or seats < 1:
        return "seats must be a positive integer (e.g. 5)."

    plan_info = PLANS[plan]
    max_seats = plan_info["max_seats"]

    if seats > max_seats:
        return (
            f"The {plan_info['display_name']} plan supports up to {max_seats} seats. "
            f"For {seats} seats, please contact sales for an enterprise quote."
        )

    monthly_unit = plan_info["monthly_price_per_seat"]
    discount_pct = plan_info["annual_discount_pct"] if billing == "annual" else 0.0

    if billing == "monthly":
        unit_price = monthly_unit
        subtotal = unit_price * seats
        discount_amount = 0.0
        total = subtotal
        savings_vs_monthly = 0.0
    else:
        # Annual: price per seat per MONTH (displayed as monthly-equivalent)
        unit_price = round(monthly_unit * (1 - discount_pct), 2)
        # Total billed annually = unit_price * seats * 12
        subtotal = round(unit_price * seats * 12, 2)
        monthly_total_if_monthly = monthly_unit * seats * 12
        discount_amount = round(monthly_total_if_monthly - subtotal, 2)
        total = subtotal
        savings_vs_monthly = discount_amount

    return json.dumps({
        "plan": plan_info["display_name"],
        "seats": seats,
        "billing": billing,
        "unit_price_per_seat_per_month": round(unit_price, 2),
        "subtotal": round(subtotal, 2),
        "discount_pct": int(discount_pct * 100),
        "discount_amount": round(discount_amount, 2),
        "total": round(total, 2),
        "savings_vs_monthly": round(savings_vs_monthly, 2),
        "billing_note": (
            f"Billed as ${total:.2f}/year" if billing == "annual"
            else f"Billed as ${total:.2f}/month"
        ),
    }, indent=2)


if __name__ == "__main__":
    print("Starting Pricing Calculator MCP server...")
    mcp.run()
