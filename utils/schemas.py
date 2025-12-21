# utils/schemas.py
from pydantic import BaseModel, Field
from typing import Optional, List

class Flight(BaseModel):
    flight_id: str
    airline: str
    source: str = Field(..., alias="from")
    destination: str = Field(..., alias="to")
    departure_time: str
    arrival_time: str
    price: float

    model_config = {
        "validate_by_name": True
    }

class Hotel(BaseModel):
    hotel_id: str
    name: str
    city: str
    stars: Optional[int]
    price_per_night: float
    amenities: Optional[List[str]] = []

    model_config = {
        "validate_by_name": True
    }

class Place(BaseModel):
    place_id: str
    name: str
    city: str
    place_type: str = Field(..., alias="type")
    rating: float

    model_config = {
        "validate_by_name": True
    }
