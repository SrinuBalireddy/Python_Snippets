# Write your code here :-)
#!python3
# imgur.py - Downloads files from imgur website to local drive.

import requests , bs4 , os
from pathlib import Path


def imgurdownload(query):

    #TODO: formatting the required url from the function argument

    url = 'https://imgur.com/'
    searchurl = url+'search?q='+query

    #TODO: download the complete url data and create a folder

    res = requests.get(searchurl)

    os.makedirs('imgur',exist_ok = True)

    #TODO: download the images using bs4

    soup = bs4.BeautifulSoup(res.text,'html.parser')
    Imgursoup = soup.select('.image-list-link img')
    #print(len(Imgursoup))
    #print(Imgursoup[0].get('src'))
    for i in range(len(Imgursoup)):
        path= 'https:'+Imgursoup[i].get('src')
        print('downloading Image ' +path)

    #TODO: write the data to local drive

        res2 = requests.get(path)
        res2.raise_for_status

        filename = open(os.path.join('Imgur',os.path.basename(path)),'wb')
        for chunk in res2.iter_content(100000):
            print('Downloading the file ..')
            filename.write(chunk)
        filename.close()


imgurdownload('messi')


"""
res = requests.get('https://imgur.com/gallery/kUCMPWX')
soup = bs4.BeautifulSoup(res.text,'html.parser')
soupdata = soup.select('.Post-item-title')
print(len(soupdata))
print(str(soupdata))
print(soupdata[0].getText())



print(res.text[0:20])
os.makedirs('imgur',exist_ok = True)
Image = open(os.path.join('imgur','test.jpeg'),'wb')

for chunk in res.iter_content(100000):
    Image.write(chunk)
"""""""""


