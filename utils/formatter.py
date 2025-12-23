from datetime import datetime

def format_trip_output(result: dict) -> str:
    flight = result["flight"]
    hotel = result["hotel"]
    places = result["places"]
    weather = result["weather"]
    budget = result["budget"]

    # ---- Flight ----
    flight_text = (
        f"- {flight.get('airline', 'N/A')} "
        f"(₹{flight.get('price', 0)})"
    )

    if flight.get("departure_time"):
        dep_time = datetime.fromisoformat(
            flight["departure_time"]
        ).strftime("%H:%M")
        flight_text += f" – Departs at {dep_time}"

    # ---- Hotel ----
    hotel_text = (
        f"- {hotel['hotel_name']} "
        f"(₹{hotel['price_per_night']}/night, "
        f"{hotel.get('rating', 0)}-star)"
    )

    # ---- Weather ----
    weather_text = "\n".join(
        [f"- Day {i+1}: {temp}"
         for i, temp in enumerate(weather.values())]
    )

    # ---- Itinerary ----
    itinerary = ""
    day = 1
    for i in range(0, len(places), 2):
        day_places = places[i:i+2]
        names = ", ".join(p["name"] for p in day_places)
        itinerary += f"Day {day}: {names}\n"
        day += 1

    # ---- Final Output ----
    return f"""
Your {result['days']}-Day Trip to {result['destination']}

Flight Selected:
{flight_text}

Hotel Booked:
{hotel_text}

Weather:
{weather_text}

Itinerary:
{itinerary.strip()}

Estimated Total Budget:
- Flight: ₹{budget['flight']}
- Hotel: ₹{budget['hotel']}
- Food & Travel: ₹{budget['food_and_local']}
-------------------------------------
Total Cost: ₹{budget['total_cost']}
""".strip()
