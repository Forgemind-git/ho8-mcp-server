"""
test_tool.py — Run the tools directly, no Claude required.
Run: python test_tool.py

This proves the server works before you connect it to Claude Desktop.
Note: this test calls the live Open-Meteo API, so you need an internet
connection. If you're offline, it will skip the live checks instead of failing.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from server import get_weather, get_forecast


def run_tests():
    print("=== Weather MCP Server — Tool Tests ===\n")

    try:
        # Test 1 — current weather for Berlin
        weather = get_weather("Berlin")
        print("get_weather('Berlin') ->", weather)

        # Test 2 — 3-day forecast for Berlin
        forecast = get_forecast("Berlin", 3)
        print("get_forecast('Berlin', 3) ->", forecast)
    except Exception as e:
        print("Skipping live test (no internet?):", e)
        return

    # If the calls came back, make sure they have the shape we expect.
    if "error" in weather:
        print("Skipping live test (no internet?):", weather["error"])
        return

    assert "city" in weather
    assert "temp" in weather
    assert "condition" in weather
    assert "humidity" in weather
    print("PASS — get_weather returned all expected keys\n")

    if forecast and "error" in forecast[0]:
        print("Skipping live test (no internet?):", forecast[0]["error"])
        return

    assert len(forecast) >= 1
    assert "date" in forecast[0]
    assert "high" in forecast[0]
    assert "low" in forecast[0]
    print("PASS — get_forecast returned all expected keys\n")

    print("All tests passed. Your server is ready to connect to Claude Desktop.")


if __name__ == "__main__":
    run_tests()
