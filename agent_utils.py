import os
import requests
from openai import OpenAI
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def read_log_file(file_path):
    """Reads the content of a given log file."""
    if not file_path or not os.path.exists(file_path):
        return None
    with open(file_path, "r") as file:
        return file.read()
    
def summarize_alert_log(log_content: str) -> str:
    """Use OpenAI GPT to summarize alerts into actionable insights (new SDK)."""
    if not log_content:
        return "❌ No log content to summarize."

    prompt = f"""
You are an intelligent real-time alert-monitoring assistant. You will receive a system log of weather alerts, news alerts, and stock price alerts. Your task is to generate a clean human-readable summary in 4-6 bullet points:

- Highlight any significant stock movements.
- Call out severe weather events and affected regions.
- Mention any notable news items.
- Conclude with an overall alert level (Low, Medium, High).
- Suggest any actions to be taken.

You need to generate the summary in the following format:
🧠 Agent Summary:
- 🚨 TSLA dropped 6.2% today — possibly due to disappointing Q2 results.
- 🌧️ Heavy rainfall and flooding expected in Mumbai and Pune tomorrow.
- 📰 Top news: Power workers nationwide protest against privatization.
- 🟡 Overall alert level: Medium – Stay alert for flood and stock triggers.

Here is the log:
\"\"\"
{log_content}
\"\"\"
Now generate the summary starting with: "🧠 Agent Summary:"
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"❌ Failed to generate summary: {e}"

def send_telegram_message(message: str):
    token = os.getenv("TG_BOT_TOKEN")
    chat_id = os.getenv("TG_CHAT_ID")

    if not token or not chat_id:
        print("❌ Missing Telegram token or chat ID.")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }

    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("📬 Summary sent to Telegram!")
        else:
            print("❌ Failed to send Telegram message:", response.text)
    except Exception as e:
        print("❌ Error:", e)

