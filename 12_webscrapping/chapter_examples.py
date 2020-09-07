# Write your code here :-)
#example 1 - web browser

"""
import webbrowser,sys,pyperclip

#webbrowser.open("https://www.google.com/maps/place/69+Francis+Rd,+Hounslow+TW4+7JT/")

if len(sys.argv)>1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open(f'https://www.google.com/maps/place/{address}/')

"""

#example 2- requests
"""
import requests,webbrowser

#webbrowser.open('https://automatetheboringstuff.com/files/rj.txt')
res=requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(len(res.text))
print(res.text[:250])
print(requests.codes.ok)
print(res.status_code)

"""
"""
import requests
res = requests.get('https://automatetheboringstuff.com/files/page_doesnot_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was an error '+ str(exc))

"""
"""
import requests
res=requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.text[:250])
filename = open('rj.txt','wb')
for chunk in res.iter_content(100000):
    filename.write(chunk)

"""

#example  - bs4
"""
import bs4

file = open('example.html')
examplesoup = bs4.BeautifulSoup(file.read(),'html.parser')
elems = examplesoup.select('p')
print(type(elems))
print(len(elems))
print(type(elems[0]))
print(str(elems))
print(elems[0])
print(elems[0].getText())
print(elems[1].getText())
print(elems[2].getText())
print(elems[0].attrs)
"""
"""
import bs4,requests

res = requests.get("https://forecast.weather.gov/MapClick.php?lat=42.55619000000007&lon=-114.46959999999996")
#print(res.text[:250])

bsexample = bs4.BeautifulSoup(res.text,'html.parser')
elems = bsexample.select('.col-sm-10')
print(str(elems))
print(len(elems))
print(elems[1].getText())
"""

import bs4, requests

res = requests.get('https://www.bbc.co.uk/weather/tw19')
bs = bs4.BeautifulSoup(res.text,'html.parser')
weather = bs.select('#daylink-10')
print(len(weather))
print(weather[0].getText())

