"""
Document Search MCP Server
---------------------------
Exposes one tool: search_docs
Search a folder of .txt and .md files for matching passages.
"""

import os
import json
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("doc-search")

# Default docs folder (relative to this file)
DEFAULT_DOCS_FOLDER = os.path.join(os.path.dirname(__file__), "docs")

CONTEXT_LINES = 3   # lines of context to show around a match
MAX_RESULTS = 10    # cap results so responses stay readable


def _search_file(filepath: str, query: str) -> list[dict]:
    """Return all matching excerpts from a single file."""
    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            lines = f.readlines()
    except OSError:
        return []

    lower_query = query.lower()
    matches = []
    seen_lines = set()

    for i, line in enumerate(lines):
        if lower_query in line.lower():
            if i in seen_lines:
                continue
            # Extract a context window around the match
            start = max(0, i - CONTEXT_LINES)
            end = min(len(lines), i + CONTEXT_LINES + 1)
            for ln in range(start, end):
                seen_lines.add(ln)

            excerpt = "".join(lines[start:end]).strip()
            matches.append({
                "line": i + 1,
                "excerpt": excerpt,
            })

    return matches


@mcp.tool()
def search_docs(query: str, folder: str = "") -> str:
    """
    Search a folder of .txt and .md files for matching passages.

    Args:
        query: Search query string (case-insensitive substring match).
        folder: Optional absolute or relative path to the docs folder.
                Defaults to the ./docs folder next to server.py.

    Returns:
        JSON list of matching files with the relevant excerpt and line number.
    """
    if not query.strip():
        return "Error: 'query' cannot be empty."

    docs_folder = folder.strip() if folder.strip() else DEFAULT_DOCS_FOLDER

    # Resolve relative paths relative to this file
    if not os.path.isabs(docs_folder):
        docs_folder = os.path.join(os.path.dirname(__file__), docs_folder)

    if not os.path.isdir(docs_folder):
        return f"Folder not found: '{docs_folder}'. Create it and add .txt or .md files."

    results = []
    for root, _dirs, files in os.walk(docs_folder):
        for filename in sorted(files):
            if not (filename.endswith(".txt") or filename.endswith(".md")):
                continue
            filepath = os.path.join(root, filename)
            file_matches = _search_file(filepath, query)
            for match in file_matches:
                rel_path = os.path.relpath(filepath, docs_folder)
                results.append({
                    "file": rel_path,
                    "line": match["line"],
                    "excerpt": match["excerpt"],
                })
                if len(results) >= MAX_RESULTS:
                    break
        if len(results) >= MAX_RESULTS:
            break

    if not results:
        return f"No results found for '{query}' in {docs_folder}."

    return json.dumps({
        "query": query,
        "folder": docs_folder,
        "result_count": len(results),
        "results": results,
    }, indent=2)


if __name__ == "__main__":
    print("Starting Document Search MCP server...")
    print(f"Default docs folder: {DEFAULT_DOCS_FOLDER}")
    mcp.run()
