# Write your code here :-)

import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

a = datetime.today() - timedelta(days=5)
b= datetime.today().strftime('%Y-%m-%d')
c = datetime.today().strptime('03-06-2020','%d-%m-%Y')

d = datetime.today()
print('d',type(d))
print('c: ',type(c))
print('b: ',type(b))

print(c)
print(datetime.today().strftime('%Y-%m-%d'))
print(a)

a = ['abc','new','kbc']

if 'abc' not in a:
    print('kbc')
else:
    print('abc')


