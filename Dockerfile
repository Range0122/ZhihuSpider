#@IgnoreInspection BashAddShebang
FROM python:2.7-onbuild

ENTRYPOINT ["scrapy"]
CMD ["crawl", "zh_spider"]
