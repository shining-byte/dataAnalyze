from django.shortcuts import render

from taobao.models import *
from taobao.serializers import *

from utils.scrapy_web import ScrapyInfo, scrapy_JD


def index(request):
    return render(request, 'index.html')


# def show(request, id):
#     mydict = {}
#     if(ProductName.objects.filter(jdProductId=id)):
#         taobaoProductId = request.session['taobaoproductId']
#         mydict['jdproductid'] = id
#         mydict['taobaoproductId'] = taobaoProductId
#         print(mydict)
#         return render(request, 'show2.html', mydict)
#
#     else:
#         keyword = request.session['keyword']
#         taobaoProductId = request.session['taobaoproductId']
#         # 初始化类
#         spider = ScrapyInfo(jdid=id, taobaoProductId=taobaoProductId, keyword=keyword)
#         # 开始爬取京东
#         jdlist = spider.scrapy_JDinfo()
#         # taobaolist = spider.scrapy_taobaoinfo()
#         # scrapy_info(id=id)
#
#         #     comments = JDCommentItem.objects.all()[:3]
#         # 饼图
#         # jdpie = pie(jdlist[0], jdlist[1])
#         # # comment_item = json.loads(text1[0], strict=False)['comments'][:3]
#         #
#         # taobaopie = pie2(taobaolist[0], taobaolist[1])
#         # # 云词图
#         # jdworldud = worldcloud(jdlist[2], jdlist[3])
#
#         jdcomments = JDCommentItem.objects.all()[:3]
#         taobaocomments = TaobaoComment.objects.all()[:10]
#         price = JDProductsItem.objects.get(productid=id).reallyPrice
#         # mydict = dict(jdpie, **jdworldud)
#         mydict['jdcomments'] = jdcomments
#         mydict['taobaocomments'] = taobaocomments
#         url = JDProductsItem.objects.get(name=keyword).url
#         mydict['url'] = url
#         mydict['price'] = price
#         mydict['taobaoproductid'] = taobaoProductId
#
#     return render(request, 'show2.html', mydict)


def search(request):
    if request.method == 'GET':
        keyword = request.GET.get('search')
        # request.session['keyword'] = keyword
        # request['keyword'] = keyword
        scrapy_JD(keyword)
        # taobaoProductId = scrapy_taobao(keyword)
        # request.session['taobaoproductId'] = taobaoProductId
        import requests

        url = 'http://127.0.0.1:6800/schedule.json'
        dictdata = {"project": 'default', "spider": 'taobao', 'keyword': '{}'.format(keyword)}

        requests.post(url=url, data=dictdata)

        # products = JDProductsItem.objects.filter(name=keyword)

    return render(request, 'show2.html', {'jdid': 12311, 'suningid': 98889, 'taobaoid': 46546})











