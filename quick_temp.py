import requests
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TG_BOT_TOKEN")

def get_chat_id():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    resp = requests.get(url)
    data = resp.json()
    print("🔍 Raw getUpdates Response:")
    print(data)

    try:
        messages = data.get("result", [])
        if not messages:
            print("📭 No messages received yet. Send a message to your bot on Telegram.")
            return
        for msg in messages:
            chat_id = msg["message"]["chat"]["id"]
            print(f"✅ Chat ID found: {chat_id}")
            return chat_id
    except Exception as e:
        print("❌ Error extracting chat_id:", e)

get_chat_id()
