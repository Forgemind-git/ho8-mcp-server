"""
test_tool.py — Manual test scaffold for your MCP tools (no Claude required)
Run: python test_tool.py
TODO: Add your own test cases after implementing server.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from server import search_docs, read_doc


def run_tests():
    print("=== Doc Search MCP Server — Tool Tests ===\n")

    # TODO: Test 1 — search for a term that exists in your docs
    # result = search_docs("TODO: a word that appears in your sample docs")
    # print(result)
    # assert len(result) > 0
    # print("PASS\n")

    # TODO: Test 2 — read a specific doc
    # result = read_doc("TODO: a filename in your sample-data/ folder")
    # print(result)
    # assert "content" in result
    # print("PASS\n")

    print("TODO: Add your test cases above, then run this file to verify your implementation.")


if __name__ == "__main__":
    run_tests()
