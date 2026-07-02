"""
test_tool.py — Run the tools directly, no Claude required.
Run: python test_tool.py

This proves the server works before you connect it to Claude Desktop.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from server import query_ho7, list_ho7


def run_tests():
    print("=== HO7 Connection MCP Server — Tool Tests ===\n")

    # Test 1 — look up an item by ID
    result = query_ho7("P001")
    print("query_ho7('P001') ->", result)
    assert result["title"] == "Weekly report generator"
    print("PASS\n")

    # Test 2 — keyword search over title / notes
    result = query_ho7("lead")
    print("query_ho7('lead') ->", result)
    assert result["id"] == "P002"
    print("PASS\n")

    # Test 3 — list every item
    result = list_ho7()
    print(f"list_ho7() -> {len(result)} items")
    assert len(result) == 4
    print("PASS\n")

    print("All tests passed. Your server is ready to connect to Claude Desktop.")


if __name__ == "__main__":
    run_tests()
