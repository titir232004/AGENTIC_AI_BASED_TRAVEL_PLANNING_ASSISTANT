import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "data", "hotels.json")


def recommend_hotel(city, max_price):
    with open(DATA_FILE, "r") as f:
        hotels = json.load(f)

    options = []

    for hotel in hotels:
        hotel_city = hotel.get("city")
        price = (
            hotel.get("price_per_night")
            or hotel.get("price")
            or hotel.get("cost")
        )

        if not hotel_city or not price:
            continue

        if hotel_city.lower() == city.lower() and price <= max_price:
            options.append(hotel)

    if not options:
        return {
            "hotel_name": "N/A",
            "price_per_night": 0,
            "rating": 0
        }

    def get_rating(h):
        return (
            h.get("rating")
            or h.get("hotel_rating")
            or h.get("stars")
            or h.get("star_rating")
            or 0
        )

    best = max(options, key=get_rating)

    return {
        "hotel_name": best.get("hotel_name") or best.get("name", "Unknown"),
        "price_per_night": (
            best.get("price_per_night")
            or best.get("price")
            or best.get("cost")
        ),
        "rating": get_rating(best)
    }
