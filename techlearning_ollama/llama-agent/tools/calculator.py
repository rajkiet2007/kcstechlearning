from langchain.tools import tool

@tool
def calculator(query: str) -> str:
    """Perform mathematical calculations"""
    try:
        return str(eval(query))
    except Exception:
        return "Calculation error"