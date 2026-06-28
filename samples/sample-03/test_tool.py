"""
test_tool.py — Manual test scaffold for your MCP tools (no Claude required)
Run: python test_tool.py
TODO: Add your own test cases after implementing server.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from server import list_tasks, add_task, complete_task


def run_tests():
    print("=== Task Manager MCP Server — Tool Tests ===\n")

    # TODO: Test 1 — add a task
    # result = add_task("TODO: a test task title")
    # print(result)
    # assert "id" in result
    # print("PASS\n")

    # TODO: Test 2 — list tasks
    # result = list_tasks()
    # print(result)
    # assert len(result) > 0
    # print("PASS\n")

    # TODO: Test 3 — complete a task
    # result = complete_task(TODO: use the id from Test 1)
    # print(result)
    # assert result == "ok"
    # print("PASS\n")

    print("TODO: Add your test cases above, then run this file to verify your implementation.")


if __name__ == "__main__":
    run_tests()
