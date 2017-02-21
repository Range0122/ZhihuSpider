# -*- coding:utf-8 -*-

import scrapy
from ZhihuSpider.items import ZhihuspiderItem
from scrapy.contrib.loader import ItemLoader

class ZhSpider(scrapy.Spider):

    name = "zh_spider"
    start_urls = ['http://tieba.baidu.com/f?kw=%D0%C2%D4%AB%BD%E1%D2%C2&fr=ala0&loc=rec']

    def parse(self, response):
        l = ItemLoader(item=ZhihuspiderItem(), response=response)
        
        # item = ZhihuspiderItem()

        # for sel in response.xpath('//*[@id="thread_list"]/li[@class=" j_thread_list clearfix"]'):

        l.add_xpath('title', '//*[@class="threadlist_title pull_left j_th_tit "]/a/@title')
        l.add_xpath('author', '//*[@class="frs-author-name-wrap"]/a/text()')
        yield l.load_item()

            # item['title'] = sel.xpath('//*[@class="threadlist_title pull_left j_th_tit "]/a/@title').extract()
            # item['author'] = sel.xpath('//*[@class="frs-author-name-wrap"]/a/text()').extract()
            # yield item