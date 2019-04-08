# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :19-3-30
import json
import os
import re
import time


from taobao.models import *
import requests
from scrapy.selector import Selector



class ScrapyInfo:
    def __init__(self,**kwargs):
        # self.web = self.web
        self.jdid = kwargs['jdid']
        # self.taobaoProductId = kwargs['taobaoProductId']
        self.keyword = kwargs['keyword']
        # self.piename = []
        # self.piecount = []
        # self.woldname = []
        # self.worldcount = []

    def scrapy_JDinfo(self):
        comment_url = 'https://sclub.jd.com/comment/productPageComments.action?productId={}&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'.format(self.jdid)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
                   'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20'}
        response = requests.get(url=comment_url, headers=headers)
        data = response.json()
        commentSummary = data.get('productCommentSummary')
        # self.piename = ['追评人数', '中评', '好评', '差评']
        # self.piecount.append(commentSummary['showCount'])
        # self.piecount.append(commentSummary['generalCount'])
        # self.piecount.append(commentSummary['goodCount'] - commentSummary['defaultGoodCount'])
        # self.piecount.append(commentSummary['poorCount'])
        try:
            JDCommentSummaryItem.objects.create(afterCount=commentSummary['afterCount'], averageScore=commentSummary['averageScore'],
                                            commentCount=commentSummary['commentCount'], defaultGoodCount=commentSummary['defaultGoodCount'],
                                            generalCount=commentSummary['generalCount'], goodCount=commentSummary['goodCount'],
                                            imageListCount=data['imageListCount'], poorCount=commentSummary['poorCount'],
                                            score=data['score'], productid=self.jdid).save()
        except Exception as e:
            print(e)
        # pool = multiprocessing.Pool(multiprocessing.cpu_count())
        for hotComment in data['hotCommentTagStatistics']:
            name = hotComment['name']
            count = hotComment['count']
            saveJDhotTag(name, count, self.jdid)
            # self.woldname.append(name)
            # self.worldcount.append(count)
            # pool.apply_async(saveJDhotTag, (name, count, self.jdid))

        # pool.close()
        # pool.join()
        # pool2 = multiprocessing.Pool(multiprocessing.cpu_count())
        for comment_item in data['comments']:
            if (comment_item.get('content') == '此用户未及时填写评价内容，系统默认评价！') or comment_item.get('content' == '此用户未填写评价内容'):
                pass
            if (len(comment_item.get('content')) <= 6):
                pass
            else:
                content = comment_item.get('content')
                nickname = comment_item.get('nickname')
                score = comment_item.get('score')
                userLevelName = comment_item.get('userLevelName')
                # days = comment_item.get('days')
                # firstCategory= comment_item.get('firstCategory')
                # imageCount = comment_item.get('imageCount')
                # productColor = comment_item.get('productColor')
                # productSize = comment_item.get('productSize')
                referenceId = comment_item.get('referenceId')
                # referenceName = comment_item.get('referenceName')
                # secondCategory = comment_item.get('secondCategory')
                # thirdCategory = comment_item.get('thirdCategory')
                # userLevelId = comment_item.get('userLevelId')
                saveJDcomment(content, nickname, referenceId, score, userLevelName, self.jdid)
        # jdlist = [self.piename, self.piecount, self.woldname, self.worldcount]
        # return jdlist

        # pool2.close()
        # pool2.join()

    # def scrapy_taobaoinfo(self):
    #     taobao_sumtagurl = 'https://rate.tmall.com/listTagClouds.htm?itemId={0}&isAll=true&isInner=true&t=&groupId=&_ksTS='.format(self.taobaoProductId)
    #     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
    #                'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20'}
    #     response = requests.get(url=taobao_sumtagurl, headers=headers).text
    #     response = response.replace('(', '')
    #     response = response.replace(')', '')
    #     taoboatag = json.loads(response)['tags']['tagClouds']
    #     taobaolist = [[taoboatag[i]['tag'] for i in range(len(taoboatag))], [taoboatag[i]['count'] for i in range(len(taoboatag))]]
    #     for i in taoboatag:
    #         TaobaoTag.objects.create(tagname=i['tag'], productid_id=self.taobaoProductId, tagcount=i['count']).save()
    #     taobao_comurl = 'http://rate.tmall.com/list_detail_rate.htm?itemId={0}&sellerId=1652490016&currentPage=1'.format(self.taobaoProductId)
    #
    #     text = requests.get(taobao_comurl).text
    #     text = text.replace('jsonp128(', '')
    #     text = text.replace(')', '')
    #     jsons = json.loads(text)
    #     comment = jsons['rateDetail']['rateList'][:10]
    #     for i in comment:
    #         try:
    #             TaobaoComment.objects.create(displayUserNick=i['displayUserNick'], rateContent=i['rateContent'], productid_id=self.taobaoProductId).save()
    #             print(i['rateContent'])
    #         except Exception as e:
    #             print(e)
    #     return taobaolist


