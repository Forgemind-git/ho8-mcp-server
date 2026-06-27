"""
test_tool.py — Unit test for lookup_customer (no Claude required)
Run: python test_tool.py
"""

import sys
import os

# Allow running from any directory
sys.path.insert(0, os.path.dirname(__file__))

from server import lookup_customer

def run_tests():
    print("=== Customer Lookup MCP Server — Tool Tests ===\n")

    # Test 1: Lookup by ID
    print("Test 1: Lookup by ID (C001)")
    result = lookup_customer("C001")
    print(result)
    assert "Alice Johnson" in result, "Expected Alice Johnson"
    assert "pro" in result, "Expected plan=pro"
    print("PASS\n")

    # Test 2: Lookup by email
    print("Test 2: Lookup by email (bob@startup.io)")
    result = lookup_customer("bob@startup.io")
    print(result)
    assert "Bob Smith" in result, "Expected Bob Smith"
    assert "starter" in result, "Expected plan=starter"
    print("PASS\n")

    # Test 3: Enterprise customer with open tickets
    print("Test 3: Lookup enterprise customer (C003)")
    result = lookup_customer("C003")
    print(result)
    assert "Carol White" in result
    assert "enterprise" in result
    assert '"open_tickets": 5' in result
    print("PASS\n")

    # Test 4: Not found by ID
    print("Test 4: Not found by ID (C999)")
    result = lookup_customer("C999")
    print(result)
    assert "No customer found" in result
    print("PASS\n")

    # Test 5: Not found by email
    print("Test 5: Not found by email (unknown@nowhere.com)")
    result = lookup_customer("unknown@nowhere.com")
    print(result)
    assert "No customer found" in result
    print("PASS\n")

    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
