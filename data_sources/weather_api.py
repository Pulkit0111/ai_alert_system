# data_sources/weather_api.py

import requests
from config import weather_api_key, LOCATION

def fetch_weather_alerts():
    url = (
        f"https://api.weatherapi.com/v1/forecast.json"
        f"?key={weather_api_key}&q={LOCATION}&days=1&alerts=yes"
    )

    try:
        response = requests.get(url)
        data = response.json()

        alerts = data.get("alerts", {}).get("alert", [])
        if alerts:
            return alerts
        else:
            return []
    except Exception as e:
        print("❌ Error fetching weather data:", e)
        return []
