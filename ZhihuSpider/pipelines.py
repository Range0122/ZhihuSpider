# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs

class ZhihuspiderPipeline(object):
    def process_item(self, item, spider):
        self.file = codecs.open('data.txt', 'w', encoding='utf-8')
        for line in item['title']:
            self.file.write(line + '\n')
        self.file.close()
        return item
