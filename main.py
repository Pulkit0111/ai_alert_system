from data_sources.weather_api import fetch_weather_alerts
from colorama import Fore, Style, init

init(autoreset=True)

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
        print(f"{Fore.WHITE}📝 Description:\n{alert.get('desc', 'No description provided.')[:400]}")
        print(f"{Fore.MAGENTA}{'-'*70}")

def get_location_input():
    print(f"{Fore.CYAN}📍 Please enter your location (e.g., Delhi or 28.61,77.20):")
    location = input("🗺️ Location: ").strip()
    return location if location else "Delhi"

def main():
    print(f"{Fore.CYAN}{'═'*60}")
    print(f"🌤️  Weather Alert Terminal App")
    print(f"{Fore.CYAN}{'═'*60}")

    location = get_location_input()

    print(f"\n📡 Fetching alerts for {Fore.YELLOW}{location}...")
    alerts = fetch_weather_alerts(location)

    display_alerts(alerts)

    print(f"\n{Fore.GREEN}🏁 Done. Stay safe!")
    print(f"{Fore.CYAN}{'═'*60}")

if __name__ == "__main__":
    main()
