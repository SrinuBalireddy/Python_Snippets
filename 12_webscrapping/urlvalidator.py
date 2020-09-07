#!python3
# urlvalidator.py
"""
opens all the links in a web page and validates each link
"""

import requests
import bs4

def urlvalidator(search):
    """
    opens all the links in a web page and validates each link
    """
    #Form the url with the search string argument

    main_url = 'https://pypi.org/'
    search_url = main_url+'search/?q='+search

    #Download the data from the url

    res1 = requests.get(search_url)

    #Parse the data

    soup = bs4.BeautifulSoup(res1.text, 'html.parser')
    pipsoup = soup.select('.package-snippet')


    print(len(pipsoup))
    print(pipsoup[0].get('href'))
    print(main_url+pipsoup[0].get('href'))


    #Open all the reference links

    for i in range(len(pipsoup)):
        res2 = requests.get(main_url+pipsoup[i].get('href')+'q')
        soup_new = bs4.BeautifulSoup(res2.text, 'html.parser')
        pipsoup_new = soup_new.select('head title')
        print('Downloa nihy5ding reference link :' + str(i+1))

    #Check the status of the page and tag any 404 errors

        if pipsoup_new[0].getText() == 'Page Not Found (404) · PyPI':
            print('Page cannot be found')
        else:
            print(main_url+pipsoup[i].get('href')+'\nPage has been downloaded successfully')


urlvalidator('boring stuff')
