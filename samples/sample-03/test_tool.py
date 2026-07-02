"""
test_tool.py — Unit test for get_repo_stats (no Claude required)
Run: python test_tool.py

Note: Makes real HTTP calls to the GitHub public API.
Rate limit: 60 requests/hour without a token.
"""

import sys
import os
import json

sys.path.insert(0, os.path.dirname(__file__))
from server import get_repo_stats


def run_tests():
    print("=== GitHub Stats MCP Server — Tool Tests ===\n")
    print("Note: these tests call the real GitHub API.\n")

    # Test 1: Well-known public repo
    print("Test 1: anthropics/anthropic-sdk-python")
    result = get_repo_stats("anthropics/anthropic-sdk-python")
    print(result)
    data = json.loads(result)
    assert data["repo"] == "anthropics/anthropic-sdk-python"
    assert isinstance(data["stars"], int) and data["stars"] >= 0
    assert isinstance(data["open_issues"], int)
    assert data["last_commit_date"] != "unknown"
    assert "language" in data
    print("PASS\n")

    # Test 2: Another well-known repo
    print("Test 2: python/cpython")
    result = get_repo_stats("python/cpython")
    print(result)
    data = json.loads(result)
    assert data["language"] == "Python"
    print("PASS\n")

    # Test 3: Invalid format
    print("Test 3: Invalid format (no slash)")
    result = get_repo_stats("notarepo")
    print(result)
    assert "Invalid repo format" in result
    print("PASS\n")

    # Test 4: Non-existent repo
    print("Test 4: Non-existent repo")
    result = get_repo_stats("definitelydoesnotexist99999/fakerepo12345")
    print(result)
    assert "not found" in result.lower() or "error" in result.lower()
    print("PASS\n")

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
