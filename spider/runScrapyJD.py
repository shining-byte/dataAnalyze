# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :19-3-18
from scrapy import cmdline

from spider.spiders.scrapy_jingdong import JDSpider
JDSpider.start_urls = ['https://search.jd.com/Search?keyword=小米8&enc=utf-8&spm=2.1.0']
cmdline.execute("scrapy crawl JD".split())