# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :19-3-18
import subprocess
from scrapy import cmdline
import os
import sys
import django
from django.core.wsgi import get_wsgi_application
sys.path.append(os.path.dirname(os.path.abspath('.')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'dataAnalyze.settings'
application = get_wsgi_application()
django.setup()
from spider.spiders.scrapy_jingdong import JDSpider



if __name__ == '__main__':
    JDSpider.start_urls = ['https://search.jd.com/Search?keyword={}&enc=utf-8&spm=2.1.0'.format('魅族16')]
    cmdline.execute("scrapy crawl JD".split())




