"""
test_tool.py — Manual test scaffold for your MCP tools (no Claude required)
Run: python test_tool.py
TODO: Add your own test cases after implementing server.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from server import lookup_customer, list_customers


def run_tests():
    print("=== Customer Lookup MCP Server — Tool Tests ===\n")

    # TODO: Test 1 — lookup a customer by ID
    # result = lookup_customer("TODO: a real customer ID from your data")
    # print(result)
    # assert "TODO: expected name" in str(result)
    # print("PASS\n")

    # TODO: Test 2 — list all customers
    # result = list_customers()
    # print(result)
    # assert len(result) > 0
    # print("PASS\n")

    print("TODO: Add your test cases above, then run this file to verify your implementation.")


if __name__ == "__main__":
    run_tests()
