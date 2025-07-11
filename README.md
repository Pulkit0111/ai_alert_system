# 🚨 Real-Time Alert System

A comprehensive Python-based alert monitoring system that tracks weather conditions, news updates, and stock price movements with AI-powered summarization and Telegram notifications.

## 🌟 Features

### 📊 Multi-Source Alert Monitoring
- **Weather Alerts**: Real-time weather warnings and forecasts for any location
- **News Alerts**: Latest news articles filtered by topic or keyword
- **Stock Price Alerts**: Monitor top 5 stocks (AAPL, MSFT, GOOGL, AMZN, TSLA) for significant price movements

### 🤖 AI-Powered Intelligence
- **Smart Summarization**: Uses OpenAI GPT-4 to generate actionable insights from alert data
- **Risk Assessment**: Automatic alert level classification (Low, Medium, High)
- **Actionable Recommendations**: AI suggests specific actions based on alert patterns

### 📱 Notification System
- **Telegram Integration**: Automatic alert summaries sent to your Telegram chat
- **Report Generation**: Detailed logs saved with timestamps for historical analysis
- **Colorized CLI**: Beautiful terminal interface with color-coded information

## 🛠️ Installation

### Prerequisites
- Python 3.13 or higher
- API keys for external services (see Configuration section)

### Quick Setup
```bash
# Clone the repository
git clone <repository-url>
cd alert_system

# Install dependencies using uv (recommended)
uv sync

# Or install with pip
pip install -r requirements.txt
```

## ⚙️ Configuration

Create a `.env` file in the project root with the following API keys:

```env
# Weather API (weatherapi.com)
WEATHER_API_KEY=your_weather_api_key

# News API (newsapi.org)
NEWS_API_KEY=your_news_api_key

# Stock Data API (twelvedata.com)
TWELVE_DATA_API_KEY=your_twelve_data_api_key

# OpenAI API (openai.com)
OPENAI_API_KEY=your_openai_api_key

# Telegram Bot (optional)
TG_BOT_TOKEN=your_telegram_bot_token
TG_CHAT_ID=your_telegram_chat_id
```

### Getting API Keys

1. **WeatherAPI**: Sign up at [weatherapi.com](https://www.weatherapi.com/) for free weather data
2. **NewsAPI**: Get your key at [newsapi.org](https://newsapi.org/) for news articles
3. **Twelve Data**: Register at [twelvedata.com](https://twelvedata.com/) for stock market data
4. **OpenAI**: Create an account at [openai.com](https://openai.com/) for AI summarization
5. **Telegram Bot**: Create a bot via [@BotFather](https://t.me/botfather) on Telegram

## 🚀 Usage

### Running the Application
```bash
python main.py
```

### Interactive Menu Options

#### 1. Weather Alerts 🌤️
- Enter any location (default: Delhi)
- View current weather warnings and forecasts
- Get detailed alert descriptions with effective dates

#### 2. News Feed Alerts 📰
- Search news by topic (default: India)
- Get latest articles from the past 24 hours
- View headlines, descriptions, and source URLs

#### 3. Stock Price Alerts 📈
- Monitor top 5 stocks for significant movements
- Automatic alerts for price changes > 3%
- Compare current vs. previous closing prices

#### 4. Exit & Generate Report 📊
- Creates a comprehensive alert summary
- Generates AI-powered insights and recommendations
- Sends summary to Telegram (if configured)
- Saves detailed logs to `logs/` directory

## 📁 Project Structure

```
alert_system/
├── main.py              # Main application entry point
├── utils.py             # Core alert fetching utilities
├── alert_agent.py       # Alert processing orchestration
├── agent_utils.py       # AI summarization and Telegram integration
├── pyproject.toml       # Project configuration and dependencies
├── logs/               # Generated alert reports
└── README.md           # Project documentation
```

## 🔧 Key Components

### Core Modules

- **`main.py`**: Interactive CLI interface with menu system
- **`utils.py`**: API integration functions for weather, news, and stock data
- **`alert_agent.py`**: Coordinates the AI analysis pipeline
- **`agent_utils.py`**: OpenAI integration and Telegram notifications

### Alert Processing Pipeline

1. **Data Collection**: Fetch alerts from multiple APIs
2. **Aggregation**: Combine alerts into structured reports
3. **AI Analysis**: Generate insights using OpenAI GPT-4
4. **Notification**: Send summaries via Telegram
5. **Logging**: Save detailed reports for historical analysis

## 🎯 Use Cases

### Personal Monitoring
- Track severe weather in your area
- Stay updated on relevant news topics
- Monitor your stock portfolio

### Business Intelligence
- Market movement analysis
- Risk assessment for operations
- Automated reporting for stakeholders

### Research & Analysis
- Historical alert pattern analysis
- Cross-correlation between news and market events
- Weather impact on business operations

## 🔍 Example Output

### Weather Alert
```
🌀 Alert #1: Heavy Rain Warning
📅 From: 2024-01-15T06:00:00Z
📅 To: 2024-01-15T18:00:00Z
📝 Description: Heavy rainfall expected with potential flooding...
```

### AI Summary
```
🧠 Agent Summary:
- 🚨 TSLA dropped 6.2% today — possibly due to disappointing Q2 results
- 🌧️ Heavy rainfall and flooding expected in Mumbai and Pune tomorrow
- 📰 Top news: Power workers nationwide protest against privatization
- 🟡 Overall alert level: Medium – Stay alert for flood and stock triggers
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add new feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For issues and questions:
- Create an issue on GitHub
- Check the logs in the `logs/` directory for troubleshooting
- Verify all API keys are correctly configured

## 🔮 Future Enhancements

- [ ] Web dashboard interface
- [ ] Email notification support
- [ ] Custom alert thresholds
- [ ] Historical data visualization
- [ ] Multi-language support
- [ ] Mobile app integration

---

⭐ **Star this repository if you find it helpful!**
