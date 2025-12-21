# utils/parsing.py
import json
from pathlib import Path
from typing import List
from .schemas import Flight, Hotel, Place

BASE = Path(__file__).resolve().parents[1]
DATA_DIR = BASE / "data"

def load_json_file(filename: str):
    path = DATA_DIR / filename
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_flights() -> List[Flight]:
    raw = load_json_file("flights.json")
    return [Flight.parse_obj(r) for r in raw]

def load_hotels() -> List[Hotel]:
    raw = load_json_file("hotels.json")
    return [Hotel.parse_obj(r) for r in raw]

def load_places() -> List[Place]:
    raw = load_json_file("places.json")
    return [Place.parse_obj(r) for r in raw]
