# 🚨 Real-Time Alert System
**Objective**: Build a comprehensive real-time alert monitoring system that tracks multiple data sources (weather, news, stock prices) and provides intelligent AI-powered summaries with automated notifications.

---

## 🎯 Project Goals
You will build a Python application that:

1. **Monitors Multiple Data Sources**:
   - Weather alerts for any location
   - Latest news articles by topic
   - Stock price movements for top 5 stocks

2. **Provides Intelligent Analysis**:
   - AI-powered summarization using LLMs
   - Risk assessment and actionable recommendations
   - Alert level classification (Low, Medium, High)

3. **Delivers Automated Notifications**:
   - Telegram bot integration for instant alerts
   - Detailed log file generation
   - Beautiful CLI interface with color coding (Optional)

4. **Maintains Data Persistence**:
   - Timestamped log files for historical analysis
---

## 🛠️ Technical Requirements

### Programming Language
- **Python 3.13+** (Latest stable version)

### Core Libraries
- `requests` - API communication
- `python-dotenv` - Environment variable management
- `colorama` - Terminal color output (Optional)
- `openai` - AI integration
- `os`, `datetime` - Built-in Python modules

### External APIs (5 Services)
1. **WeatherAPI** - Weather alerts and forecasts
2. **NewsAPI** - News articles and headlines
3. **Twelve Data API** - Stock market data
4. **OpenAI API** - AI-powered summarization
5. **Telegram Bot API** - Instant notifications

---

## 📚 API Setup Guide

### 1. WeatherAPI (Weather Alerts)
**Website**: https://www.weatherapi.com/
**Purpose**: Real-time weather alerts and forecasts

**Setup Steps**:
1. Visit https://www.weatherapi.com/
2. Click "Sign Up" and create a free account
3. Verify your email address
4. Navigate to "API Keys" section in your dashboard
5. Copy your API key (format: `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`)

**Free Tier**: 1 million calls per month, 3 days forecast

**API Endpoint Used**: `https://api.weatherapi.com/v1/forecast.json`

### 2. NewsAPI (News Articles)
**Website**: https://newsapi.org/
**Purpose**: Latest news articles and headlines

**Setup Steps**:
1. Go to https://newsapi.org/
2. Click "Get API Key" and register
3. Choose "Developer" plan (free)
4. Verify your email
5. Find your API key in the dashboard

**Free Tier**: 1,000 requests per month, 500 articles per request

**API Endpoint Used**: `https://newsapi.org/v2/everything`

### 3. Twelve Data API (Stock Market Data)
**Website**: https://twelvedata.com/
**Purpose**: Real-time stock prices and market data

**Setup Steps**:
1. Visit https://twelvedata.com/
2. Create a free account
3. Navigate to "API" section
4. Copy your API key from the dashboard
5. Note the rate limits for free tier

**Free Tier**: 800 API calls per day, 8 calls per minute

**API Endpoint Used**: `https://api.twelvedata.com/time_series`

### 4. OpenAI API or Gemini (AI Summarization)
**Purpose**: AI-powered alert summarization and insights

**Setup Steps for OpenAI**:
1. Go to https://platform.openai.com/
2. Sign up or log in
3. Navigate to "API Keys" section
4. Click "Create new secret key"
5. Copy and store the key securely
6. Add billing information (required for API usage)

**Pricing**: Pay-per-use, typically $0.03 per 1K tokens for GPT-4

**Model Used**: `gpt-4o` (optimized version), This is just a suggestion, you can totally go with `gemini-2.0-flash` as well, in that case you would just need a gemini key.

### 5. Telegram Bot API (Notifications)
**Website**: https://telegram.org/
**Purpose**: Instant alert notifications

**Setup Steps**:
1. Install Telegram on your device
2. Search for "@BotFather" and start a conversation
3. Send `/newbot` command
4. Choose a bot name (e.g., "My Alert Bot")
5. Choose a username (e.g., "my_alerts_bot")
6. Copy the bot token provided
7. To get Chat ID:
   - Send a message to your bot
   - Visit: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
   - Find your chat ID in the response

