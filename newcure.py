from gettext import install

import matplotlib.pyplot as plt
import requests
import json
import datetime
import random
import matplotlib
from matplotlib.dates import datestr2num
import streamlit


def get_price(ccy1, ccy2):
    api_url = "https://api.freecurrencyapi.com/v1/latest"
    api_key = "fca_live_Y6gSQXpFBYgtNPXL2wB1e3VqWYBb9MnD0nSn8VpI"
    query = "?apikey=%s&base_currency=%s&currencies=%s" % (api_key, ccy1, ccy2)
    response = requests.get(api_url + query)
    response_in_json = response.json()
    return response_in_json ['data'][ccy2]

ccy1 = input("Please enter currency you would like to exchange from:").upper()
ccy2 = input("Please enter currency you would like to exchange to:").upper()
amount = float(input("Please enter amount:"))
price = get_price(ccy1, ccy2)
exchange_rate = price * amount
print("Price for" + ccy1 + ccy2 + "is" + str(exchange_rate))
print("Price for 1" + ccy1 + ccy2 + "is" + str(price))

def get_price_history(ccy1, ccy2, startDate, endDate):
    price = get_price (ccy1, ccy2)
    my_date = startDate
    history = dict()
    while my_date <= endDate:
        history[my_date] = price + random.uniform(-0.5, 0.5)
        my_date += datetime.timedelta(days=1)
    return history


startDate = datetime.date(2024, 10, 1)
endDate = datetime.date(2024, 10, 30)
price_history = get_price_history(ccy1, ccy2, startDate, endDate)
average = sum(price_history.values())/len(price_history)
print ("Average for the month is" + str(average))

q1 = input("Do you want to sell chosen currency or buy?:").upper()

if q1 == "SELL":
    if price > average:
        print("Good time to change")
    elif price == average:
        print("Average price for the last month")
    else:
        print("Not the best time to change")
elif q1 == "BUY":
    if price > average:
        print("Maybe not today")
    elif price == average:
        print("Average price for the last month")
    else:
        print("Good time to buy, price lower than usual")

dates = [startDate + datetime.timedelta(days=i) for i in range((endDate - startDate).days + 1)]
rates = price_history.values()


plt.figure(figsize=(12, 6))
plt.scatter(dates,rates,color='red')
plt.title('Exchange Rate History')
plt.xlabel('Date')
plt.ylabel('Exchange Rate')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()