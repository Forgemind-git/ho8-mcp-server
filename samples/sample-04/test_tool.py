"""
test_tool.py — Quick local test for your MCP tools (no Claude required).
Run: python test_tool.py
"""

import sys
import os

# Make sure we can import server.py that sits next to this file.
sys.path.insert(0, os.path.dirname(__file__))

from server import get_quote, get_commission


def run_tests():
    print("=== Pricing Calculator MCP Server — Tool Tests ===\n")

    # Test 1 — a quote for 10 seats on the pro plan, billed for a full year.
    result = get_quote(10, "pro", 12)
    print("get_quote(10, 'pro', 12) ->", result)
    assert "error" not in result, "quote should not return an error"
    assert "monthly" in result, "quote should include a 'monthly' figure"
    print("PASS\n")

    # Test 2 — senior-tier commission on a $5,000 deal = 8% = $400.00.
    result = get_commission(5000.0, "senior")
    print("get_commission(5000.0, 'senior') ->", result)
    assert "amount" in result, "commission should include an 'amount'"
    assert result["amount"] == 400.0, "8% of 5000 should be 400.0"
    print("PASS\n")

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
