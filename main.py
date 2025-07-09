from data_sources.weather_api import fetch_weather_alerts
from colorama import Fore, Style, init

init(autoreset=True)

def display_alerts(alerts):
    print(f"\n{Fore.YELLOW}⚠️ Weather Alerts from WeatherAPI")
    print(f"{Fore.MAGENTA}{'='*70}")
    for i, alert in enumerate(alerts, 1):
        print(f"{Fore.RED}🌀 Alert #{i}: {alert.get('event', 'Unknown Event')}")
        print(f"{Fore.CYAN}📅 From: {alert.get('effective', 'N/A')}")
        print(f"{Fore.CYAN}📅 To: {alert.get('expires', 'N/A')}")
        print(f"{Fore.CYAN}📝 Description:\n{Fore.WHITE}{alert.get('desc', 'No description provided.')[:400]}")

        # Debug raw alert (optional)
        # print(f"{Fore.LIGHTBLACK_EX}🔍 Raw alert: {alert}")

        print(f"{Fore.MAGENTA}{'-'*70}")

def main():
    print(f"{Fore.CYAN}🌦️ Checking weather alerts...")
    alerts = fetch_weather_alerts()

    if alerts:
        display_alerts(alerts)
    else:
        print(f"{Fore.GREEN}✅ No weather alerts at the moment.")

if __name__ == "__main__":
    main()
