print ("Hello, this is currency exchange for PLN and USD!")
currency = input("Would you like to ecxhange PLN?")
if currency == "Yes"or currency == "yes":
    amount = float(input("Please enter amount:"))
    result = amount * 0.25
    print (result)
else:
    currency1 = float(input("Please enter USD amount:"))
    result1 = currency1 * 3.8
    print (result1)


