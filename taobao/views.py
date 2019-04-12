from django.shortcuts import render
import time

from pypinyin import lazy_pinyin

from taobao.models import *
from taobao.serializers import *

from utils.scrapy_web import *


def index(request):
    return render(request, 'index.html')


def index3(request):
    return render(request, 'index3.html')


def onlineshop(request):
    return render(request, 'onlineshop.html')


# 不入数据库,实时爬取
def search_reslut(request):
    keyword = request.GET.get('q')
    # 获取京东id
    try:
        jdlist = scrapy_JD2(keyword)
        suninglist = scrapy_suning2(keyword)
        taobaolist = scrapy_taobao(keyword)
    except Exception as e:
        print(e)
    userAgent = request.META['HTTP_USER_AGENT']
    _long_matches = r'googlebot-mobile|android|avantgo|blackberry|blazer|elaine|hiptop|ip(hone|od)|kindle|midp|mmp|mobile|o2|opera mini|palm( os)?|pda|plucker|pocket|psp|smartphone|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce; (iemobile|ppc)|xiino|maemo|fennec'
    _long_matches = re.compile(_long_matches, re.IGNORECASE)
    _short_matches = r'1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|e\-|e\/|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(di|rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|xda(\-|2|g)|yas\-|your|zeto|zte\-'
    _short_matches = re.compile(_short_matches, re.IGNORECASE)

    if _long_matches.search(userAgent) != None:
        return render(request, 'phone.html', {'jdlist': jdlist, 'suninglist': suninglist, 'keyword': keyword, 'taobaolist': taobaolist})
    user_agent = userAgent[0:4]
    if _short_matches.search(user_agent) != None:
        return render(request, 'phone.html', {'jdlist': jdlist, 'suninglist': suninglist, 'keyword': keyword, 'taobaolist': taobaolist})
    else:

        # 爬取京东
        # spider = ScrapyInfo(jdid=id, keyword=keyword)
        # spider.scrapy_JDinfo()
        # print(new_dict)
        # for price, desc, imgurl, id, url in new_dict.items:
        #     print(price, desc, imgurl)
        return render(request, 'search_reslut.html', {'jdlist': jdlist, 'suninglist': suninglist, 'keyword': keyword, 'taobaolist': taobaolist})


def hotel(request):
    return render(request, 'hotel.html')


def travel(request):
    return render(request, 'travel.html')


def cate(request):
    return render(request, 'cate.html')


# 酒店搜索结果
def hotel_reslut(request):
    q = request.GET.get('q')
    try:
        meituan = Meituan(q)
        ctrip = Ctrip(q)
        meituanlist = meituan.hotels
        ctriplist = ctrip.hotels
    except Exception as e:
        print(e)
    return render(request, 'hotel_reslut.html', {'meituanlist': meituanlist, 'ctriplist': ctriplist})


# 旅游搜索结果
def travel_reslut(request):
    q = request.GET.get('q')
    print(q)
    info = scrapy_tuniu(q)
    print(info)

    return render(request, 'travel_reslut.html', {'info': info})


# 美食搜索结果
def cate_reslut(request):
    city = request.GET.get('q')
    #  先获取id
    id = scrapy_mafengwoCityId(city)
    # 再该城市的美食
    cates = scrapy_maofengwo(id)
    return render(request, 'cate_reslut.html', {'cates': cates})


# 地图
def map(request):
    return render(request, 'map.html')


# 导航
def navigation(request):
    origin = request.GET.get('origin')
    destination = request.GET.get('destination')
    way = request.GET.get('way')
    return render(request, 'navigation.html', {'origin': origin, 'destination': destination, 'way': way})


# 食物
def food(request):
    return render(request, 'food.html')


# 食物相克
def checkfood(request):
    food = request.GET.get('q')
    pinyin = ''.join(lazy_pinyin(food))
    url = 'http://shiwuxiangke.00cha.com/{}.html'.format(pinyin)
    response = requests.get(url)
    response.encoding = 'gb2312'
    text = response.text
    info = re.compile('<div class="zynr">.*?<h1.*?">(.*?)</h1>.*?<img.*?src="(.*?)".*?>.*?</div>', re.S).findall(text)
    # print(info)
    title = info[0][0]
    imgurl = 'http://shiwuxiangke.00cha.com/'+info[0][1]
    content = re.compile('<p>(.*?)</p>', re.S).findall(text)
    return render(request, 'food_reslut.html', {'content': content[0], 'title': title, 'imgurl': imgurl})


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
        # 判断是否已经爬过
        if(ProductName.objects.filter(name=keyword)):
            print('已经爬取过京东，跳过')
        else:
            print('没爬过,先获取jd的id并生成')
            id = scrapy_JD(keyword)
            spider = ScrapyInfo(jdid=id, keyword=keyword)
            spider.scrapy_JDinfo()
            print('开始爬取京东')


        # 判断是否爬过淘宝
        if ProductName.objects.get(name=keyword).taobaoProductId == '0':
            # 爬取淘宝
            print('开始爬取淘宝')
            import requests

            url = 'http://127.0.0.1:6800/schedule.json'
            dictdata = {"project": 'default', "spider": 'taobao', 'keyword': '{}'.format(keyword)}

            r = requests.post(url=url, data=dictdata)
            print(r.text)

        else:
            print(ProductName.objects.get(name=keyword).taobaoProductId)
            print('已经爬取过淘宝，跳过')


        # 爬取苏宁
        if ProductName.objects.get(name=keyword).suningId == '0':

            print('开始爬取苏宁')
            scrapy_suning(keyword)
        else:
            print('已经爬取苏宁，跳过')

        # 取到id
        try:
            taobaoid = ProductName.objects.get(name=keyword).taobaoProductId
        except Exception:
            time.sleep(2)
            taobaoid = ProductName.objects.get(name=keyword).taobaoProductId
        jdid = ProductName.objects.get(name=keyword).jdProductId
        jd = JDProductsItem.objects.get(productid=jdid)
        jdurl = jd.url
        jdprice = jd.reallyPrice
        dict = {}

        # taobao
        try:
            taobao = TaobaoProduct.objects.filter(productid=taobaoid)[0]
            taobaoprice = taobao.productprice
            taobaourl = taobao.producturl
            dict['taobaoprice'] = taobaoprice
            dict['taobaourl'] = taobaourl
        except Exception as e:
            print(e)

            # taobao = TaobaoProduct.objects.filter(productid=taobaoid)[0]

        # 取评论
        try:
            taobaocomments = TaobaoComment.objects.filter(productid=taobaoid)[:10]
            jdcomments = JDCommentItem.objects.filter(productid=jdid)[:10]
            suningid = ProductName.objects.get(name=keyword).suningId
            suningcomments = SuNingComment.objects.filter(productid=suningid)[:10]
            suningurl = SuNingProduct.objects.get(productid=suningid).producturl
            dict['jdid'] = jdid
            dict['jdurl'] = jdurl
            dict['jdprice'] = jdprice
            dict['taobaoid'] = taobaoid
            dict['taobaocomments'] = taobaocomments
            dict['jdcomments'] = jdcomments
            dict['suningid'] = suningid
            dict['suningcomments'] = suningcomments
            dict['suningurl'] = suningurl
        except Exception as e:
            print(e)
    return render(request, 'show2.html', dict)











