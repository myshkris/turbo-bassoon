
import requests

import json

def get_price(ccy1, ccy2):
    api_url = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_Y6gSQXpFBYgtNPXL2wB1e3VqWYBb9MnD0nSn8VpI&currencies=EUR%2CUSD%2CCAD"
    api_key = "fca_live_Y6gSQXpFBYgtNPXL2wB1e3VqWYBb9MnD0nSn8VpI"
    query = "?apikey=%s&base_currency=%s&currencies=%s" % (api_key, ccy1, ccy2)
    return requests.get(api_url + query)

ccy1 = input("Please enter currency you would like to exchange from:")
ccy2 = input("Please enter currency you would like to exchange to:")
# response = get_price(ccy1, ccy2)
# response_in_json = response.json()
print("Print from service" + str(response_in_json))
print("Price for" + ccy1 + ccy2 + "is" + str(response_in_json['data'] [ccy2]))