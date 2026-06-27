"""
test_tool.py — Unit test for search_docs (no Claude required)
Run: python test_tool.py

Uses the sample docs in ./docs/
"""

import sys
import os
import json

sys.path.insert(0, os.path.dirname(__file__))
from server import search_docs

DOCS_FOLDER = os.path.join(os.path.dirname(__file__), "docs")


def run_tests():
    print("=== Document Search MCP Server — Tool Tests ===\n")

    # Test 1: Search for a term that exists
    print("Test 1: Search for 'billing'")
    result = search_docs("billing")
    print(result[:500], "...\n")
    data = json.loads(result)
    assert data["result_count"] > 0
    assert any("billing" in r["file"].lower() or "billing" in r["excerpt"].lower() for r in data["results"])
    print("PASS\n")

    # Test 2: Search in specific folder
    print("Test 2: Search for 'authentication' in docs folder")
    result = search_docs("authentication", DOCS_FOLDER)
    print(result[:500], "...\n")
    data = json.loads(result)
    assert data["result_count"] > 0
    print("PASS\n")

    # Test 3: Case-insensitive match
    print("Test 3: Case-insensitive search (WEBHOOK vs webhook)")
    result = search_docs("WEBHOOK")
    print(result[:500], "...\n")
    data = json.loads(result)
    assert data["result_count"] > 0
    print("PASS\n")

    # Test 4: No results
    print("Test 4: Search for something that doesn't exist")
    result = search_docs("xyzzy_no_match_9999")
    print(result)
    assert "No results found" in result
    print("PASS\n")

    # Test 5: Empty query
    print("Test 5: Empty query")
    result = search_docs("")
    print(result)
    assert "Error" in result
    print("PASS\n")

    # Test 6: Non-existent folder
    print("Test 6: Non-existent folder")
    result = search_docs("anything", "/tmp/this_folder_definitely_does_not_exist_12345")
    print(result)
    assert "not found" in result.lower() or "Folder not found" in result
    print("PASS\n")

    # Test 7: Excerpt contains surrounding context
    print("Test 7: Result excerpt contains multi-line context")
    result = search_docs("rate limit")
    data = json.loads(result)
    first_excerpt = data["results"][0]["excerpt"]
    print(f"Excerpt: {first_excerpt[:200]}\n")
    assert len(first_excerpt.splitlines()) > 1, "Expected multi-line context"
    print("PASS\n")

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
