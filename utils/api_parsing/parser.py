import string
from urllib import response
import requests

from bs4 import BeautifulSoup
import time
from random import randrange
import json

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}


def get_apple_urls(url):
    s = requests.Session()
    response = s.get(url=url, headers=header)

    with open('./apple.html', 'w', encoding="utf-8") as file:
         file.write(response.text)
    soup = BeautifulSoup(response.text, 'lxml')
    # prodact_image = soup.find('div', class_='ty-column4').find('img')
    product_type = soup.find('ul', class_='ut2-subcategories clearfix').find_all('span')
    
    for page in product_type:
        url = f'https://elmakon.uz/telefony-gadzhety-aksessuary/smartfony/{page.get_text()}/'
        # print(url)
        
        for phones_url in soup.find_all('div', class_= 'ut2-gl__image'):
            print(phones_url.get('href'))

        




def main():
    # print(get_article_urls(url='https://elmakon.uz/telefony-gadzhety-aksessuary/smartfony/'))
    get_apple_urls(url='https://elmakon.uz/telefony-gadzhety-aksessuary/smartfony/page-2/?items_per_page=128')

if __name__ == '__main__':
    main()