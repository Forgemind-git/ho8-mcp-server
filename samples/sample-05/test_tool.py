"""
test_tool.py — Unit test for calculate_quote (no Claude required)
Run: python test_tool.py
"""

import sys
import os
import json

sys.path.insert(0, os.path.dirname(__file__))
from server import calculate_quote


def run_tests():
    print("=== Pricing Calculator MCP Server — Tool Tests ===\n")

    # Test 1: Starter monthly — no discount
    print("Test 1: Starter, 3 seats, monthly")
    result = calculate_quote("starter", 3, "monthly")
    print(result)
    data = json.loads(result)
    assert data["plan"] == "Starter"
    assert data["unit_price_per_seat_per_month"] == 12.00
    assert data["total"] == 36.00
    assert data["discount_amount"] == 0.0
    assert data["savings_vs_monthly"] == 0.0
    print("PASS\n")

    # Test 2: Pro annual — 20% discount
    print("Test 2: Pro, 10 seats, annual")
    result = calculate_quote("pro", 10, "annual")
    print(result)
    data = json.loads(result)
    assert data["plan"] == "Pro"
    assert data["discount_pct"] == 20
    monthly_unit = 29.00
    expected_unit = round(monthly_unit * 0.80, 2)
    assert data["unit_price_per_seat_per_month"] == expected_unit
    assert data["savings_vs_monthly"] > 0
    print("PASS\n")

    # Test 3: Enterprise annual — 25% discount
    print("Test 3: Enterprise, 100 seats, annual")
    result = calculate_quote("enterprise", 100, "annual")
    print(result)
    data = json.loads(result)
    assert data["plan"] == "Enterprise"
    assert data["discount_pct"] == 25
    assert data["savings_vs_monthly"] > 0
    print("PASS\n")

    # Test 4: Invalid plan
    print("Test 4: Invalid plan 'premium'")
    result = calculate_quote("premium", 5, "monthly")
    print(result)
    assert "Unknown plan" in result
    print("PASS\n")

    # Test 5: Invalid billing
    print("Test 5: Invalid billing 'quarterly'")
    result = calculate_quote("pro", 5, "quarterly")
    print(result)
    assert "Unknown billing period" in result
    print("PASS\n")

    # Test 6: Seats exceed starter max (5)
    print("Test 6: Starter with 10 seats (exceeds max of 5)")
    result = calculate_quote("starter", 10, "monthly")
    print(result)
    assert "5 seats" in result or "contact sales" in result.lower()
    print("PASS\n")

    # Test 7: Case-insensitive plan and billing
    print("Test 7: Case-insensitive inputs (PRO / ANNUAL)")
    result = calculate_quote("PRO", 5, "ANNUAL")
    print(result)
    data = json.loads(result)
    assert data["plan"] == "Pro"
    assert data["billing"] == "annual"
    print("PASS\n")

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