# 搜索时调用
def scrapy_JD(keyword):
    # 先保存产品
    try:
        product = ProductName.objects.create(name=keyword)
        product.save()
    except Exception as e:
        print(e)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0','authorization':'oauth c3cef7c66a1843f8b3a9e6a1e3160e20'}
    response = requests.get(url='https://search.jd.com/Search?keyword={}&enc=utf-8&spm=2.1.0'.format(keyword), headers=headers)
    response.encoding = 'utf8'
    selector = Selector(response)
    # productsItem = ProductsItem()
    price = selector.xpath('//*[@id="J_goodsList"]/ul/li/div/div/strong/i/text()').extract()[0]
    # name = selector.xpath('//*[@id="J_goodsList"]/ul/li/div/div/a/em/font/text()').extract()[0]
    desc = selector.xpath('//*[@id="J_goodsList"]/ul/li/div/div/a/em/text()').extract()[0]
    # // *[ @ id = "J_goodsList"] / ul / li[1] / div / div[1] / a / img
    imgurl = selector.xpath('//*[@id="J_goodsList"]/ul/li/div/div[1]/a/img/@source-data-lazy-img').extract()[0]
    idurl = selector.xpath('//*[@id="J_goodsList"]/ul/li/div/div[4]/a/@href').extract()[:1]
    id = [re.compile('com/(.*?).html').findall(i)[0] for i in idurl]
    url = ['https:' + i for i in idurl]
    category = selector.xpath('//*[@id="J_selector"]/div[1]/div/div[2]/div[1]/ul/li[1]/a/text()').extract()
    # print(selector.xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[4]/a/em/text()').extract())
    # print(name)
    # for i in range(len(price)):
    #     if name[i] == keyword:
    try:
        ProductName.objects.filter(name=keyword).update(jdProductId=id[0])

        product = JDProductsItem.objects.create(productid=id[0], category=category[0], description=desc,
                                            imgurl=imgurl, reallyPrice=price, url=url[0])
        product.save()
            #     product.save()
    except Exception as e:
        print(e)
    return id[0]


