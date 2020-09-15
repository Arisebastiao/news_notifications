import requests
import bs4
import lxml
import smtplib
import time


def get_news():
    source = requests.get('https://www.noticiasaominuto.com/').text

    soup = bs4.BeautifulSoup(source, 'lxml')

    soup.select('a[href="https://www.noticiasaominuto.com/"]')

    parsing = soup.find_all('div', {'class': 'main-carousel-item-container carousel-item-img swiper-slide'})
    title_news = soup.find_all('span', {'class': 'hover-background main-carousel-nav-item-text'})

    for element in title_news:
        title = element.tex
        for link in parsing:
            print(title, '\n', link.a['href'])
        break
    send_email()


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('arisebastiao99@gmail.com', 'vwwtsfrdnywtmqwf')

    subject = 'Top News:'
    body = 'hello'

    msg = f'subject: {subject}\n\n{body}'

    server.sendmail('arisebastiao99@gmail.com', 'arisebastiao99@gmail.com', msg)

    print('News notifications sent!')

    server.quit()


get_news()

time.sleep(10800)
