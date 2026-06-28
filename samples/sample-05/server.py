# MCP Server: Document Search
# Connects to Claude Desktop — no ANTHROPIC_API_KEY needed
# Uses your Claude.ai subscription via Claude Desktop

import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("TODO: name your MCP server")

# TODO: Set up your docs folder path here
# DOCS_FOLDER = os.path.join(os.path.dirname(__file__), "sample-data")
# This should point to the folder containing your .txt and .md files


@mcp.tool()
def search_docs(query: str) -> list:
    """TODO: describe what this tool does and what it returns"""
    # TODO: implement this tool
    # It should walk DOCS_FOLDER looking for .txt and .md files,
    # search each file for the query string (case-insensitive),
    # and return a list like:
    # [{"filename": "...", "snippet": "...", "path": "..."}]
    raise NotImplementedError("TODO: implement search_docs")


@mcp.tool()
def read_doc(filename: str) -> dict:
    """TODO: describe what this tool does and what it returns"""
    # TODO: implement this tool
    # It should find the file by name in DOCS_FOLDER and return:
    # {"content": "<full text of the file>"}
    raise NotImplementedError("TODO: implement read_doc")


if __name__ == "__main__":
    mcp.run()
