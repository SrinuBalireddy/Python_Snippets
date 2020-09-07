# Write your code here :-)
import requests

headers = {
    "StoreFrontAccessToken": "494265621e3afb9710e05063176e17a3",
    "Content-Type": "application/json"
    }

resp = requests.get('https://a38f4a6a8cb713fe2bebdbf3df331f54:3182dcd29ff6c3f6f2dd325ba99b4216@mishipaytestdevelopmentemptystore.myshopify.com/admin/products.json')

resp = requests.get('https://a38f4a6a8cb713fe2bebdbf3df331f54:3182dcd29ff6c3f6f2dd325ba99b4216@mishipaytestdevelopmentemptystore.myshopify.com/admin/products.json?ids=4408136663107')

#resp = requests.get('https://a38f4a6a8cb713fe2bebdbf3df331f54:3182dcd29ff6c3f6f2dd325ba99b4216@mishipaytestdevelopmentemptystore.myshopify.com/admin/products.json?ids=4408178344003')

#r = requests.get("https://a38f4a6a8cb713fe2bebdbf3df331f54:3182dcd29ff6c3f6f2dd325ba99b4216@mishipaytestdevelopmentemptystore.myshopify.com/admin/api/2020-01/orders.json")

print(resp.json()['products'])
#print(resp.json()['products'][1])
