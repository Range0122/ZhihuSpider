# -*- coding:utf-8 -*-

import scrapy
from ZhihuSpider.items import ZhihuspiderItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from bs4 import BeautifulSoup
from scrapy_redis.spiders import RedisCrawlSpider, RedisSpider
import re
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class ZhSpider(CrawlSpider):
    """Follow categories and extract links."""
    name = 'zh_spider'
    start_urls = ['http://tieba.baidu.com/f?kw=%D0%C2%D4%AB%BD%E1%D2%C2&fr=ala0&loc=rec']
    redis_key = 'zh_spider:start_urls'
    rules = [
        Rule(LinkExtractor(allow=('utf-8&pn'), unique=True),
             callback='parse_page', follow=True),
    ]
    # restrict_xpaths = ('//a[@class="next pagination-item "]/@href',)

    def parse_page(self, response):
        soup = BeautifulSoup(response.body, "lxml")
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
        item["content"] = re.findall(r'class="d_post_content j_d_post_content  clearfix">([\s]*[\S]*)?<img class',
                                     response.body)[0].replace('<br>', '')
        return item
