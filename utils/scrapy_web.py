# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :19-3-30
import math
import re
import subprocess
from pyecharts import Line3D, Pie, WordCloud

from taobao.models import ProductsItem, CommentItem
import requests
from scrapy.selector import Selector

REMOTE_HOST = "https://pyecharts.github.io/assets/js"


class ScrapyInfo:
    def __init__(self,id):
        # self.web = self.web
        self.id = id
        self.piename = []
        self.piecount = []
        self.woldname = []
        self.worldcount = []

    def scrapy_info(self):
        comment_url = 'https://sclub.jd.com/comment/productPageComments.action?productId={}&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'.format(self.id)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
                   'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20'}
        response = requests.get(url=comment_url, headers=headers)
        # response.encoding = 'utf8'
        # print('-------------'+response.text)
        data = response.json()
        commentSummary = data.get('productCommentSummary')
        self.piename = ['追评人数', '中评', '好评', '差评']
        self.piecount.append(commentSummary['showCount'])
        # v1.append(json2['defaultGoodCount'])
        self.piecount.append(commentSummary['generalCount'])
        self.piecount.append(commentSummary['goodCount'] - commentSummary['defaultGoodCount'])
        self.piecount.append(commentSummary['poorCount'])

        for hotComment in data['hotCommentTagStatistics']:
            self.woldname.append(hotComment['name'])
            self.worldcount.append(hotComment['count'])


        for comment_item in data['comments']:
            if (comment_item.get('content')[:7] in '此用户未及时填写评价内容，系统默认评价！'):
                pass
            if (len(comment_item.get('content')) <= 6):
                pass
            else:
                comment = {}
                # comment['shop_id'] = shop_id
                # comment['userid'] = comment_item.get('id')
                comment['content'] = comment_item.get('content')
                # comment['creationTime'] = comment_item.get('creationTime')
                # comment['days'] = comment_item.get('days')
                # comment['firstCategory'] = comment_item.get('firstCategory')
                # comment['imageCount'] = comment_item.get('imageCount')
                comment['nickname'] = comment_item.get('nickname')
                # comment['productColor'] = comment_item.get('productColor')
                # comment['productId'] = product_id
                # comment['productSize'] = comment_item.get('productSize')
                # comment['referenceId'] = comment_item.get('referenceId')
                # comment['referenceName'] = comment_item.get('referenceName')
                comment['score'] = comment_item.get('score')
                comment['userLevelName'] = comment_item.get('userLevelName')

    # 元饼图
    def pie(self):

        pie = Pie("")
        # 传入两个列表
        pie.add("", self.piename, self.piecount, is_label_show=True)
        return pie

    # 云词
    def worldcloud(self):
        wordcloud = WordCloud(width=1300, height=620)
        # 传入两个列表
        wordcloud.add("", self.woldname, self.worldcount, word_size_range=[20, 100])
        return wordcloud

    def line3d(self):
        _data = []
        for t in range(0, 25000):
            _t = t / 1000
            x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
            y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
            z = _t + 2.0 * math.sin(75 * _t)
            _data.append([x, y, z])
        range_color = [
            '#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
            '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
        line3d = Line3D("3D line plot demo", width=1200, height=600)
        line3d.add("", _data, is_visualmap=True,
                   visual_range_color=range_color, visual_range=[0, 30],
                   is_grid3D_rotate=True, grid3D_rotate_speed=180)
        return line3d


def scrapy_JD(keyword):

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0','authorization':'oauth c3cef7c66a1843f8b3a9e6a1e3160e20'}
    response = requests.get(url='https://search.jd.com/Search?keyword={}&enc=utf-8&spm=2.1.0'.format(keyword), headers=headers)
    response.encoding = 'utf8'

    selector = Selector(response)
    # productsItem = ProductsItem()
    price = selector.xpath('//*[@id="J_goodsList"]/ul/li/div/div/strong/i/text()').extract()[:10]
    name = selector.xpath('//*[@id="J_goodsList"]/ul/li/div/div/a/em/font/text()').extract()[:10]
    desc = selector.xpath('//*[@id="J_goodsList"]/ul/li/div/div/a/em/text()').extract()[:10]
    # // *[ @ id = "J_goodsList"] / ul / li[1] / div / div[1] / a / img
    imgurl = selector.xpath('//*[@id="J_goodsList"]/ul/li/div/div[1]/a/img/@source-data-lazy-img').extract()[:10]
    idurl = selector.xpath('//*[@id="J_goodsList"]/ul/li/div/div[4]/a/@href').extract()[:10]
    id = [re.compile('com/(.*?).html').findall(i)[0] for i in idurl]
    url = ['https:' + i for i in idurl]
    category = selector.xpath('//*[@id="J_selector"]/div[1]/div/div[2]/div[1]/ul/li[1]/a/text()').extract()

    for i in range(len(price)):
        try:
            product = ProductsItem.objects.create(productid=id[i], category=category[0], description=desc[i], name=name[i],
                                                  imgurl=imgurl[i], reallyPrice=price[i], url=url[i])
            product.save()
        except Exception as e:
            print(e)

