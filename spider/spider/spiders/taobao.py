# -*- coding: utf-8 -*-
import scrapy


class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['taobao.com']
    # start_urls = ['https://rate.tmall.com/list_detail_rate.htm?itemId=587578411300&spuId=1152764912&sellerId=2024314280&order=3&currentPage=1&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098']
    start_urls = ['https://www.taobao.com/']

    def parse(self, response):
        pass
import re
import json
import scrapy
from scrapy.http import Request


import requests
from spider.items import *


#
# class taobaoSpider(scrapy.Spider):
#     # name = 'taobao'
#     name = 'taobao'
#     allowed_domains = ['taobao.com']
#
#     start_urls = ['https://rate.tmall.com/list_detail_rate.htm?itemId=587578411300&spuId=1152764912&sellerId=2024314280&order=3&currentPage=1&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098']
#
#     def parse(self, response):
#         print(response.text)
