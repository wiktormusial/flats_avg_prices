import requests
import numpy as np
from bs4 import BeautifulSoup

def get_avg_price(city):
    arr = []
    r = requests.get(f'https://www.olx.pl/d/nieruchomosci/mieszkania/sprzedaz/{city}/?page=1')
    if r.status_code == 200:
       soup = BeautifulSoup(r.text, 'html.parser')
       id = int(soup.find_all("li", attrs={"data-testid": "pagination-list-item"})[-1].text)    
       if id >= 10:
           id = 5 
       for i in range(id):
           r = requests.get(f'https://www.olx.pl/d/nieruchomosci/mieszkania/sprzedaz/{city}/?page={id}')
           soup = BeautifulSoup(r.text, 'html.parser')
           prices = soup.find_all("p", {"class": "css-1bhbxl1-Text"})
           for j in prices:
               index = j.text.index("-") + 2
               end = j.text.index("z") - 1 
               arr.append(float(j.text[index:end]))
       return np.average(arr) 
    else:
        raise Exception('Status code not 200')
