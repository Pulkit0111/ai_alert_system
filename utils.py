import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from colorama import Fore, Style, init

init(autoreset=True)

load_dotenv()

weather_api_key = os.getenv("WEATHER_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")
tweleve_data_api_key = os.getenv("TWELVE_DATA_API_KEY")

TOP_5_STOCKS = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]

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

def fetch_news_alerts(query="India", max_results=5):
    print("\n🗞️ Fetching News Alerts...")

    if not news_api_key:
        print("❌ NEWS_API_KEY is missing in environment variables.")
        return []

    base_url = "https://newsapi.org/v2/everything"

    from_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    to_date = datetime.now().strftime("%Y-%m-%d")

    params = {
        "q": query,
        "from": from_date,
        "to": to_date,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": max_results,
        "apiKey": news_api_key,
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        articles = response.json().get("articles", [])
        if not articles:
            print("🔍 No relevant news found.")
        return articles
    except Exception as e:
        print("❌ Failed to fetch news:", e)
        return []

def format_news_alerts_nicely(articles):
    if not articles:
        return "📭 No news alerts available."

    output = "\n🗞️ Latest News Alerts\n" + "="*70 + "\n"
    for idx, article in enumerate(articles, 1):
        output += f"""📰 News #{idx}
📅 Published: {article.get("publishedAt", "N/A")}
🧾 Title: {article.get("title", "N/A")}
📝 Description: {article.get("description", "N/A")}
🔗 URL: {article.get("url", "N/A")}
{"-"*70}
"""
    return output

def fetch_top_stock_alerts(threshold_percent=3.0):
    print("\n📉 Checking Stock Price Alerts for Top 5 Stocks...")
    if not tweleve_data_api_key:
        print("❌ Missing TWELVE_DATA_API_KEY in your .env file.")
        return {}

    base_url = "https://api.twelvedata.com/time_series"
    alerts = {}

    for symbol in TOP_5_STOCKS:
        params = {
            "symbol": symbol,
            "interval": "1day",
            "outputsize": 2,
            "apikey": tweleve_data_api_key
        }

        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            data = response.json()

            if "values" not in data:
                print(f"⚠️ Failed to get data for {symbol}: {data.get('message', 'Unknown error')}")
                continue

            values = data["values"]
            latest = float(values[0]["close"])
            previous = float(values[1]["close"])
            change = latest - previous
            percent_change = (change / previous) * 100
            alert_needed = abs(percent_change) >= threshold_percent

            alerts[symbol] = {
                "symbol": symbol,
                "latest_close": latest,
                "previous_close": previous,
                "change": round(change, 2),
                "percent_change": round(percent_change, 2),
                "alert_needed": alert_needed
            }

        except Exception as e:
            print(f"❌ Error fetching {symbol}: {e}")

    return alerts

def format_stock_alerts_pretty(alerts: dict) -> str:
    if not alerts:
        return "📭 No stock alerts available.\n"

    output = "\n📈 Stock Price Alerts Summary"
    output += "\n" + "=" * 65
    for i, (symbol, data) in enumerate(alerts.items(), 1):
        output += f"""
🧾 {i}. {symbol}
💵 Latest: ${data['latest_close']}
📊 Previous: ${data['previous_close']}
📉 Change: {data['change']} ({data['percent_change']}%)

{"⚠️ Significant movement!" if data['alert_needed'] else "✅ Normal movement"}
{"-" * 65}
"""
    return output
