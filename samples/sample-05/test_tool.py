"""
test_tool.py — Manual test for your MCP tools (no Claude or API key required)
Run: python test_tool.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from server import search_docs, read_doc


def run_tests():
    print("=== Doc Search MCP Server — Tool Tests ===\n")

    # Test 1 — search for "refund", which appears in docs/billing.md
    print("Test 1: search_docs('refund')")
    result = search_docs("refund")
    for match in result:
        print(f"  - {match['filename']}: {match['snippet']}")
    assert len(result) > 0, "Expected at least one match for 'refund'"
    print(f"  PASS — found {len(result)} match(es)\n")

    # Test 2 — read a specific document and check we got its content
    print("Test 2: read_doc('faq.txt')")
    result = read_doc("faq.txt")
    print(f"  keys returned: {list(result.keys())}")
    assert "content" in result, "Expected a 'content' key in the result"
    print(f"  PASS — read {len(result['content'])} characters from faq.txt\n")

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
