from data_sources.weather_api import fetch_weather_alerts
from colorama import Fore, Style, init

init(autoreset=True)

def display_alerts(alerts):
    print(f"\n{Fore.YELLOW}⚠️ Weather Alerts Found!")
    print(f"{Fore.MAGENTA}{'='*60}")
    for alert in alerts:
        print(f"{Fore.RED}🌀 Event: {alert.get('event')}")
        print(f"{Fore.WHITE}📅 From: {alert.get('start')}")
        print(f"📅 To: {alert.get('end')}")
        print(f"📄 Description:\n{alert.get('description')}\n")
        print(f"{Fore.MAGENTA}{'-'*60}")

def main():
    print(f"{Fore.CYAN}🌦️ Checking weather alerts...")
    alerts = fetch_weather_alerts()

    if alerts:
        display_alerts(alerts)
    else:
        print(f"{Fore.GREEN}✅ No weather alerts at the moment.")

if __name__ == "__main__":
    main()
