import json
import os
from utils.extract import extract_trip_details
from tools.flight_tool import search_flights
from tools.places_tool import discover_places
from tools.weather_tool import get_weather
from tools.budget_tool import estimate_budget


CITY_FOOD_COST = {
    "Goa": 1000,
    "Delhi": 900,
    "Mumbai": 1000,
    "Kolkata": 800,
    "Bangalore": 900
}

DEFAULT_FOOD_COST = 800


def run_travel_agent(user_query: str):
    details = extract_trip_details(user_query)

    if not details:
        return {"error": "Could not understand your trip details."}

    source = details["source"]
    destination = details["destination"]
    days = details["days"]
    nights = details["nights"]
    budget_limit = details["budget"]

    if not budget_limit:
        return {"error": "Please specify a budget (e.g. under 20000)."}

    #  Robust food + local travel cost
    per_day_food = CITY_FOOD_COST.get(destination, DEFAULT_FOOD_COST)
    food_and_local = per_day_food * days

    # Flight
    flight = search_flights(source, destination)
    flight_price = flight.get("price", 0)

    if flight_price == 0:
        return {"error": f"No flights found from {source} to {destination}."}

    if flight_price >= budget_limit:
        return {"error": "Flight cost alone exceeds your budget."}

    # hotels
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    HOTEL_FILE = os.path.join(BASE_DIR, "data", "hotels.json")

    with open(HOTEL_FILE) as f:
        hotels = json.load(f)

    hotels = sorted(
        [h for h in hotels if h.get("city", "").lower() == destination.lower()],
        key=lambda x: x.get("price_per_night", 999999)
    )

    for hotel in hotels:
        hotel_price = hotel.get("price_per_night", 0)

        budget = estimate_budget(
            flight_price,
            hotel_price,
            nights,
            food_and_local
        )

        if budget["total_cost"] <= budget_limit:
            return {
                "source": source,
                "destination": destination,
                "days": days,
                "nights": nights,
                "flight": flight,
                "hotel": {
                    "hotel_name": hotel.get("name", "Unknown"),
                    "price_per_night": hotel_price,
                    "rating": hotel.get("stars", 0)
                },
                "places": discover_places(destination),
                "weather": get_weather(destination),
                "budget": budget,
                "budget_limit": budget_limit,
                "budget_exceeded": False
            }

    return {
        "error": f"No feasible plan fits within ₹{budget_limit}."
    }
