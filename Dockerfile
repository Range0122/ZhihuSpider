#@IgnoreInspection BashAddShebang
FROM python:2.7-onbuild

RUN pip install -r requirements.txt

ENTRYPOINT ["scrapy"]
CMD ["crawl", "zh_spider"]
