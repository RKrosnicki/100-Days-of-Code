import requests
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

def daily_stock(stock):
    """
    This function is doing a check how is company mentioned in COMPANY_NAME doing lately using Alpha Advantage API.
    """

    alpha_advantage_endpoint = 'https://www.alphavantage.co/query'

    alpha_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock,
        "apikey": os.environ["ALPHA_ADVANTAGE_API_KEY"],
    }

    alpha_response = requests.get(url=alpha_advantage_endpoint, params=alpha_params)
    alpha_data = alpha_response.json()
    alpha_data = alpha_data['Time Series (Daily)']

    days_list = alpha_data.keys()
    yesterday_close = float(alpha_data[list(days_list)[0]]['4. close'])
    day_before_yesterday_close = float(alpha_data[list(days_list)[1]]['4. close'])
    result = ((yesterday_close - day_before_yesterday_close) / yesterday_close) * 100
    result = round(result, 4)
    # print(result) ## Uncomment if you want to print a stock fluctuations.
    return result, days_list

def get_news(company_name:str):
    """
    This function downloads and returns a list of 3 most popular articles from last 5 days about our COMPANY_NAME using NewsAPI.org
    """

    news_api_endpoint = "https://newsapi.org/v2/everything?"

    news_api_params = {
        'q': company_name,
        'from': list(days)[4],
        'sortBy': 'popularity',
        'apiKey':os.environ["NEWS_API_KEY"]
    }

    news_response = requests.get(url=news_api_endpoint, params=news_api_params)
    # print(news_response.raise_for_status())  ## Uncomment to see status number for NewsAPI.
    news_data = news_response.json()["articles"][:3]
    return news_data

def send_news():
    """
    This function sends SMS with info about changes, and latest articles if stock fluctuations are higher than 5%.
    """

    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']

    client = Client(account_sid, auth_token)

    if diff > 0:
        message = f"{STOCK}: 🔺{diff}%."
    else:
        message = f"{STOCK}: 🔻{diff}%."

    message = client.messages.create(
             body=message,
             from_='+16072282842',
             to=os.environ['MY_NUMBER']
         )
    #print(message.status) ## Uncomment if you want to see when the message is sent.

    for news in latest_news:
        message = f"\n====================\nHeadline: {news['title']}\nBrief: {news['description']}"
        message = client.messages.create(
                 body=message,
                 from_='+16072282842',
                 to=os.environ['MY_NUMBER']
             )
        # print(message.status) ## Uncomment if you want to see when the message is sent.

diff, days = daily_stock(STOCK)

if abs(diff) > 5:
    latest_news = get_news(COMPANY_NAME)
    send_news()
# else:
#     latest_news = get_news(COMPANY_NAME)     ## Uncomment these lines if you want to send messages no matter how high the fluctuations are.
#     send_news()
