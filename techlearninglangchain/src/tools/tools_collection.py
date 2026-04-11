from langchain_core.tools import tool
class Tools:
    def __init__(self):
        self.tools = {}

    @tool("web_search", description="Search the web for information.")  # Custom name
    def search(query: str) -> str:
        """Search the web for information."""
        # return f"Results for: {query}"
        return "Current temperature in the city is 25°C with clear skies."

    @tool("get_city_weather", description="Get the current weather information for a specified city.")
    def get_city_wheather(city: str) -> str:
        # Implement your logic to get weather information for the specified city
        return f"The current weather in {city} is sunny with a temperature of 25°C."

    @tool("suggest_clothing", description="Suggest appropriate clothing based on the weather.")
    def suggest_clothing(weather: str) -> str:
        # Implement your logic to suggest clothing based on the weather
        if "sunny" in weather:
            return "It's sunny outside. You might want to wear light clothing and sunglasses."
        elif "rainy" in weather:
            return "It's rainy outside. You should consider wearing a raincoat and carrying an umbrella."
        else:
            return "The weather is moderate. Dress comfortably and check for updates later."
        
    