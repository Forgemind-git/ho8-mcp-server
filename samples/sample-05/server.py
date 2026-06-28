# MCP Server: Document Search
# Connects to Claude Desktop — no ANTHROPIC_API_KEY needed
# Uses your Claude.ai subscription via Claude Desktop
#
# It gives Claude two tools:
#   - search_docs(query): find which documents mention a word or phrase
#   - read_doc(filename): read the full text of one document
#
# The documents live in the "docs/" folder next to this file. Drop in any
# .txt or .md files and Claude will be able to search them.

import os
from mcp.server.fastmcp import FastMCP

# Create the MCP server. "doc-search" is the name Claude Desktop will show.
mcp = FastMCP("doc-search")

# The folder we search. By default it's the "docs" folder next to this file.
DOCS_FOLDER = os.path.join(os.path.dirname(__file__), "docs")

# Only these file types are treated as searchable documents.
ALLOWED_EXTENSIONS = (".txt", ".md")


def _read_file_safely(path):
    """Read a text file and return its contents, or None if it can't be read."""
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except Exception:
        # Unreadable file (permissions, etc.) — skip it gracefully.
        return None


@mcp.tool()
def search_docs(query: str) -> list:
    """Search all documents for a word or phrase (case-insensitive).

    Returns a list of matches. Each match is a dict with:
      - filename: the document's name (e.g. "billing.md")
      - snippet:  a short ~150 character window around the first match
      - path:     the document's path relative to the docs folder

    Returns an empty list if nothing matches.
    """
    results = []
    needle = query.lower()  # what we're looking for, lowercased

    # Walk through every file in the docs folder (and any sub-folders).
    for root, _dirs, files in os.walk(DOCS_FOLDER):
        for name in files:
            # Only look at .txt and .md files.
            if not name.lower().endswith(ALLOWED_EXTENSIONS):
                continue

            full_path = os.path.join(root, name)
            text = _read_file_safely(full_path)
            if text is None:
                continue  # couldn't read it — move on

            # Case-insensitive substring search.
            position = text.lower().find(needle)
            if position == -1:
                continue  # this file doesn't mention the query

            # Build a ~150-character window centered on the first match.
            start = max(0, position - 60)
            end = min(len(text), position + len(query) + 90)
            snippet = text[start:end].strip().replace("\n", " ")
            if start > 0:
                snippet = "..." + snippet
            if end < len(text):
                snippet = snippet + "..."

            results.append({
                "filename": name,
                "snippet": snippet,
                "path": os.path.relpath(full_path, DOCS_FOLDER),
            })

    # Friendly: if nothing matched, return an empty list.
    return results


@mcp.tool()
def read_doc(filename: str) -> dict:
    """Read the full text of one document by its filename.

    Returns {"filename": ..., "content": ...} on success,
    or {"error": ...} if no document with that name exists.
    """
    target = os.path.basename(filename)  # ignore any folder parts in the input

    # Look for a file whose basename matches (case-insensitive).
    for root, _dirs, files in os.walk(DOCS_FOLDER):
        for name in files:
            if name.lower() == target.lower():
                text = _read_file_safely(os.path.join(root, name))
                if text is None:
                    return {"error": f"Could not read document '{filename}'"}
                return {"filename": name, "content": text}

    # No matching file found.
    return {"error": f"No document named '{filename}'"}


# Start the server when run directly (this is what Claude Desktop launches).
if __name__ == "__main__":
    mcp.run()
