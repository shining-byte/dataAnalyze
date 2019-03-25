# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :19-3-18
from scrapy import cmdline

from spider.spiders.scrapy_jingdong import JDSpider
JDSpider.start_urls = ['https://item.jd.com/100000232304.html']
cmdline.execute("scrapy crawl JD".split())