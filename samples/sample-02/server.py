# MCP Server: API Wrapper (Weather)
# Connects to Claude Desktop — no ANTHROPIC_API_KEY needed
# Uses your Claude.ai subscription via Claude Desktop

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("TODO: name your MCP server")

# TODO: Set up your API client here
# This sample uses the Open-Meteo free weather API (no key required)
# Docs: https://open-meteo.com/en/docs
# You'll need to: 1) geocode the city name to lat/lon, 2) call the weather endpoint


@mcp.tool()
def get_weather(city: str) -> dict:
    """TODO: describe what this tool does and what it returns"""
    # TODO: implement this tool
    # It should call the Open-Meteo API and return a dict like:
    # {"temp": 22, "condition": "Partly cloudy", "humidity": 65}
    raise NotImplementedError("TODO: implement get_weather")


@mcp.tool()
def get_forecast(city: str, days: int) -> list:
    """TODO: describe what this tool does and what it returns"""
    # TODO: implement this tool
    # It should return a list of dicts like:
    # [{"date": "2024-01-15", "high": 25, "low": 18}]
    raise NotImplementedError("TODO: implement get_forecast")


if __name__ == "__main__":
    mcp.run()
