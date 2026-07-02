"""
test_tool.py — Unit test for manage_tasks (no Claude required)
Run: python test_tool.py

Note: Creates and modifies tasks.json in the same folder.
A backup is taken before tests and restored afterwards.
"""

import sys
import os
import json
import shutil

sys.path.insert(0, os.path.dirname(__file__))

TASKS_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")
BACKUP_FILE = TASKS_FILE + ".bak"


def setup():
    """Back up existing tasks.json and start clean."""
    if os.path.exists(TASKS_FILE):
        shutil.copy(TASKS_FILE, BACKUP_FILE)
        os.remove(TASKS_FILE)


def teardown():
    """Remove test tasks.json and restore backup."""
    if os.path.exists(TASKS_FILE):
        os.remove(TASKS_FILE)
    if os.path.exists(BACKUP_FILE):
        shutil.move(BACKUP_FILE, TASKS_FILE)


def run_tests():
    from server import manage_tasks

    print("=== Task Manager MCP Server — Tool Tests ===\n")
    setup()

    try:
        # Test 1: List when empty
        print("Test 1: List empty task list")
        result = manage_tasks("list")
        print(result)
        assert "No tasks yet" in result
        print("PASS\n")

        # Test 2: Add a task
        print("Test 2: Add 'Write the course README'")
        result = manage_tasks("add", "Write the course README")
        print(result)
        assert "Task added" in result
        assert "[1]" in result
        print("PASS\n")

        # Test 3: Add another task
        print("Test 3: Add 'Record intro video'")
        result = manage_tasks("add", "Record intro video")
        print(result)
        assert "Task added" in result
        assert "[2]" in result
        print("PASS\n")

        # Test 4: List tasks
        print("Test 4: List tasks")
        result = manage_tasks("list")
        print(result)
        assert "Write the course README" in result
        assert "Record intro video" in result
        assert "TODO" in result
        print("PASS\n")

        # Test 5: Complete by ID
        print("Test 5: Complete task 1 by ID")
        result = manage_tasks("complete", "1")
        print(result)
        assert "Task completed" in result
        print("PASS\n")

        # Test 6: Complete by title fragment
        print("Test 6: Complete 'intro video' by title fragment")
        result = manage_tasks("complete", "intro video")
        print(result)
        assert "Task completed" in result
        print("PASS\n")

        # Test 7: List shows DONE
        print("Test 7: List shows both tasks as DONE")
        result = manage_tasks("list")
        print(result)
        assert result.count("DONE") == 2
        print("PASS\n")

        # Test 8: Complete already done
        print("Test 8: Complete already-done task")
        result = manage_tasks("complete", "1")
        print(result)
        assert "already completed" in result
        print("PASS\n")

        # Test 9: Invalid action
        print("Test 9: Invalid action")
        result = manage_tasks("delete")
        print(result)
        assert "Unknown action" in result
        print("PASS\n")

        # Test 10: Add with no title
        print("Test 10: Add with no title")
        result = manage_tasks("add", "")
        print(result)
        assert "Error" in result
        print("PASS\n")

        print("All tests passed!")
    finally:
        teardown()


if __name__ == "__main__":
    run_tests()
