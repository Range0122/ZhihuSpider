#����zhihu����������
����������֪���ģ��������õ�һ�γ���scrapy����ص�һЩ�����ͻ��˼�һ�����վ��
#����
##2017.03.02
��������һЩС�ĸĶ�����Ȼ�������£�

![Paste_Image.png](http://upload-images.jianshu.io/upload_images/4218178-60b937b60aff7ed3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


��֪��Ϊʲô�����`KeyError: 'Spider not found: zh_spider'`��`ImportError: No module named bs4`�Լ�`Could not load spiders from module 'ZhihuSpider.spiders'. Check SPIDER_MODULES setting`������Error
�����ܲ鵽��û�и�Redis��صģ���ֻ����`Scrapy`�е�`Settings`û�����úã�����û����ȷ`spider`��`name`����

���⻹��һ�����ʣ�

![Paste_Image.png](http://upload-images.jianshu.io/upload_images/4218178-f10213cc6da476f8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

�����ڻ�û����ȫŪ�����`spider`����ô����`docker`����ģ�����ĿǰҲֻ�Ǵ��������Redis�ֲ�ʽ��ԭ������`Dockerfile`��`docker-compose.yml`��`requirements.txt`�������ļ��ı�д��ʽ��ԭ�������Ǻ����ס