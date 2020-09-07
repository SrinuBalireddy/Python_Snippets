from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup


def home(request):

        price_results = {}
        product =[]

        if request.method == 'POST':
            product = request.POST.getlist('item')

            for i in range(len(product)):
                # Tesco
                tesco_url_str = 'https://www.tesco.com/groceries/en-GB/search?query='
                tesco_main_url = tesco_url_str + product[i]
                tesco_res = requests.get(tesco_main_url)
                tesco_res.raise_for_status()
                tesco_productSoup = BeautifulSoup(tesco_res.text, 'html.parser')
                tesco_productElems = tesco_productSoup.select('.value')

                # Asda

                # asda_url_str = 'https://groceries.asda.com/search/'
                # asda_main_url = asda_url_str + product[i]
                # asda_res = requests.get(asda_main_url)
                # asda_res.raise_for_status()
                # asda_productSoup = BeautifulSoup(asda_res.text, 'lxml')
                # asda_productElems = asda_productSoup.find('span')
                # asda = asda_productElems.text

                price_results[product[i]] = {
                                            'Tesco':  tesco_productElems[0].getText(),
                                            'Asda':   0
                                            }

            return render(request, 'products/results.html', {'price_results': price_results})

        else:
            items_list = ['Sensations','Eggs','Onions','Apples','carrot']
            return render(request, 'products/home.html', {'items_list': items_list} )

