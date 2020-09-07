# Write your code here :-)
#!python3
# xkcd.py - saves the images to hard drive
import requests, bs4 ,os

url = 'https://xkcd.com'        # starting url
os.makedirs('xkcd', exist_ok=True)  #store comic in ./xkcd

while not url.endswith('#'):

    #TODO: Find the url of the comic page
    print(f'Downloading the page {url}')
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text,'html.parser')

    #TODO: Download the image.

    comicElem = soup.select('#comic img')
    #print('https:'+comicElem[0].get('src'))

    if comicElem==[]:
        print('Could not find comic image')
    else:
        comicurl = 'https:'+comicElem[0].get('src')
        print(f'Downloading the image {comicurl}')
        res = requests.get(comicurl)
        res.raise_for_status()

    #TODO: Save the image to ./xkcd.com
    imageFile = open (os.path.join('xkcd',os.path.basename(comicurl)),'wb')

    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    #url ='#'

    #TODO: Get the prev's button's url

    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com'+prevLink.get('href')


print('Done')
