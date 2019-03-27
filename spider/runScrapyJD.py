# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :19-3-18
import subprocess
from scrapy import cmdline

from spider.spiders.scrapy_jingdong import JDSpider



JDSpider.start_urls = ['https://search.jd.com/Search?keyword={}&enc=utf-8&spm=2.1.0'.format('小米9')]
subprocess.Popen("scrapy crawl JD".split())
print('----------------------')



