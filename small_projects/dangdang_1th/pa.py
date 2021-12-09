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
        self.headers = {'User-Agent': ua.random}

    def get_html(self, url):
        response = requests.get(url, headers=self.headers)
        html = response.text
        return html

    def parse_html(self, html):
        target = etree.HTML(html)
        pics = target.xpath('//li/div[@class="pic"]/a/img/@title')
        names = target.xpath('//li/div[@class="name"]/a/@title')
        stars = target.xpath(
            '//li/div[@class="star"]/span[@class="tuijian"]/text()')
        publisher_infos_foreign = target.xpath(
            '//li/div[@class="publisher_info"][1]/a[1]/text()')
        publisher_infos_mainland = target.xpath(
            '//li/div[@class="publisher_info"][2]/a/text()')

        price_n_s = target.xpath(
            '//li/div[@class="price"]/p[1]/span[@class="price_n"]/text()')
        price_r_s = target.xpath(
            '//li/div[@class="price"]/p[1]/span[@class="price_r"]/text()')
        price_s_s = target.xpath(
            '//li/div[@class="price"]/p[1]/span[@class="price_s"]/text()')
        price_e_s = target.xpath(
            '//li/div[@class="price"]/p[2][@class="price_e"]')

        with open('./dangdang.csv', 'a', newline='', encoding='gb18030') as f:
            csvwriter = csv.writer(f, delimiter=',')
            for name, star, author, publisher, price_n, price_r, price_s in zip(
                    names, stars, publisher_infos_foreign,
                    publisher_infos_mainland, price_n_s, price_r_s, price_s_s):
                csvwriter.writerow(
                    [name, star, author, publisher, price_n, price_r, price_s])

    def main(self):
        url = self.url
        html = self.get_html(url)
        self.parse_html(html)
        print("完成")


if __name__ == '__main__':
    spider = dangdang()
    spider.main()
