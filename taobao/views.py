from django.shortcuts import render
from rest_framework import mixins, viewsets, filters
from django.db import connection
from django.db.utils import OperationalError

from taobao.filter import JDHotCommentTagFilter
from taobao.models import *
from taobao.serializers import *
from django_filters.rest_framework import DjangoFilterBackend

from taobao.serializers_pagination import *
from utils.scrapy_web import ScrapyInfo, scrapy_JD, scrapy_taobao, pie, worldcloud, pie2


def index(request):
    return render(request, 'index.html')


def show(request, id):
    keyword = request.session['keyword']
    taobaoProductId = request.session['taobaoproductId']
    # 初始化类
    spider = ScrapyInfo(jdid=id, taobaoProductId=taobaoProductId, keyword=keyword)
    # 开始爬取京东
    jdlist = spider.scrapy_JDinfo()
    taobaolist = spider.scrapy_taobaoinfo()
    # scrapy_info(id=id)

    #     comments = JDCommentItem.objects.all()[:3]
    # 饼图
    jdpie = pie(jdlist[0], jdlist[1])
    # comment_item = json.loads(text1[0], strict=False)['comments'][:3]

    taobaopie = pie2(taobaolist[0], taobaolist[1])
    # 云词图
    jdworldud = worldcloud(jdlist[2], jdlist[3])

    comments = JDCommentItem.objects.all()[:3]
    mydict = dict(jdpie, **jdworldud)
    mydict['comments'] = comments
    url = JDProductsItem.objects.get(name=keyword).url
    mydict['url'] = url

    return render(request, 'show.html', mydict)


def search(request):
    if request.method == 'GET':
        keyword = request.GET.get('search')
        request.session['keyword'] = keyword
        # request['keyword'] = keyword
        scrapy_JD(keyword)
        taobaoProductId = scrapy_taobao(keyword)
        request.session['taobaoproductId'] = taobaoProductId
        products = JDProductsItem.objects.filter(name=keyword)

    return render(request, 'reslut.html', {'products': products})











