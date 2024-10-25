import requests

api_key = "fca_live_Y6gSQXpFBYgtNPXL2wB1e3VqWYBb9MnD0nSn8VpI"
response = requests.get(api_key)

def get_price(ccy1, ccy2):
    return requests.get(api_url + query)

print ("Hello, this is currency exchange for PLN and USD!")
ccy1 = input("Please enter currency you would like to eschange from:")
ccy2 = input("Please enter currency you would like to exchange to:")
currency = input ("Would you like to exchange ccy1 to ccy2?")
if currency == "Yes"or currency == "yes":
    amount = float(input("Please enter amount:"))
    result = amount * get_price
    print (result)
else:
    currency1 = float(input("Please enter USD amount:"))
    result1 = currency1 * get_price()
    print (result1)


