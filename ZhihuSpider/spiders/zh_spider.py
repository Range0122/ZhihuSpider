# -*- coding:utf-8 -*-

import scrapy
from ZhihuSpider.items import ZhihuspiderItem

class ZhSpider(scrapy.Spider):

    name = "zh_spider"
    start_urls = ['http://tieba.baidu.com/f?kw=%D0%C2%D4%AB%BD%E1%D2%C2&fr=ala0&loc=rec']

    def parse(self, response):
        item = ZhihuspiderItem()
        # sel = response.xpath('//*[@id="thread_list"]/li[@class=" j_thread_list clearfix"]').extract()
        # print sel
        for sel in response.xpath('//*[@id="thread_list"]/li[@class=" j_thread_list clearfix"]'):
            item['title'] = sel.xpath('//*[@class="threadlist_title pull_left j_th_tit "]/a/@title').extract()
            print item['title']
            yield item