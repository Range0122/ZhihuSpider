# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
SPIDER_MODULES = ['ZhihuSpider.spiders']
NEWSPIDER_MODULE = 'ZhihuSpider.spiders'

BOT_NAME = ['ZhihuSpider', ]

USER_AGENT = 'ZhihuSpider (+https://github.com/Range0122/ZhihuSpider/tree/master/ZhihuSpider)'

# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# SCHEDULER_PERSIST = True


#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

ITEM_PIPELINES = {
    'ZhihuSpider.pipelines.ZhihuspiderPipeline': 300,
    # 'scrapy_redis.pipelines.RedisPipeline': 400,
}

LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.

DOWNLOAD_DELAY = 0.5

# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
# REDIS_URL = '127.0.0.1:6379'
# REDIS_HOST = '127.0.0.1'
# REDIS_PORT = 6379