
# 🚀 StockWatcher: Real-Time Price Alerts & Predictions 📈🔔

**StockWatcher** is a Python-powered app that delivers **real-time stock price alerts**, **AI-driven predictions**, and **trending news updates** straight to your phone via SMS. Stay ahead of the market with instant insights! 💹

---

## 🌟 Key Features

- **🚨 Real-Time Stock Alerts**: Monitor price changes for your favorite stocks (e.g., Tesla).
- **🔮 Stock Predictions**: Predicts if a stock will rise (🟢) or fall (🔴) using historical data.
- **📰 News Updates**: Fetches the latest news articles about your selected company.
- **📱 SMS Notifications**: Get alerts directly on your phone with price changes and news snippets.
- **🔒 Secure**: Uses `.env` to protect API keys and sensitive data.

---

## 🛠️ Table of Contents
- [Installation](#-installation)
- [How It Works](#-how-it-works)
- [Example Output](#-example-output)
- [Contributing](#-contributing)
- [Acknowledgements](#-acknowledgements)

---

## ⚡ Installation

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/Solomon-mbash/StockWatcher-Price-Alerts.git
cd StockWatcher-Price-Alerts
```

### 2️⃣ **Install Dependencies**
```bash
pip install requests twilio python-dotenv
```

### 3️⃣ **Set Up Environment Variables**
Create a `.env` file and add your API keys:
```plaintext
STOCK_API_KEY=your_alphavantage_api_key_here  # 📈 Get from Alpha Vantage
NEWS_API_KEY=your_newsapi_api_key_here        # 📰 Get from NewsAPI
TWILIO_ACCOUNT_SID=your_twilio_sid_here       # 📱 Get from Twilio
TWILIO_AUTH_TOKEN=your_twilio_token_here      # 🔑 Get from Twilio
```

### 4️⃣ **Run the App**
```bash
python main.py
```

---

## 🧠 How It Works

1. **📊 Stock Data Fetching**  
   Retrieves daily stock prices (open/close) using the Alpha Vantage API.
   
2. **🔍 Price Analysis**  
   Calculates percentage changes between opening and closing prices to detect trends.

3. **🧠 Prediction Engine**  
   Determines if the stock is likely to rise (🔺) or fall (🔻) based on recent performance.

4. **📰 News Aggregation**  
   Fetches the top 3 news articles about the company using NewsAPI.

5. **📲 SMS Alerts**  
   Sends a consolidated SMS via Twilio with price changes and a news summary.

---

## 📨 Example Output

You’ll receive an SMS like this:
```
TSLA: 🔺5.24%  
📰 Headline: Tesla's Stock Soars After Record Earnings!  
💬 Brief: Tesla announced a 20% revenue increase, beating analyst expectations.
```

---

## 👥 Contributing

**Love this project?** Feel free to contribute!  
1. 🍴 Fork the repo.  
2. 🌿 Create a branch: `git checkout -b feature/your-feature`.  
3. 💾 Commit changes: `git commit -m "Add awesome feature"`.  
4. 🚀 Push to the branch: `git push origin feature/your-feature`.  
5. 🔄 Open a pull request.

---

## 🤝 Acknowledgements

- **📈 Stock Data**: Powered by [Alpha Vantage](https://www.alphavantage.co/).
- **📰 News API**: Sourced from [NewsAPI](https://newsapi.org/).
- **📱 SMS Service**: Delivered by [Twilio](https://www.twilio.com/).

---

**Made with ❤️ by [Solomon Mbash](https://github.com/Solomon-mbash)**
```
