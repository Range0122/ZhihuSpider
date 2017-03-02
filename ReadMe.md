#名叫zhihu的贴吧爬虫
本来是想爬知乎的，后来觉得第一次尝试scrapy及相关的一些包，就换了简单一点的网站。
#更新
##2017.03.02
早上做了一些小的改动，在cmd下执行`docker-compose up`语句后仍然报错。如下：

![Paste_Image.png](http://upload-images.jianshu.io/upload_images/4218178-60b937b60aff7ed3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


不知道为什么会出现`KeyError: 'Spider not found: zh_spider'`和`ImportError: No module named bs4`以及`Could not load spiders from module 'ZhihuSpider.spiders'. Check SPIDER_MODULES setting`这样的Error
网上能查到的没有跟Redis相关的，都只是在`Scrapy`中的`Settings`没有设置好，或者没有明确`spider`的`name`属性

另外还有一个疑问：

![Paste_Image.png](http://upload-images.jianshu.io/upload_images/4218178-f10213cc6da476f8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

到现在还没有完全弄清楚，`spider`是怎么传到`docker`这里的，而且目前也只是大概明白了Redis分布式的原理，对于`Dockerfile`、`docker-compose.yml`、`requirements.txt`这三个文件的编写方式，原理都还不是很明白。
