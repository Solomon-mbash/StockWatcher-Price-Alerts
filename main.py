import requests
import random
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_api_endpoint = "https://www.alphavantage.co/query"
news_api_endpoint = "https://newsapi.org/v2/everything"

parameter_stock = {
    "symbol": STOCK,
    "apikey": os.getenv("STOCK_API_KEY"),
    "function": "TIME_SERIES_DAILY"
}

parameter_news = {
    "q": COMPANY_NAME,
    "from": "2024-12-09",
    "sortBy": "publishedAt",
    "apiKey": os.getenv("NEWS_API_KEY")
}

#--------------------------------READING STOCKS--------------------------------------------------------------#
response_stock = requests.get(stock_api_endpoint, params=parameter_stock)
data_stocks = response_stock.json()

dates = list(data_stocks["Time Series (Daily)"].keys())
yesterday = dates[0]
day_b4_yesterday = dates[1]
opening_stock = float(data_stocks["Time Series (Daily)"][yesterday]["1. open"])
closing_stock = float(data_stocks["Time Series (Daily)"][day_b4_yesterday]["4. close"])

percentage_change = ((closing_stock - opening_stock) / opening_stock) * 100
#--------------------------------------END----------------------------------------------------------------------#
#---------------------------------------READING NEWS-----------------------------------------------------------#
response_news = requests.get(news_api_endpoint, params=parameter_news)
data = response_news.json()

articles = data['articles']
random_article = random.choice(articles)

#----------------------------------END-------------------------------------------------------------------------------#
#_________________________________________________SENDING SMS__________________________________________________#

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)
message = client.messages.create(
    body=f"TSLA: {'🔺' if percentage_change > 0 else '🔻'}{int(percentage_change):.2f}%\nHeadline: {random_article['title']}\nBrief: {random_article['description']}",
    from_="+12185953387",
    to="+255760412105"
)
print(message.sid)
#____________________________________________________END_____________________________________________________#


