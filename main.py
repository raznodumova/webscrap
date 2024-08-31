import bs4
import requests
import lxml
from pprint import pprint
from fake_headers import Headers


KEYWORDS = ['Процессоры', 'Химия', 'IT']

url = 'https://habr.com/ru/articles/'


def get_fake_headers():
    headers = Headers(
        browser="сhrome",
        os="win"
    )
    return headers.generate()

def find_news(url):
    response = requests.get(url, headers=get_fake_headers())

    soup = bs4.BeautifulSoup(response.text, 'lxml')
    global_data = soup.find_all('div', class_='tm-article-snippet')
    for d in global_data:
        title = d.find('h2')
        news_link = title.find('a')['href']
        full_link = f'https://habr.com{news_link}'
        date = d.find('a', class_='tm-article-datetime-published').find('time')['title']
        key_words = d.findAll('span', class_='tm-publication-hub__link-container')
        for key in key_words:
            keys = key.find('span').text
            for k in KEYWORDS:
                if k in keys:
                    pprint(f'<{date}>-<{title.text}>-<{full_link}>')


if __name__ == '__main__':
    find_news(url)
