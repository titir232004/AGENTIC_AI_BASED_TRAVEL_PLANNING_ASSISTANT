from langchain_community.llms import Ollama
import re
from tools.flight_tool import search_flights
from tools.hotel_tool import recommend_hotel
from tools.places_tool import discover_places
from tools.weather_tool import get_weather
from tools.budget_tool import estimate_budget

# Local LLM (FREE, no API key)
llm = Ollama(model="llama3")


def extract_trip_days(query: str) -> int:
    """Extract number of days from user query. Defaults to 3."""
    match = re.search(r'(\d+)\s*day', query.lower())
    if match:
        return int(match.group(1))
    return 3


def extract_cities(user_query: str):
    """
    Extract source and destination cities using LLM reasoning.
    Returns a tuple: (source, destination)
    """
    prompt = f"""
You are a travel assistant.

Extract source city and destination city from the user query.

Query:
"{user_query}"

Respond ONLY in JSON format:
{{"source": "<city>", "destination": "<city>"}}
"""

    response = llm.invoke(prompt)

    try:
        data = eval(response)
        return data["source"], data["destination"]
    except Exception:
        return None, None


def run_travel_agent(user_query: str, nights: int = 3):
    """Main function to plan a trip based on user query."""
    print("🧠 Understanding user request...")

    source, destination = extract_cities(user_query)
    if not source or not destination:
        return "❌ Could not understand the cities."

    print(f"📍 Source: {source}, Destination: {destination}")

    print("✈️ Searching flights...")
    flight = search_flights(source, destination)

    print("🏨 Finding hotels...")
    hotel = recommend_hotel(destination, max_price=5000)

    print("📍 Discovering places...")
    places = discover_places(destination)

    print("🌦️ Fetching weather...")
    # You might want to update these lat/lon values dynamically
    weather = get_weather(15.2993, 74.1240)

    print("💰 Estimating budget...")
    days = extract_trip_days(user_query)
    nights = max(days - 1, 1)
    budget = estimate_budget(
        flight["price"],
        hotel["price_per_night"],
        nights=nights
    )

    return {
        "source": source,
        "destination": destination,
        "days": days,
        "nights": nights,
        "flight": flight,
        "hotel": hotel,
        "places": places,
        "weather": weather,
        "budget": budget
    }


if __name__ == "__main__":
    result = run_travel_agent(
        "Plan a 3-day trip from Delhi to Kolkata under 20000"
    )
    print("\n✅ FINAL OUTPUT:")
    print(result)
