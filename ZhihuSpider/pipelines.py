# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import xml.dom.minidom

# from scrapy.mail import MailSender
# mailer = MailSender()


class ZhihuspiderPipeline(object):
    def __init__(self):
        self.impl = xml.dom.minidom.getDOMImplementation()
        self.dom = self.impl.createDocument(None, 'root', None)
        self.root = self.dom.documentElement
    #     self.file = codecs.open('F:\\data.txt', 'a', encoding='utf-8')
    #     self.file.truncate()
    #     self.file.close()
    #     return 0

    def process_item(self, item, spider):
        # with codecs.open('F:\\w_data.txt', 'a', encoding='utf-8') as f:
        #     f.write(item["url"] + ' ' + item["title"] + ' ' + item["author"] + ' ' + item["content"] + '\r')

        page = self.dom.createElement('page')
        self.root.appendChild(page)

        url = self.dom.createElement('url')
        title = self.dom.createElement('title')
        author = self.dom.createElement('author')
        content = self.dom.createElement('content')

        url_data = self.dom.createTextNode(item['url'])
        title_data = self.dom.createTextNode(item['title'])
        author_data = self.dom.createTextNode(item['author'])
        content_data = self.dom.createTextNode(item['content'])

        url.appendChild(url_data)
        title.appendChild(title_data)
        author.appendChild(author_data)
        content.appendChild(content_data)

        page.appendChild(url)
        page.appendChild(title)
        page.appendChild(author)
        page.appendChild(content)
        return item

    def close_spider(self, spider):
        print '***************** SPIDER FINISHED *******************'
        with open('data.xml', 'a') as f:
            self.dom.writexml(f, addindent='  ', newl='\n')
