import config
import telebot
import requests
import time
import schedule
import urllib
from bs4 import BeautifulSoup as bs

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

kfc_url = 'https://www.kfc.ru/coupons'

url='https://retailer.ru/wp-content/uploads/2019/04/kfc-logo-1.jpg'
f = open('out.jpg','wb')
f.write(urllib.request.urlopen(url).read())
f.close()

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
                # 'img': cupon.find('div', attrs={'style'}),
            }
            # print(cupon.div['style'])

bot = telebot.TeleBot(config.TOKEN)


# если /help, /start
@bot.message_handler(commands=['start'])
def send_welcome(message):

    bot.send_message(message.chat.id, "Здравствуйте "
                     + message.from_user.first_name
                     + ",\n Я бот сервисного центра 🔥 *IT-S | Service* 🔥, чтобы вы хотели узнать? "
                     + "\n /contacts - Контакты 📞"
                     + "\n /reg - Оставить заявку 📒"
                     + "\n /start - Начать сначала 💪", )




def send_data(message):

    if request.status_code == 200:
        request = session.get(kfc_url, headers=headers)
        soup = bs(request.content, 'lxml')
        cupon_table = soup.find('div', attrs={'class': '_1h2YIDTLoW mt-64'})

        cupons_info = cupon_table.find_all('div', attrs={'class': '_2NyuN9wIxb _2863BpiS1v mr-32 mb-64'})

        for cupon in cupons_info:
            data = {
                'cupon': cupon.find('div', attrs={'class': '_2pr76I4WPm'}).text,
                'title': cupon.find('div',
                                    attrs={'class': '_3POebZQSBG t-md c-description mt-16 pl-24 pr-24 condensed'}).text,
                'old_price': cupon.find('div', attrs={'class': '_2XDTnYog36'}).span.text,
                'new_price': cupon.find('span', attrs={'class': '_1trEHSCHMh condensed c-primary bold'}).text,
                # 'img': cupon.find('div', attrs={'style'}),
            }
            schedule.every(5).seconds.do(bot.send_message(message.chat.id, "Купон KFC: "
                             + "\n Сегодня доступен: " + data['title']
                             + "\n По купону: " + data['cupon']
                             + "\n Старая цена: " + data['old_price'] + "₽"
                             + "\n Новая цена: " + data['new_price'] + "₽"))


def send_cupon():
    # chat_id= "402149651"
    img = open('out.jpg', 'rb')
    chat_id= "-1001301485842"
    session = requests.Session()
    request = session.get(kfc_url, headers=headers)



    if request.status_code == 200:
        request = session.get(kfc_url, headers=headers)
        soup = bs(request.content, 'lxml')
        cupon_table = soup.find('div', attrs={'class': '_1h2YIDTLoW mt-64'})

        cupons_info = cupon_table.find_all('div', attrs={'class': '_2NyuN9wIxb _2863BpiS1v mr-32 mb-64'})

        dist = []

        for cupon in cupons_info:
            data = {
                'купон': cupon.find('div', attrs={'class': '_2pr76I4WPm'}).text.strip(),
                'Название': cupon.find('div',
                                    attrs={'class': '_3POebZQSBG t-md c-description mt-16 pl-24 pr-24 condensed'}).text.strip(),
                'старая цена': cupon.find('div', attrs={'class': '_2XDTnYog36'}).span.text.strip(),
                'новая цена': cupon.find('span', attrs={'class': '_1trEHSCHMh condensed c-primary bold'}).text.strip(),
                '\n': ':::::::::::::::::::: : \n'

            }
            dist.append(data)
            # send_cupon_message(chat_id, data)
        # send_cupon_message(chat_id, data)
        str = ""
        for element in dist:
            # print(element)
            for key, value in element.items():
                result = '\n '.join([f'{key.capitalize()}: {value}'])
                str += result + "\n"
        return send_cupon_message(chat_id, str)



#bot.send_photo(id, photo, caption='желаемый текст')


def send_cupon_message(chat_id, data):
    img = open('out.jpg', 'rb')
    # text = "Купон KFC: \n Сегодня доступен: " + data['title']  + "\n По купону: " + data['cupon'] + "\n Старая цена: " + data['old_price'] + "₽" + "\n Новая цена: " + data['new_price'] + "₽"
    return print(len(data))
    # return bot.send_photo(chat_id, img, caption=data) // Всем сообщением не влазит


schedule.every(5).seconds.do(send_cupon)
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("02:03").do(send_cupon) # Send message every day in 01:57
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":27").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

bot.polling(none_stop=True)
