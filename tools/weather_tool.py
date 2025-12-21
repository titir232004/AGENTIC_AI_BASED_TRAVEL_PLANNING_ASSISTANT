import requests


def get_weather(lat, lon):
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        "&daily=temperature_2m_max"
        "&timezone=auto"
    )

    r = requests.get(url).json()
    temps = r["daily"]["temperature_2m_max"]

    return {
        "day_1": f"{temps[0]}°C",
        "day_2": f"{temps[1]}°C",
        "day_3": f"{temps[2]}°C"
    }
