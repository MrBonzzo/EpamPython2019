from bs4 import BeautifulSoup
from collections import Counter
import re
import requests
import time
import json


def get_cookies_from_file(filename):
    with open(filename, 'r') as cookie_file:
        lines = [c.strip() for c in cookie_file.read().split('\n')]
        cookies = {lines[0]: lines[1], lines[2]: lines[3]}
    return cookies


class PikabuGrabber():
    cookies = get_cookies_from_file('Cookies')
    HEADERS_MAIN_PAGE = {
        "Host": "pikabu.ru",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; "
                      "rv:67.0) Gecko/20100101 Firefox/67.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;"
                  "q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Referer": "https://pikabu.ru/",
        "Cookie": cookies['Cookie_main_page'],
        "Upgrade-Insecure-Requests": "1",
        "Cache-Control": "max-age=0",
        "TE": "Trailers"}

    HEADERS_LOADING = {
        "Host": "pikabu.ru",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; "
                      "x64; rv:67.0) Gecko/20100101 Firefox/67.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "X-Csrf-Token": "ouoo8b36mu9vlvt51ou0fooo9aea3go5",
        "X-Requested-With": "XMLHttpRequest",
        "Connection": "keep-alive",
        "Referer": "https://pikabu.ru/",
        "Cookie": cookies['Cookie_loading']}

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = self.HEADERS_MAIN_PAGE
        self.page_number = 1
        self.query_number = int(time.time())*1000
        self.responce = 0
        self.query = 'https://pikabu.ru'

    def get_page(self):
        self.responce = self.session.get(self.query)
        return self.responce

    def change_ulfs(self):
        headers = str(self.responce.headers)
        ulfs_pattern = re.compile(r'(ulfs=\d*)')
        new_cookie = ulfs_pattern.search(headers).groups()[0]
        self.HEADERS_LOADING['Cookie'] = \
            ulfs_pattern.sub(new_cookie, self.HEADERS_LOADING['Cookie'])

    def change_headers(self):
        self.session.headers = self.HEADERS_LOADING

    def change_query(self):
        self.page_number += 1
        self.query_number += 1
        query_str = f"https://pikabu.ru/?twitmode=1&of=v2&page=\
                    {self.page_number}&_={self.query_number}"
        self.query = query_str

    def update_http_headers(self):
        self.change_query()
        self.change_ulfs()
        self.change_headers()


def get_posts_from_json(json_object):
    return [j['html'] for j in json.loads(json_object)['data']['stories']]


grabber = PikabuGrabber()
main_page = grabber.get_page()
soup = BeautifulSoup(main_page.text, 'html.parser')
tags = [s.get_text() for s in soup.find_all(class_='tags__tag')]
tags_counter = Counter(tags)
print("counted 20 posts")
grabber.change_headers()
for i in range(4):
    grabber.update_http_headers()
    time.sleep(3)
    page = grabber.get_page()
    posts = get_posts_from_json(page.text)
    if page.status_code != 200:
        print(f'Status code {page.status_code}')
        break
    for post in posts:
        soup = BeautifulSoup(post, 'html.parser')
        tags = [s.get_text() for s in soup.find_all(class_='tags__tag')]
        tags_counter += Counter(tags)
    print(f"counted {40 + i*20} posts")
else:
    with open("dump_stat.txt", 'w') as stat_dump:
        tags_counter_list = list(tags_counter.items())
        tags_counter_list.sort(key=lambda x: x[1], reverse=True)
        for tag in tags_counter_list:
            stat_dump.write(f'{tag[0]}: {tag[1]}\n')
