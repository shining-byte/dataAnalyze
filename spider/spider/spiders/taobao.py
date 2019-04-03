# -*- coding: utf-8 -*-
import re
import json
import requests
import scrapy
from spider.items import *
from scrapy.http import Request


class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['taobao.com', 'rate.tmall.com']

    def __init__(self, keyword=None, *args, **kwargs):
        super(TaobaoSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://s.taobao.com/search?q={}'.format(keyword)]
        self.keyword = keyword

    def parse(self, response):
        prices = re.findall('"view_price":"(.*?)",', response.text)[1]  # 正则提示商品价格
        nid = re.findall('"nid":"(.*?)"', response.text)[1]  # 正则匹配id
        Product = ProductName()
        Product['taobaoProductId'] = nid
        Product['name'] = self.keyword
        yield Product
        taobaoproduct = TaobaoProduct()
        taobaoproduct['productid'] = nid
        taobaoproduct['productname'] = self.keyword
        taobaoproduct['productprice'] = prices
        taobaoproduct['producturl'] = 'https://detail.tmall.com/item.htm?spm=a230r.1.14.6.70de7ffcZej9q8&id={}&cm_id=140105335569ed55e27b&abbucket=20&sku_properties=10004:1617715035;5919063:6536025'.format(nid)
        yield taobaoproduct
        data = {}
        data['id'] = nid
        taobao_sumtagurl = 'https://rate.tmall.com/listTagClouds.htm?itemId={0}&isAll=true&isInner=true&t=&groupId=&_ksTS='.format(nid)

        yield Request(url=taobao_sumtagurl, callback=self.parse_comment, meta=data, dont_filter=True)

    def parse_comment(self, response):
        # taobao_sumtagurl = 'https://rate.tmall.com/listTagClouds.htm?itemId={0}&isAll=true&isInner=true&t=&groupId=&_ksTS='.format(response.meta['id'])
        id = response.meta['id']
        # response = json.loads(response.text)
        response = response.text
        response = response.replace('(', '')
        response = response.replace(')', '')
        taoboatag = json.loads(response)['tags']['tagClouds']
        taobaolist = [[taoboatag[i]['tag'] for i in range(len(taoboatag))],[taoboatag[i]['count'] for i in range(len(taoboatag))]]
        for i in taoboatag:
            taobaotag = TaobaoTag()
            taobaotag['tagname'] = i['tag']
            taobaotag['productid'] = id
            taobaotag['tagcount'] = i['count']
            yield taobaotag
        taobao_comurl = 'https://rate.tmall.com/list_detail_rate.htm?itemId={}&spuId=1152764912&sellerId=2024314280&order=3&currentPage=1&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098'.format(id)

        text = requests.get(taobao_comurl).text
        text = text.replace('jsonp128(', '')
        text = text.replace(')', '')
        jsons = json.loads(text)
        comment = jsons['rateDetail']['rateList'][:10]
        for i in comment:
            taobaocomments = TaobaoComment()
            taobaocomments['displayUserNick'] = i['displayUserNick']
            taobaocomments['rateContent'] = i['rateContent']
            taobaocomments['productid'] = id
            yield taobaocomments

