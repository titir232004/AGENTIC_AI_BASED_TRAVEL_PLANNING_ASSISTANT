import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "data", "flights.json")


def search_flights(source, destination):
    with open(DATA_FILE, "r") as f:
        flights = json.load(f)

    matches = []

    for flight in flights:
        from_city = flight.get("source") or flight.get("from")
        to_city = flight.get("destination") or flight.get("to")

        if not from_city or not to_city:
            continue

        if from_city.lower() == source.lower() and to_city.lower() == destination.lower():
            matches.append(flight)

    if not matches:
        return {
            "airline": "N/A",
            "price": 0
        }

    return min(matches, key=lambda x: x.get("price", 999999))
