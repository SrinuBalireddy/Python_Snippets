# Write your code here :-)


import webbrowser, requests, bs4

#webbrowser.open('https://www.instagram.com/p/B_BQaZlFLE5/')
res = requests.get('https://www.instagram.com/beforeafter.design/')
#print(res.text[:250])
soup = bs4.BeautifulSoup(res.text,'html.parser')
iElems = soup.select('._9AhH0')
print(len(iElems))
print(iElems[0].get('nth-child'))