**Free Tier**: Completely free, no limits

---

## 📊 Expected Functionality

### 1. Weather Alerts
- **Input**: Location (e.g., "New York", "London")
- **Output**: Active weather warnings with details
- **Features**: Event type, effective dates, descriptions

### 2. News Alerts
- **Input**: Topic/keyword (e.g., "India", "technology")
- **Output**: Latest news articles from past 24 hours
- **Features**: Headlines, descriptions, publication dates, URLs

### 3. Stock Price Alerts
- **Input**: None (monitors top 5 stocks: AAPL, MSFT, GOOGL, AMZN, TSLA)
- **Output**: Price movements and alerts for significant changes
- **Features**: Current price, previous close, percentage change, alert flags

### 4. AI Summary
- **Input**: Aggregated alert log
- **Output**: Intelligent summary with actionable insights
- **Features**: Risk assessment, recommendations, alert levels

---

## 🔍 Code Structure Examples

### Environment Variable Loading
```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("WEATHER_API_KEY")
```

### API Request Pattern
```python
import requests

def fetch_data(endpoint, params):
    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error: {e}")
        return None
```

### Colorized Output
```python
from colorama import Fore, Style, init

init(autoreset=True)
print(f"{Fore.GREEN}✅ Success message")
print(f"{Fore.RED}❌ Error message")
print(f"{Fore.YELLOW}⚠️ Warning message")
```

---

## 🚨 Common Issues & Solutions

### API Key Issues
- **Problem**: "Invalid API key" errors
- **Solution**: Verify key format, check for extra spaces, ensure proper .env file loading

### Rate Limiting
- **Problem**: "Too many requests" errors
- **Solution**: Implement delays between calls, respect API rate limits

### Missing Dependencies
- **Problem**: "Module not found" errors
- **Solution**: Ensure all packages are installed in virtual environment

### Telegram Bot Issues
- **Problem**: Messages not being sent
- **Solution**: Verify bot token, check chat ID, ensure bot is started by user

---

## 🎓 Learning Outcomes

By completing this project, you will learn:

1. **API Integration**: How to work with RESTful APIs
2. **Environment Management**: Secure handling of API keys
3. **Error Handling**: Robust error management in API calls
4. **AI Integration**: Working with OpenAI's GPT models
5. **Real-time Notifications**: Telegram bot implementation
6. **Data Processing**: JSON parsing and data transformation
7. **File I/O**: Log file creation and management
8. **CLI Development**: Interactive command-line interfaces
9. **Python Best Practices**: Code organization and structure

---

## 🔗 Documentation References

### API Documentation
- **WeatherAPI**: https://www.weatherapi.com/docs/
- **NewsAPI**: https://newsapi.org/docs
- **Twelve Data**: https://twelvedata.com/docs
- **OpenAI**: https://platform.openai.com/docs
- **Telegram Bot**: https://core.telegram.org/bots/api

### Python Libraries
- **Requests**: https://requests.readthedocs.io/
- **Python-dotenv**: https://pypi.org/project/python-dotenv/
- **Colorama**: https://pypi.org/project/colorama/
- **OpenAI Python**: https://github.com/openai/openai-python

### Additional Resources
- **JSON Handling**: https://docs.python.org/3/library/json.html
- **DateTime**: https://docs.python.org/3/library/datetime.html
- **File I/O**: https://docs.python.org/3/tutorial/inputoutput.html

---

## 🏆 Bonus Challenges

Once you complete the basic implementation:

