from langchain_core.tools import tool

@tool
def get_weather(city: str) -> str:
    """Get weather for a city"""
    return f"The weather in {city} is 30°C and sunny (mock data)"