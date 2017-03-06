# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs


# from scrapy.mail import MailSender
# mailer = MailSender()

class ZhihuspiderPipeline(object):
    # def open_spider(self, spider):
    #     self.file = codecs.open('F:\\data.txt', 'a', encoding='utf-8')
    #     self.file.truncate()
    #     self.file.close()
    #     return 0
    def process_item(self, item, spider):
        with codecs.open('F:\\w_data.txt', 'a', encoding='utf-8') as f:
            f.write(item["url"] + ' ' + item["title"] + ' ' + item["author"] + ' ' + item["content"] + '\r')
        return item