# 搜索时调用, 不入数据库
def scrapy_JD2(keyword):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0','authorization':'oauth c3cef7c66a1843f8b3a9e6a1e3160e20'}
    response = requests.get(url='https://search.jd.com/Search?keyword={}&enc=utf-8&spm=2.1.0'.format(keyword), headers=headers)
    response.encoding = 'utf8'
    selector = Selector(response)
    # productsItem = ProductsItem()
    price = selector.xpath('//*[@id="J_goodsList"]/ul/li/div/div/strong/i/text()').extract()[:5]
    # name = selector.xpath('//*[@id="J_goodsList"]/ul/li/div/div/a/em/font/text()').extract()[0]
    desc = selector.xpath('//*[@id="J_goodsList"]/ul/li/div/div/a/em/text()').extract()[:5]
    # // *[ @ id = "J_goodsList"] / ul / li[1] / div / div[1] / a / img
    imgurl = selector.xpath('//*[@id="J_goodsList"]/ul/li/div/div[1]/a/img/@source-data-lazy-img').extract()[:5]
    idurl = selector.xpath('//*[@id="J_goodsList"]/ul/li/div/div[4]/a/@href').extract()[:5]
    id = [re.compile('com/(.*?).html').findall(i)[0] for i in idurl][:5]
    # 购买链接
    url = ['https:' + i for i in idurl]
    # category = selector.xpath('//*[@id="J_selector"]/div[1]/div/div[2]/div[1]/ul/li[1]/a/text()').extract()

    new_list = []
    mid = map(list, zip(price, desc, imgurl, id, url))
    for item in mid:
        new_dict = dict(zip(['price', 'desc', 'imgurl', 'id', 'url'], item))
        new_list.append(new_dict)
    return new_list


# 搜索时调用
def scrapy_suning(keyword):
    url = 'https://search.suning.com/{}/'.format(keyword)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0','authorization':'oauth c3cef7c66a1843f8b3a9e6a1e3160e20'}
    text = requests.get(url, headers=headers).text
    suningid = re.compile('''<li docType="1".*?id="0000000000-(.*?)".*?</li>''', re.S).findall(text)[0]
    ProductName.objects.filter(name=keyword).update(suningId=suningid)
    # 价钱
    # suningproduct = 'https://product.suning.com/0000000000/{}.html'.format(suningid)
    # response = requests.get(url=suningproduct)
    # selector = Selector(response)
    # suningprice = selector.xpath('//*[@id="mainPrice"]/dl[1]/dd/span/text()').extract()
    # print(suningprice)

    SuNingProduct.objects.create(productid=suningid, producturl='https://product.suning.com/0000000000/{}.html'.format(suningid))
    # 获取标签
    tagurl = 'https://review.suning.com/ajax/getClusterReview_labels/general-30309172-0000000{}-0000000000-----commodityrLabels.htm?'.format(suningid)
    text = requests.get(url=tagurl).text
    text = text.replace('commodityrLabels(', '')

    text = text.replace(')', '')
    tagjsons = json.loads(text)['commodityLabelCountList']
    for i in tagjsons:
        SuNingTag.objects.create(productid=suningid, labelName=i['labelName'], labelCnt=i['labelCnt']).save()

    for i in range(2):
        suningcommenturl = 'https://review.suning.com/ajax/cluster_review_lists/general-30309172-0000000{}-0000000000-total-{}-default-10-----reviewList.htm'.format(suningid, i+1)
        text = requests.get(url=suningcommenturl).text
        text = text.replace('reviewList(', '')
        text = text.replace(')', '')
        datajsons = json.loads(text)
        for j in datajsons['commodityReviews']:
            if j['content'] == '此用户没有填写评价内容' or len(j['content']) <= 20:
                pass
            SuNingComment.objects.create(productid=suningid, content=j['content'], nickName=j['userInfo']['nickName'],
                                         levelName=j['userInfo']['levelName']).save()# 搜索时调用


# 不入数据库
def scrapy_suning2(keyword):
    url = 'https://search.suning.com/{}/'.format(keyword)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0','authorization':'oauth c3cef7c66a1843f8b3a9e6a1e3160e20'}
    text = requests.get(url, headers=headers).text
    info = re.compile('''<a target="_blank".*?href="(.*?)"class="sellPoint".*?<img alt="(.*?)" src="(.*?)">''',
                      re.S).findall(text)[:5]
    suninglist = []
    for i in range(len(info)):
        suninglist = []
        for i in range(len(info)):
            list1 = ['url', 'desc', 'imgurl']
            list2 = info[i]
            suningdict = dict(zip(list1, list2))
            suninglist.append(suningdict)
    return suninglist


