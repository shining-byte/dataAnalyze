from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets

from taobao.models import JDProductsItem, JDCommentItem
from utils.scrapy_web import ScrapyInfo, scrapy_JD, scrapy_taobao


def index(request):
    return render(request, 'index.html')


def show(request, id):
    print(id)
    keyword = request.session['keyword']
    # 初始化类
    spider = ScrapyInfo(jdid=id, keyword=keyword)
    # 开始爬虫
    spider.scrapy_JDinfo()
    # scrapy_info(id=id)

    # 饼图
    pie = spider.pie()
    # comment_item = json.loads(text1[0], strict=False)['comments'][:3]
    comments = JDCommentItem.objects.all()[:3]

    # 云词图
    worldud = spider.worldcloud()


    mydict = dict(pie, **worldud)
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
    if request.method == 'GET':
        keyword = request.GET.get('search')
        request.session['keyword'] = keyword
        # request['keyword'] = keyword
        scrapy_JD(keyword)
        scrapy_taobao(keyword)
        products = JDProductsItem.objects.filter(name=keyword)

    return render(request, 'reslut.html', {'products': products})


# rest framework

# class ShowListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
#     """
#     主页面序列化
#     """
#     queryset =









