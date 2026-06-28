"""
test_tool.py — Manual test scaffold for your MCP tools (no Claude required)
Run: python test_tool.py
TODO: Add your own test cases after implementing server.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from server import get_weather, get_forecast


def run_tests():
    print("=== API Wrapper MCP Server — Tool Tests ===\n")

    # TODO: Test 1 — get weather for a city
    # result = get_weather("TODO: a city name")
    # print(result)
    # assert "temp" in result
    # print("PASS\n")

    # TODO: Test 2 — get forecast
    # result = get_forecast("TODO: a city name", 3)
    # print(result)
    # assert len(result) == 3
    # print("PASS\n")

    print("TODO: Add your test cases above, then run this file to verify your implementation.")


if __name__ == "__main__":
    run_tests()
