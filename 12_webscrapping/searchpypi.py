# Write your code here :-)
#! python3
# searchpypi.py -- opens several search results

import webbrowser,sys,requests, bs4,pyperclip

if len(sys.argv)>1:
    searchtext = ' '.join(sys.argv[1:])
else:
    searchtext = pyperclip.paste()

print(searchtext)
search_results = requests.get('https://pypi.org/search/?q='+searchtext)
search_results.raise_for_status()

#retrieve top search results link
soup = bs4.BeautifulSoup(search_results.text,'html.parser')

#open a browser tab for each result.
linkElems = soup.select('.package-snippet')
print(len(linkElems))
#print(str(linkElems))
print(linkElems[0].get('href'))

numopen = min(5,len(linkElems))
for i in range(numopen):
    urlToOpen = 'https://pypi.org'+linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)



