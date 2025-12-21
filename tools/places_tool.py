import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE_DIR, "data", "places.json")


def discover_places(city):
    with open(DATA) as f:
        places = json.load(f)

    return [
        p for p in places
        if p["city"].lower() == city.lower()
    ][:5]
