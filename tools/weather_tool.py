import requests

def get_weather(city: str):
    geo_url = (
        f"https://geocoding-api.open-meteo.com/v1/search"
        f"?name={city}&count=1"
    )
    geo_res = requests.get(geo_url).json()

    if "results" not in geo_res:
        return {"error": "Location not found"}

    lat = geo_res["results"][0]["latitude"]
    lon = geo_res["results"][0]["longitude"]

    weather_url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        "&daily=temperature_2m_max"
        "&timezone=auto"
    )
    weather_res = requests.get(weather_url).json()

    temps = weather_res["daily"]["temperature_2m_max"]

    return {
        "day_1": f"{temps[0]}°C",
        "day_2": f"{temps[1]}°C",
        "day_3": f"{temps[2]}°C"
    }
