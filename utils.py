import requests
import os
from dotenv import load_dotenv
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

load_dotenv()

weather_api_key = os.getenv("WEATHER_API_KEY")

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

def create_alert_report(alert_log: str, output_dir: str = "logs"):
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"alert_summary_{timestamp}.txt"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w") as f:
        f.write(alert_log)

    return filepath

def display_alerts(alerts):
    print(f"\n{Fore.YELLOW}⚠️ Weather Alerts from WeatherAPI")
    print(f"{Fore.MAGENTA}{'='*70}")
    if not alerts:
        print(f"{Fore.GREEN}✅ No active weather alerts for your region.")
        return

    for i, alert in enumerate(alerts, 1):
        print(f"{Fore.RED}🌀 Alert #{i}: {alert.get('event', 'Unknown Event')}")
        print(f"{Fore.CYAN}📅 From: {alert.get('effective', 'N/A')}")
        print(f"{Fore.CYAN}📅 To: {alert.get('expires', 'N/A')}")
        print(f"{Fore.WHITE}📝 Description:\n{alert.get('desc', 'No description provided.')[:400]}...")
        print(f"{Fore.MAGENTA}{'-'*70}")