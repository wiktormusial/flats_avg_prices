import requests
import numpy as np
from bs4 import BeautifulSoup

def get_avg_price(city):
    r = requests.get(f'https://www.olx.pl/d/nieruchomosci/mieszkania/sprzedaz/{city}/')
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        prices = soup.find_all("p", {"class": "css-1bhbxl1-Text"})
        arr = []
        for i in prices:
            index = i.text.index("-") + 2
            end = i.text.index("z") - 1 
            arr.append(float(i.text[index:end]))
        return np.average(arr) 
    else:
        raise Exception('Status code not 200')
