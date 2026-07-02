"""
GitHub Stats MCP Server
-----------------------
Exposes one tool: get_repo_stats
Get star count, open issue count, and last commit date for any public GitHub repo.
"""

import json
import urllib.request
import urllib.error
from datetime import datetime
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("github-stats")


@mcp.tool()
def get_repo_stats(repo: str) -> str:
    """
    Get star count, open issue count, and last commit date for any public GitHub repo.

    Args:
        repo: Repository in owner/repo format, e.g. 'anthropics/anthropic-sdk-python'.

    Returns:
        stars, open_issues, last_commit_date, and language as JSON.
    """
    repo = repo.strip().strip("/")

    if repo.count("/") != 1:
        return f"Invalid repo format '{repo}'. Use owner/repo, e.g. 'anthropics/anthropic-sdk-python'."

    owner, name = repo.split("/", 1)

    # ---- Fetch repo metadata from GitHub public API (no auth needed) ----
    repo_url = f"https://api.github.com/repos/{owner}/{name}"
    commits_url = f"https://api.github.com/repos/{owner}/{name}/commits?per_page=1"

    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "mcp-github-stats/1.0",
    }

    try:
        # Fetch repo info
        req = urllib.request.Request(repo_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            repo_data = json.loads(resp.read().decode())

        stars = repo_data.get("stargazers_count", 0)
        open_issues = repo_data.get("open_issues_count", 0)
        language = repo_data.get("language") or "unknown"

        # Fetch last commit date
        req2 = urllib.request.Request(commits_url, headers=headers)
        with urllib.request.urlopen(req2, timeout=10) as resp2:
            commits = json.loads(resp2.read().decode())

        last_commit_date = "unknown"
        if commits:
            raw_date = commits[0]["commit"]["committer"]["date"]
            # Parse ISO 8601 and reformat nicely
            try:
                dt = datetime.strptime(raw_date, "%Y-%m-%dT%H:%M:%SZ")
                last_commit_date = dt.strftime("%Y-%m-%d")
            except ValueError:
                last_commit_date = raw_date[:10]

        return json.dumps({
            "repo": f"{owner}/{name}",
            "stars": stars,
            "open_issues": open_issues,
            "last_commit_date": last_commit_date,
            "language": language,
        }, indent=2)

    except urllib.error.HTTPError as e:
        if e.code == 404:
            return f"Repository '{repo}' not found. Check that it's public and the name is correct."
        elif e.code == 403:
            return "GitHub API rate limit exceeded. Wait a minute and try again (or add a GitHub token)."
        else:
            return f"GitHub API error: HTTP {e.code} — {e.reason}"
    except urllib.error.URLError as e:
        return f"Network error reaching GitHub API: {e.reason}"
    except Exception as e:
        return f"Unexpected error: {e}"


if __name__ == "__main__":
    print("Starting GitHub Stats MCP server...")
    mcp.run()
