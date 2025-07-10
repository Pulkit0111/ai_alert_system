from utils import (
    fetch_weather_alerts, 
    create_alert_report, 
    display_alerts, 
    fetch_news_alerts, 
    format_news_alerts_nicely,
    fetch_top_stock_alerts,
    format_stock_alerts_pretty
)
from agent_utils import (
    get_latest_log_file,
    read_log_file,
    summarize_alert_log,
    send_telegram_message
)
from colorama import Fore, Style, init

init(autoreset=True)

def main():
    alert_log = "==== ALERT SUMMARY REPORT ====\n"
    
    while True:
        print(f"\n{Fore.CYAN}📊 Real-Time Alert System - Choose an option:")
        print(f"{Fore.YELLOW}1. Weather Alerts")
        print(f"{Fore.YELLOW}2. News Feed Alerts")
        print(f"{Fore.YELLOW}3. Stock Price Alerts")
        print(f"{Fore.YELLOW}4. Exit")
        print(f"{Style.RESET_ALL}{'-'*50}")
        
        choice = input(f"{Fore.BLUE}🧭 Your Choice: ").strip()

        if choice == "1":
            location = input("🗺️ Enter your location (default: Delhi): ").strip() or "Delhi"
            alerts = fetch_weather_alerts(location)
            display_alerts(alerts)
            alert_log += f"\n[Weather Alerts - {location}]"
            for i, alert in enumerate(alerts, 1):
                alert_log += f"""
                    \n🌀 Alert #{i}: {alert.get('event', 'Unknown Event')}
                    \n📅 From: {alert.get('effective', 'N/A')}
                    \n📅 To: {alert.get('expires', 'N/A')}
                    \n📝 Description:\n{alert.get('desc', 'No description provided.')}  
                """
            alert_log += f"\n{'-'*70}"

        elif choice == "2":
            query = input("🔍 Enter topic (default: India): ").strip() or "India"
            articles = fetch_news_alerts(query=query)
            print(format_news_alerts_nicely(articles))
            alert_log += f"\n[News Alerts - {query}]"
            for idx, article in enumerate(articles, 1):
                alert_log += f"""
                    \n📰 News #{idx}
                    \n📅 Published: {article.get("publishedAt", "N/A")}
                    \n🧾 Title: {article.get("title", "N/A")}
                    \n📝 Description: {article.get("description", "N/A")}
                    \n🔗 URL: {article.get("url", "N/A")}
                """
            alert_log += f"\n{'-'*70}"

        elif choice == "3":
            alerts = fetch_top_stock_alerts()
            print(format_stock_alerts_pretty(alerts))
            alert_log += f"\n📈 Stock Price Alerts Summary"
            for i, (symbol, data) in enumerate(alerts.items(), 1):
                alert_log += f"""
                    \n🧾 {i}. {symbol}
                    \n💵 Latest: ${data['latest_close']}
                    \n📊 Previous: ${data['previous_close']}
                    \n📉 Change: {data['change']} ({data['percent_change']}%)
                    \n{"⚠️ Significant movement!" if data['alert_needed'] else "✅ Normal movement"}
                """
            alert_log += f"\n{'-'*65}"
            

        elif choice.lower() == "4":
            print(f"\n{Fore.YELLOW}📝 Generating final report...")
            path = create_alert_report(alert_log)
            print(f"{Fore.GREEN}✅ Report saved to: {path}")
            log_content = read_log_file(path)
            log_summary = summarize_alert_log(log_content)
            send_telegram_message(log_summary)
            print(f"{Fore.CYAN}👋 Exiting. Stay safe and informed!\n")
            break

        else:
            print(f"{Fore.RED}❌ Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()