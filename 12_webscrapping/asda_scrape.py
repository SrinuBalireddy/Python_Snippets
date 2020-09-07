# Write your code here :-)
import requests
from bs4 import BeautifulSoup

product = 'sensations'

asda_url_str = 'https://groceries.asda.com/search/'
asda_main_url = asda_url_str + product
print(asda_main_url)
asda_res = requests.get(asda_main_url)
asda_res.raise_for_status()
asda_productSoup = BeautifulSoup(asda_res.text, 'html.parser')
asda_productElems = asda_productSoup.select('.modern')

"""
for innerdiv in asda_productSoup.find_all('div'):
    for a in innerdiv.find_all('div'):
        print(a)
        print('-----------------')
"""
#print(asda_res.text[:100])
print(asda_res.prettify())
print(len(str(asda_res)))
print(asda_productElems)
print(len(asda_productElems))


