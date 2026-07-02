# MCP Server: Weather (API Wrapper)
# Connects to Claude Desktop — no ANTHROPIC_API_KEY needed
# Uses your Claude.ai subscription via Claude Desktop
#
# This is a WORKING example. Clone it, run it, see it work. It wraps the free
# Open-Meteo weather API (no signup, no API key) so Claude can answer real
# weather questions instead of guessing. Only the Python standard library and
# the `mcp` package are used.

import json
import urllib.parse
import urllib.request
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

# Open-Meteo's weather_code is a number. This small dictionary turns the most
# common codes into plain-English conditions a person (and Claude) can read.
WEATHER_CODES = {
    0: "Clear",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Fog",
    51: "Drizzle",
    53: "Drizzle",
    55: "Drizzle",
    61: "Rain",
    63: "Rain",
    65: "Rain",
    71: "Snow",
    73: "Snow",
    75: "Snow",
    80: "Rain showers",
    81: "Rain showers",
    82: "Rain showers",
    95: "Thunderstorm",
}


def _get_json(url: str) -> dict:
    """Fetch a URL and return the parsed JSON. Times out after 10 seconds so the
    server never hangs waiting on the network."""
    with urllib.request.urlopen(url, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))


def _geocode(city: str) -> dict:
    """Turn a city name (e.g. "Berlin") into latitude/longitude using
    Open-Meteo's free geocoding API. Returns a dict with 'lat', 'lon' and the
    resolved 'name', or raises ValueError if the city can't be found."""
    # quote() makes the city name safe to drop into a URL (handles spaces, etc.)
    query = urllib.parse.quote(city)
    url = (
        "https://geocoding-api.open-meteo.com/v1/search"
        f"?name={query}&count=1"
    )
    data = _get_json(url)
    results = data.get("results")
    if not results:
        raise ValueError(f"Could not find a city called '{city}'.")
    top = results[0]
    return {
        "lat": top["latitude"],
        "lon": top["longitude"],
        "name": top["name"],
    }


@mcp.tool()
def get_weather(city: str) -> dict:
    """Get the CURRENT weather for a city.

    Returns a dict with the city name, temperature (°C), a plain-English
    condition and the humidity (%). Example:
    {"city": "Berlin", "temp": 18.2, "condition": "Partly cloudy", "humidity": 61}
    """
    try:
        place = _geocode(city)
        # Ask Open-Meteo for the current temperature, humidity and weather code.
        url = (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={place['lat']}&longitude={place['lon']}"
            "&current=temperature_2m,relative_humidity_2m,weather_code"
            "&timezone=auto"
        )
        data = _get_json(url)
        current = data["current"]
        code = current["weather_code"]
        return {
            "city": place["name"],
            "temp": current["temperature_2m"],
            "condition": WEATHER_CODES.get(code, "Unknown"),
            "humidity": current["relative_humidity_2m"],
        }
    except ValueError as e:
        # City not found — return a friendly message instead of crashing.
        return {"error": str(e)}
    except Exception as e:
        # Any network / parsing problem ends up here.
        return {"error": f"Could not fetch weather for '{city}': {e}"}


@mcp.tool()
def get_forecast(city: str, days: int = 3) -> list:
    """Get a multi-day forecast (daily high/low) for a city.

    `days` is clamped to between 1 and 7. Returns a list of dicts like:
    [{"date": "2026-06-28", "high": 24.1, "low": 14.3}, ...]
    """
    try:
        # Keep days within the range Open-Meteo supports (1 to 7).
        days = max(1, min(7, days))
        place = _geocode(city)
        url = (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={place['lat']}&longitude={place['lon']}"
            "&daily=temperature_2m_max,temperature_2m_min"
            f"&forecast_days={days}&timezone=auto"
        )
        data = _get_json(url)
        daily = data["daily"]
        # The API returns parallel lists (dates, highs, lows). Zip them together
        # into one tidy row per day.
        forecast = []
        for date, high, low in zip(
            daily["time"],
            daily["temperature_2m_max"],
            daily["temperature_2m_min"],
        ):
            forecast.append({"date": date, "high": high, "low": low})
        return forecast
    except ValueError as e:
        return [{"error": str(e)}]
    except Exception as e:
        return [{"error": f"Could not fetch forecast for '{city}': {e}"}]


if __name__ == "__main__":
    mcp.run()
