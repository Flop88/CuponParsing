import requests
from bs4 import BeautifulSoup as bs

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

kfc_url = 'https://www.kfc.ru/coupons'
# base_url = 'http://malvina-club.ru/hours/'

def cupon_pars():

    session = requests.Session()
    request = session.get(kfc_url, headers=headers)

    if request.status_code == 200:
        request = session.get(kfc_url, headers=headers)
        soup = bs(request.content, 'lxml')
        cupon_table = soup.find('div', attrs={'class': '_1h2YIDTLoW mt-64'})

        cupons_info = cupon_table.find_all('div', attrs={'class': '_2NyuN9wIxb _2863BpiS1v mr-32 mb-64'})

        for cupon in cupons_info:
            data = {
                'cupon': cupon.find('div', attrs={'class': '_2pr76I4WPm'}).text,
                'title': cupon.find('div', attrs={'class': '_3POebZQSBG t-md c-description mt-16 pl-24 pr-24 condensed'}).text,
                'old_price': cupon.find('div', attrs={'class': '_2XDTnYog36'}).span.text,
                'new_price': cupon.find('span', attrs={'class': '_1trEHSCHMh condensed c-primary bold'}).text,
                'img': cupon.find('div', attrs={'class': '_3nVETUX19K'}),
            }
            print(data)



cupon_pars()