# 保存京东标签
def saveJDhotTag(*args):
    JDHotCommentTagItem.objects.create(name=args[0], count=args[1], productid=args[2]).save()


# 保存京东评论信息
def saveJDcomment(*args):

    jdcomment = JDCommentItem.objects.create(content=args[0], nickname=args[1], referenceId=args[2],
                                             score=args[3], userLevelName=args[4], productid=args[5])
    jdcomment.save()


# 爬取酒店
class Ctrip:
    def __init__(self,city,star=3):
        local_path = os.path.dirname(os.path.realpath(__file__))
        area = open(local_path+'/Ctrip', mode='r')  #读取城市字典
        self.__cities = eval(area.readline())
        self.page=1 #当前页数
        self.city=city #当期城市
        self.star=star #当前酒店等级
        self.hotels=[] #所有酒店列表
        self.changeCity(self.city)
        area.close()

    def __geturl(self,city,page):
        return "https://hotels.ctrip.com/hotel/"+self.__cities[city][0]+self.__cities[city][1]+"/p"+str(page)

    #改变城市
    def changeCity(self,city,star=3,page=1):
        try:
            self.city=city
            self.star=star
            self.page=page
            headers={
                "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
            }
            datas={
                #'checkIn':'2019-4-5', #入住日期
                #'checkOut':'2019-04-07', #退房日期
                #'RoomGuestCount':'5,2,1,12',#房间数，成人数，儿童数，儿童岁数+
                'Star':star #星级数
            }
            respon=requests.post(self.__geturl(self.city, self.page), headers=headers, data=datas)
            respon.raise_for_status()
            respon.encoding=respon.apparent_encoding
            page=respon.text
            names = re.findall(r'hotel_item_pic.*?title="(.*?)"', page, re.S)  #酒店名称
            id = re.findall(r'<h2 class="hotel_name" data-id="(.*?)">', page, re.S)  #酒店ID
            pic_href = re.findall(r'<img alt=.*? src="(.*?)"', page, re.S)  #图片地址
            for i in range(len(pic_href)):  # 清洗数据
                pic_href[i] = pic_href[i][2:]
            locations = re.findall(r'<p class="hotel_item_htladdress">(.*?) <a href="javascript', page, re.S)  #酒店地址

            for i in range(len(locations)):  # 清洗数据
                if '】' in locations[i]:
                    locations[i] = locations[i].split('】')[1]

            scores = re.findall(r'"hotel_value">(.*?)</span>', page, re.S)  #酒店评分
            prices = re.findall(r'<span class="J_price_lowList">(.*?)</span>', page, re.S)  #酒店价格
            recommends = re.findall(r'009933.*?>(.*?)</span>用户推荐', page, re.S)  #推荐比例
            peoples = re.findall(r'FF9900.*?>(\d+)</span>位住客点评', page, re.S)  #推荐人数
            hotels = []
            for name, id, pic_href, location, score, price, recommend, people in zip(names, id, pic_href, locations,
                                                                                       scores, prices, recommends,
                                                                                       peoples):
                data = {}
                data['name'] = name
                data['id'] = id
                data['score'] = score
                data['price'] = price
                data['recommend_ratio'] = recommend
                data['people_num'] = people
                data['location'] = location
                data['pic_href'] = pic_href
                data['href']= 'https://hotels.ctrip.com/hotel/'+data['id']+'.html' #酒店地址
                hotels.append(data)
            self.hotels=hotels #所有酒店列表
        except Exception as e:
            print(e)

    #改变页数
    def changePage(self,page):
        self.changeCity(self.city,self.star,page)

    def __str__(self):
        return str(self.hotels)


