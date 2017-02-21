# -*- coding:utf-8 -*-

import scrapy
from ZhihuSpider.items import ZhihuspiderItem
from bs4 import BeautifulSoup

class ZhSpider(scrapy.Spider):

    name = "zh_spider"
    start_urls = ['http://tieba.baidu.com/f?kw=%D0%C2%D4%AB%BD%E1%D2%C2&fr=ala0&loc=rec']

    def parse(self, response):
        item = ZhihuspiderItem()
        soup = BeautifulSoup(response.body, "html5lib")

        sites = soup.find_all(class_=' j_thread_list clearfix')

        for site in sites:
            item["title"] = site.find(class_="threadlist_lz clearfix").div.a.get_text()
            item["author"] = site.find(class_="frs-author-name-wrap").a.get_text()
            # print item["title"], item["author"]
            yield item
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