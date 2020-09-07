# Write your code here :-)
#!python3
# pricematch.py
"""
Checks the price of a product in amazon,
compares with the given price,
sends out an email and message when the price drops.
"""

import requests
import bs4
import ezgmail


class Pricematch():

    my_price = 1.00

    #TODO: Nagivate to the Tesco page(search result - sensations)

    res = requests.get('https://www.tesco.com/groceries/en-GB/products/267308049')

    #TODO: Parse the site

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    soup_data = soup.select('.value')

    #TODO: Identify the price of the product and store it in a variable

    item_price = float(soup_data[0].getText())
    print(item_price, my_price , sep='\n')

    #TODO: Compare the price with the desirable price
    #send a notification if the price is dropped

    if item_price <= my_price:
        print('Yay!! The item is on discount. Go order it soon')
        ezgmail.send('srinubalireddy@gmail.com','Tesco - Price Alert','Yay!! The item is on discount. Go order it soon')

    else:
        print('Price of Sensations in Tesco: '+str(item_price))
        ezgmail.send('sowndarya.sri@gmail.com','Tesco - Price Alert','Price of Sensations in Tesco: '+str(item_price))

