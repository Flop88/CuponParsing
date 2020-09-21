import requests
from bs4 import BeautifulSoup as bs

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

mac_url = 'https://promokodus.com/campaigns/mcdonalds/'
# base_url = 'http://malvina-club.ru/hours/'

def cupon_pars():

    session = requests.Session()
    request = session.get(mac_url, headers=headers)

    if request.status_code == 200:
        request = session.get(mac_url, headers=headers)
        soup = bs(request.content, 'lxml')
        cupon_table = soup.find('div', attrs={'id': 'coupons'})

        print(cupon_table)

cupon_pars()