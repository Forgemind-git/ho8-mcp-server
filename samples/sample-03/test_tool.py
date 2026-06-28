# Quick test for the task-manager tools.
# Run it with:  python test_tool.py
# Note: this writes to the same tasks.db file the server uses — that's fine,
# it just adds and completes one extra test task.

import os
import sys

# Make sure we can import server.py from this same folder.
sys.path.insert(0, os.path.dirname(__file__))

from server import list_tasks, add_task, complete_task


def run_tests():
    print("1. Adding a task...")
    result = add_task("Test task from test_tool")
    assert "id" in result, "add_task should return a dict with an 'id'"
    new_id = result["id"]
    print(f"   Added task with id {new_id}")

    print("2. Listing tasks...")
    tasks = list_tasks()
    assert len(tasks) > 0, "list_tasks should return at least one task"
    print(f"   Got {len(tasks)} task(s)")

    print("3. Completing the task we just added...")
    done = complete_task(new_id)
    assert done == "ok", f"complete_task should return 'ok', got {done!r}"
    print(f"   complete_task returned: {done}")

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
