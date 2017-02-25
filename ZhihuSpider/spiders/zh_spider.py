# -*- coding:utf-8 -*-

import scrapy
from ZhihuSpider.items import ZhihuspiderItem
from bs4 import BeautifulSoup
import re
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class ZhSpider(scrapy.Spider):

    name = "zh_spider"
    start_urls = ['http://tieba.baidu.com/f?kw=%D0%C2%D4%AB%BD%E1%D2%C2&fr=ala0&loc=rec']


    def parse(self, response):

        soup = BeautifulSoup(response.body, "html5lib")
        basic_url = "http://tieba.baidu.com"

        sites = soup.find_all(class_=' j_thread_list clearfix')

        for site in sites:
            item = ZhihuspiderItem()
            item["title"] = site.find(class_="threadlist_lz clearfix").div.a.get_text()
            item["author"] = site.find(class_="frs-author-name-wrap").a.get_text()
            item["url"] = basic_url + site.find(class_="threadlist_lz clearfix").div.a['href']
            requests = scrapy.Request(item["url"], callback=self.parse_item)
            requests.meta["item"] = item
            yield requests


    def parse_item(self, response):
        item = response.meta["item"]
        item["content"] = re.findall(r'class="d_post_content j_d_post_content  clearfix">([\s]*[\S]*)?<img class', response.body)[0].replace('<br>', '')
        return item

        # l = ItemLoader(item=ZhihuspiderItem(), response=response)
        #
        #
        # # for sel in response.xpath('//*[@id="thread_list"]/li[@class=" j_thread_list clearfix"]'):
        #
        # l.add_xpath('title', '//*[@class="threadlist_title pull_left j_th_tit "]/a/@title')
        # l.add_xpath('author', '//*[@class="frs-author-name-wrap"]/a/text()')
        # yield l.load_item()

            # item['title'] = sel.xpath('//*[@class="threadlist_title pull_left j_th_tit "]/a/@title').extract()
            # item['author'] = sel.xpath('//*[@class="frs-author-name-wrap"]/a/text()').extract()
            # yield item