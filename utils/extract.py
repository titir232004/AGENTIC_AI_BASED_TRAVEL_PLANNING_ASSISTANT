import re

def extract_trip_details(query: str):
    query = query.lower()

    city_match = re.search(
        r"from\s+([a-z\s]+?)\s+to\s+([a-z\s]+?)(?:\s+under|\s+within|\s+below|$)",
        query
    )

    if not city_match:
        return None

    source = city_match.group(1).strip().title()
    destination = city_match.group(2).strip().title()

    day_match = re.search(r"(\d+)\s*day", query)
    days = int(day_match.group(1)) if day_match else 3
    nights = max(days - 1, 1)

    budget_match = re.search(r"(under|within|below)\s*(\d+)", query)
    budget = int(budget_match.group(2)) if budget_match else None

    return {
        "source": source,
        "destination": destination,
        "days": days,
        "nights": nights,
        "budget": budget
    }
