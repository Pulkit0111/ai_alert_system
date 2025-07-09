import requests
from config import weather_api_key

def fetch_weather_alerts(location: str):
    url = (
        f"https://api.weatherapi.com/v1/forecast.json"
        f"?key={weather_api_key}&q={location}&days=1&alerts=yes"
    )

    try:
        response = requests.get(url)
        data = response.json()
        alerts = data.get("alerts", {}).get("alert", [])
        return alerts
    except Exception as e:
        print("❌ Error fetching WeatherAPI alerts:", e)
        return []
