import requests
from bs4 import BeautifulSoup
import re
import json
import time
from collections import Counter


class PikabuGrabber():
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
        "Cookie": "PHPSESS=ouoo8b36mu9vlvt51ou0fooo9aea3go5; "
                  "is_scrollmode=1; pcid=VuZjWR0Zhv2; ulfs=1561372327; "
                  "_vA3=P5-w-C-C-90ZQ-KCaQ.t4-d-A-B-90ZQ-1NaQ."
                  "X4-w-C-C-A_ZQ-PCaQ.4a8yMB; "
                  "rheftjdd=rheftjddVal; pkb_modern=11; "
                  "_ym_uid=1561364278671438861; "
                  "_ym_d=1561364278; bs=G0; _ga=GA1.2.799294783.1561364279; "
                  "_gid=GA1.2.1965745844.1561364279; _ym_isad=2; "
                  "vn=eJwdybcRADAIBLCFXBA+sP9kPqhUSLaK+WTDqLMz1g7O"
                  "SumebXzljAmR; "
                  "cto_lwid=885ad351-4ecc-4503-91dc-572e4f9268be; "
                  "fps=d0cb5eec6656a5774a8628d19df6341197; "
                  "__utma=43320484.799294783.1561364279.1561364341."
                  "1561364341.1; "
                  "__utmc=43320484; "
                  "__utmz=43320484.1561364341.1.1.utmcsr=(direct)|"
                  "utmccn=(direct)|utmcmd=(none); "
                  "autohide_news=0; _nuser=1; nps7s=2149264246; "
                  "_ym_visorc_174977=w; "
                  "_ym_visorc_56459=w; set_autohide_news=-1; la=1; "
                  "phpDug2=a%3A4%3A%7Bs%3A3%3A%22uid%22%3Bs%3A7%3A%222795727%"
                  "22%3Bs%3A8%3A%22username%22%3Bs%3A8%3A%22Bonzzomi%22%3Bs%3"
                  "A3%3A%22rem%22%3Bs%3A32%3A%225b0faa5498b47b1098a11f60f6498"
                  "be1%22%3Bs%3A5%3A%22tries%22%3Bi%3A0%3B%7D",
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
        "Cookie": "PHPSESS=ouoo8b36mu9vlvt51ou0fooo9aea3go5; "
                  "is_scrollmode=1; pcid=VuZjWR0Zhv2; ulfs=1561381851; "
                  "_vA3=X4-w-B-B-A_ZQ-eGaQ.t4-d-A-B-90ZQ-1NaQ.Q5-d-C-C-RDaQ-"
                  "dGaQ.P5-w-B-B-90ZQ-dGaQ.z0mK1C; rheftjdd=rheftjddVal; "
                  "pkb_modern=11; _ym_uid=1561364278671438861; "
                  "_ym_d=1561364278; bs=G0; _ga=GA1.2.799294783.1561364279; "
                  "_gid=GA1.2.1965745844.1561364279; _ym_isad=2; "
                  "vn=eJwlybENACAMA8GFKEIS27D/YiimeumPEi9yUepoTos6Uya2v/p77bA"
                  "H7CDtKPUDCwgOfQ==; cto_lwid=885ad351-4ecc-4503-91dc-572e"
                  "4f9268be; fps=d0cb5eec6656a5774a8628d19df6341197; "
                  "__utma=43320484.799294783.1561364279.1561364341."
                  "1561364341.1; __utmc=43320484; __utmz=43320484.1561364341."
                  "1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); "
                  "autohide_news=0; _nuser=1; nps7s=2149264246; "
                  "set_autohide_news=-1; phpDug2=a%3A4%3A%7Bs%3A3%3A%22uid"
                  "%22%3Bs%3A7%3A%222795727%22%3Bs%3A8%3A%22username%22%3B"
                  "s%3A8%3A%22Bonzzomi%22%3Bs%3A3%3A%22rem%22%3Bs%3A32%3A%"
                  "225b0faa5498b47b1098a11f60f6498be1%22%3"
                  "Bs%3A5%3A%22tries%22%3Bi%3A0%3B%7D; "
                  "la=1; _gat_gtag_UA_28292940_1=1"}

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
