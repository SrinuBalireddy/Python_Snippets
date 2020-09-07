# Write your code here :-)
#! python3
# googlesearch.py -opens search results in multiple windows

import sys, pyperclip, requests , bs4, webbrowser

if len(sys.argv)>1:
    searchText = ' '.join(sys.argv[1:])
else:
    searchText = 'python'#pyperclip.paste()

print(searchText)

webbrowser.open('https://duckduckgo.com/?q='+searchText)
#webbrowser.open('https://www.google.com/search?q='+searchText)
res = requests.get('https://www.google.com/search/?q='+searchText)
bs = bs4.BeautifulSoup(res.text,'html.parser')
bs_search = bs.select('#r1')
print(str(bs_search))
print(len(bs_search))
