"""
test_tool.py — Run the tools directly, no Claude required.
Run: python test_tool.py

This proves the server works before you connect it to Claude Desktop.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from server import lookup_customer, list_customers


def run_tests():
    print("=== Customer Lookup MCP Server — Tool Tests ===\n")

    # Test 1 — look up a customer by ID
    result = lookup_customer("C001")
    print("lookup_customer('C001') ->", result)
    assert result["name"] == "Alice Johnson"
    print("PASS\n")

    # Test 2 — look up a customer by partial name
    result = lookup_customer("carol")
    print("lookup_customer('carol') ->", result)
    assert result["id"] == "C003"
    print("PASS\n")

    # Test 3 — list all customers
    result = list_customers()
    print(f"list_customers() -> {len(result)} customers")
    assert len(result) == 8
    print("PASS\n")

    print("All tests passed. Your server is ready to connect to Claude Desktop.")


if __name__ == "__main__":
    run_tests()
