from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for general information (mock implementation)"""
    return f"Search results for: {query}"