1. **Add Email Notifications**: Integrate SMTP for email alerts
2. **Create Web Dashboard**: Build a streamlit interface
3. **Implement Caching**: Add Redis for API response caching
4. **Add More Data Sources**: Integrate cryptocurrency, forex, or weather maps
5. **Create Mobile App**: Build a Flutter/React Native companion app
6. **Add Database Storage**: Use SQLite/PostgreSQL for historical data
7. **Implement Webhooks**: Create webhook endpoints for real-time updates

---

## 🌐 OPTIONAL: Build a Streamlit Web Dashboard

If you want to take your project to the next level, you can build a modern web dashboard using [Streamlit](https://streamlit.io/). This will allow you to visualize alerts, summaries, and reports in a user-friendly browser interface.

### What is Streamlit?
Streamlit is an open-source Python library that makes it easy to build beautiful, interactive web apps for data science and machine learning projects with minimal code.

### How to Get Started
1. **Install Streamlit**
   ```bash
   pip install streamlit
   ```
2. **Create a new file** (e.g., `dashboard.py`)
3. **Import your core functions** from your existing codebase (weather, news, stocks, AI summary)
4. **Design the UI** using Streamlit widgets:
   - `st.text_input` for location/topic input
   - `st.button` for triggering API calls
   - `st.write`, `st.markdown`, `st.table` for displaying results
   - `st.success`, `st.warning`, `st.error` for alert levels
   - `st.expander` for collapsible sections (e.g., raw logs)
5. **Run the app**
   ```bash
   streamlit run dashboard.py
   ```

### Suggested Features for Your Dashboard
- **Weather Alerts Tab**: Input location, display current weather alerts
- **News Alerts Tab**: Input topic, show latest news articles
- **Stock Alerts Tab**: Show top 5 stock movements, highlight significant changes
- **AI Summary Tab**: Display the latest AI-generated summary and recommendations
- **Log Viewer**: Browse or download historical alert logs
- **Telegram Test**: Button to send a test notification

### Example Streamlit Layout
```python
import streamlit as st
from utils import fetch_weather_alerts, fetch_news_alerts, fetch_top_stock_alerts
from agent_utils import summarize_alert_log

st.title('🚨 Real-Time Alert System Dashboard')

# Weather Section
with st.expander('🌤️ Weather Alerts'):
    location = st.text_input('Enter location', 'Delhi')
    if st.button('Get Weather Alerts'):
        alerts = fetch_weather_alerts(location)
        st.write(alerts)

# News Section
with st.expander('📰 News Alerts'):
    topic = st.text_input('Enter news topic', 'India')
    if st.button('Get News Alerts'):
        articles = fetch_news_alerts(topic)
        st.write(articles)

# Stock Section
with st.expander('📈 Stock Price Alerts'):
    if st.button('Get Stock Alerts'):
        stocks = fetch_top_stock_alerts()
        st.write(stocks)

# AI Summary
with st.expander('🧠 AI Summary'):
    # Assume you have a function to get the latest log
    log_content = '...'  # Load from file or generate
    if st.button('Generate AI Summary'):
        summary = summarize_alert_log(log_content)
        st.markdown(summary)
```

### Streamlit Documentation
- [Streamlit Docs](https://docs.streamlit.io/)
- [Streamlit Widgets](https://docs.streamlit.io/library/api-reference/widgets)
- [Streamlit Layouts](https://docs.streamlit.io/library/api-reference/layout)

### Tips
- Keep the UI simple and intuitive
- Use color and icons to highlight important alerts
- Add download buttons for logs or summaries
- Experiment with Streamlit’s layout and interactivity features

---

## 📞 Support & Help

### Getting Help
- Review error messages carefully
- Check API documentation for endpoint requirements
- Verify environment variable loading
- Test each component individually before integration

### Debugging Tips
- Use print statements to trace execution flow
- Check API response status codes
- Validate JSON structure before parsing
- Test with minimal data first

---

**Good luck building your Real-Time Alert System! 🚀**

Remember: This is a learning project. Don't hesitate to experiment, break things, and learn from mistakes. The journey is just as important as the destination!