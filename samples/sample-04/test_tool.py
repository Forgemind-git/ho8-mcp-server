"""
test_tool.py — Manual test scaffold for your MCP tools (no Claude required)
Run: python test_tool.py
TODO: Add your own test cases after implementing server.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from server import get_quote, get_commission


def run_tests():
    print("=== Pricing Calculator MCP Server — Tool Tests ===\n")

    # TODO: Test 1 — get a quote
    # result = get_quote(10, "TODO: plan name", 12)
    # print(result)
    # assert "monthly" in result
    # print("PASS\n")

    # TODO: Test 2 — get commission
    # result = get_commission(5000.0, "TODO: tier name")
    # print(result)
    # assert "amount" in result
    # print("PASS\n")

    print("TODO: Add your test cases above, then run this file to verify your implementation.")


if __name__ == "__main__":
    run_tests()
