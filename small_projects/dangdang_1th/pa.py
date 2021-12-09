#########################################################################
# File Name: pa.py
# Author: Walker
# mail:qngskk@gmail.com
# Created Time: Thu Dec  9 14:54:19 2021
#########################################################################
# !/usr/bin/env python3

import requests
from fake_useragent import UserAgent
from lxml import etree
import csv


class dangdang(object):
    def __init__(self):
        self.url = 'http://bang.dangdang.com/books/bestsellers'
        ua = UserAgent(verify_ssl=False)
        for i in range(1, 100):
            self.headers = {
                'User-Agent': ua.random
            }

    def get_html(self, url):
        response = requests.get(url, headers=self.headers)
        html = response.text
        return html

    def parse_html(self, html):
        target = etree.HTML(html)
        titles = target.xpath('//p[@class="name"]/a/@title')
        prices = target.xpath('//p[@class="price"]/span/text()')
        links = target.xpath('//p[@class="name"]/a/@href')
        with open('./dangdang.csv', 'a', newline='', encoding='gb18030') as f:
            csvwriter = csv.writer(f, delimiter=',')
            for title, price, link in zip(titles, prices, links):
                csvwriter.writerow([title, price, link])

    def main(self):
        for page in range(1, 11):
            #url = self.url.format(product, page)
            html = self.get_html(url)
            self.parse_html(html)


if __name__ == '__main__':
    spider = dangdang()
    spider.main()
