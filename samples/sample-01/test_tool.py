"""
test_tool.py — Unit test for query_ho7 (no Claude required)
Run: python test_tool.py
"""

import sys
import os

# Allow running from any directory
sys.path.insert(0, os.path.dirname(__file__))

from server import query_ho7


def run_tests():
    print("=== HO7 Connection MCP Server — Tool Tests ===\n")

    # Test 1: Summary overview
    print("Test 1: Summary overview")
    result = query_ho7("summary")
    print(result)
    assert '"total": 3' in result, "Expected total=3"
    print("PASS\n")

    # Test 2: Lookup by id
    print("Test 2: Lookup by id (P001)")
    result = query_ho7("P001")
    print(result)
    assert "Weekly report generator" in result
    print("PASS\n")

    # Test 3: Keyword search
    print("Test 3: Keyword search (lead)")
    result = query_ho7("lead")
    print(result)
    assert "Lead follow-up drafts" in result
    print("PASS\n")

    # Test 4: No match
    print("Test 4: No match (banana)")
    result = query_ho7("banana")
    print(result)
    assert "matched" in result
    print("PASS\n")

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
