# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :19-3-18
import subprocess
from scrapy import cmdline

from spider.spiders.scrapy_jingdong import JDSpider

if __name__ =='__main__':

    JDSpider.start_urls = ['https://search.jd.com/Search?keyword={}&enc=utf-8&spm=2.1.0'.format('魅族16')]
    cmdline.execute("scrapy crawl JD".split())
# subprocess.Popen("scrapy crawl JD".split())
# print('----------------------')



