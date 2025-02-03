# **Stock Price Alert: Price Alerts & Predictions 📈🔔**

**Stock Price Alert** is a Python-based app that provides real-time stock price alerts, trending news, and predictions for specific stocks. The app retrieves stock price data, predicts whether the stock will rise or fall, and sends SMS alerts to users. It also delivers relevant news articles for the selected company to keep users well-informed.

---

## **Features**
- **Real-time Stock Alerts**: Get alerts for selected stocks (e.g., Tesla).
- **Stock Predictions**: Predicts whether the stock price will rise or fall based on recent trends.
- **News Updates**: Fetches trending news articles related to the selected company.
- **SMS Notifications**: Receive real-time SMS notifications for stock updates.

---

## **Installation**

To get started with StockWatcher, follow the steps below.

### **1. Clone the Repository**
```bash
git clone https://github.com/Solomon-mbash/StockWatcher-Price-Alerts.git
cd StockWatcher
```

### **2. Install Dependencies**
Ensure you have `requests`, `twilio`, and `python-dotenv` installed.

```bash
pip install requests twilio python-dotenv
```

### **3. Set Up .env File**

Create a `.env` file in the root of the project and add the following keys:

```plaintext
STOCK_API_KEY=your_alphavantage_api_key
NEWS_API_KEY=your_newsapi_api_key
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
```

### **4. Run the App**
To run the app, execute the following command:

```bash
python main.py
```

---

## **How It Works**

1. **Stock Data**: Fetches the latest stock data (open and close prices) for the selected stock (e.g., Tesla).
2. **Stock Prediction**: Calculates the percentage change between the opening price and closing price from the previous days.
3. **News Fetching**: Retrieves the latest news articles related to the selected company.
4. **SMS Notification**: Sends an SMS with the stock price change percentage and a random news article to a predefined phone number.

---

## **Example Output**

When the stock price of Tesla changes, you will receive an SMS like this:

```
TSLA: 🔺5.24%
Headline: Tesla's stock price rises amid positive earnings report
Brief: Tesla's earnings exceeded expectations, pushing stock value higher.
```

---

## **Acknowledgements**
- [Alpha Vantage API](https://www.alphavantage.co/) for stock data.
- [NewsAPI](https://newsapi.org/) for news articles.
- [Twilio](https://www.twilio.com/) for SMS service.
---