# 美团酒店
class Meituan:
    def __init__(self, city):
        local_path = os.path.dirname(os.path.realpath(__file__))
        meituan = open(local_path+"/meituan.txt", mode='r')#读取城市字典
        self.__cities = eval(meituan.readline())
        self.city = city #当前城市
        self.page = 1 #当前页面
        self.hotels = [] #所有酒店列表
        self.changeCity(self.city)
        meituan.close()

    # 改变城市或页数
    def changeCity(self, city, page=1):
        try:
            self.city = city
            self.page = page
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
            }
            respon=requests.get(self.__getUrl(self.city,self.page), headers=headers)
            raw_hotels = respon.json()['data']['searchresult']
            hotels=[]
            for raw_hotel in raw_hotels:
                hotel={}
                hotel['name']=raw_hotel.get('name') #酒店名字
                hotel['id']=raw_hotel.get('poiid') #酒店id
                hotel['price']=raw_hotel.get('lowestPrice') #酒店价格
                hotel['score']=raw_hotel.get('avgScore') #酒店评分
                hotel['star']=raw_hotel.get('hotelStar') #酒店等级文字
                hotel['people_num']=raw_hotel.get('poiSaleAndSpanTag') #消费人数
                hotel['location']=raw_hotel.get('addr') #酒店地址
                hotel['tag']=raw_hotel.get('forward').get('serviceTagList') #酒店标签
                hotel['href']='https://hotel.meituan.com/'+str(hotel['id']) #酒店链接
                hotels.append(hotel)
            self.hotels=hotels
        except Exception as e:
            print(e)

    def changePage(self,page):
        self.changeCity(self.city,page)

    def __getUrl(self,city,page):
        t=time.time()
        date=time.strftime('%Y%m%d',time.localtime(t))

        #startDay=入住日期，endday=退房日期
        return 'https://ihotel.meituan.com/hbsearch/HotelSearch?utm_medium=pc' \
               '&version_name=999.9' \
               '&cateId=20' \
               '&attr_28=129' \
               '&uuid=A38CA98F1B71F4F7883E116E2C4431BB6F328E7CA4B2AEA76CD2677BF8892F73@'+str(t*1000)+'' \
               '&cityId='+self.__cities[city][0]+'' \
               '&offset='+str(page*20)+'' \
               '&limit=20' \
               '&startDay='+date+'' \
               '&endDay='+date+'' \
               '&q=' \
               '&sort=defaults' \
               '&X-FOR-WITH=dcCguOydblRtueRqqSe3mN2MKykJoRbWMwgfnWsgh0ji/S3Vx8IZHHtcWY5oNxBugMj3FssLS8c5LDJZfBpRF9iiQbeVTBzkzeuTJhUJ+fEDncPWsQsK5KUyPABbwIHi2/qPAjm+bCwmA2fDZ16Ctg=='


    def __str__(self):
        return str(self.hotels)


# 搜索途牛旅游网
def scrapy_tuniu(keyword):
    url = 'http://s.tuniu.com/search_complex/whole-shz-0-{}/'.format(keyword)
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
                   'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20'}
        response = requests.get(url=url, headers=headers).text


        url = re.compile('''<li>.*?<a.*?href="(.*?)".*?>.*?</li>''', re.S).findall(response)[:20]  # 链接
        imgurl = re.compile('''<li>.*?<img.*?data-src="(.*?)".*?>.*?</li>''', re.S).findall(response)[1:21]  # 图片链接

        title = re.compile('''<li>.*?<span.*?title="&lt;(.*?)">.*?</span>.*?</li>''', re.S).findall(response)[:20]  # 标题
        destination = re.compile('''<li>.*?<dd class="overview" title="(.*?)">.*?</dd>.*?</li>''', re.S).findall(response)[:20]  # 目的地

        price = re.compile('''<li>.*?<em>(.*?)</em>.*?</li>''', re.S).findall(response)[:20]  # 价格

        new_list = []
        mid = map(list, zip(price, destination, imgurl, title, url))
        for item in mid:
            new_dict = dict(zip(['price', 'destination', 'imgurl', 'title', 'url'], item))
            new_list.append(new_dict)
        return new_list
    except Exception as e:
        print(e)
        return None


