from django.shortcuts import render

# Create your views here.

import math
import json
import re
import subprocess
from pyecharts import Line3D, Pie, WordCloud

from taobao.models import ProductsItem, CommentItem
import requests
from scrapy.selector import Selector

from utils.scrapy_web import scrapy_JD, ScrapyInfo

REMOTE_HOST = "https://pyecharts.github.io/assets/js"

def index(request):
    return render(request, 'index.html')

    # try:
    #     product = CommentSummaryItem.objects.create(productid=id[i], category=category[0], description=desc[i], name=name[i],
    #                                           imgurl=imgurl[i], reallyPrice=price[i], url=url[i])
    #     product.save()
    # except Exception as e:
    #     print(e)
    # print(json.loads(response.text))


def show(request, id):
    # 初始化类
    spider = ScrapyInfo(id=id)
    # 开始爬虫
    spider.scrapy_info()
    # scrapy_info(id=id)
    print(id)
    pe = spider.pie()
    # comment_item = json.loads(text1[0], strict=False)['comments'][:3]
    comments = CommentItem.objects.all()[:3]
    pie = dict(
        mypie=pe.render_embed(),
        host=REMOTE_HOST,
        script_list=pe.get_js_dependencies()
    )

    worldud = spider.worldcloud()
    world = dict(
        myworldcloud = worldud.render_embed(),
        host=REMOTE_HOST,
        script_list=worldud.get_js_dependencies()
    )

    mydict = dict(pie, **world)
    mydict['comments'] = comments
    # mydict2 = dict(mydict, **commentdict)
    #
    # print(mydict['mypie'])
    # # # print(mydict)
    # print(context['mypie'])
    return render(request, 'show.html',mydict)

from twisted.internet import reactor,defer
import scrapy
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from scrapy.utils.log import configure_logging
import os

from spider.spiders.scrapy_jingdong import JDSpider

# configure_logging()
# runner = CrawlerRunner()


def search(request):
    if request.method == 'POST':
        print(request.POST.get('search'))
    if request.method == 'GET':
        keyword = request.GET.get('search')
        scrapy_JD(keyword)
        products = ProductsItem.objects.filter(name=keyword)

    return render(request, 'reslut.html', {'products': products})










