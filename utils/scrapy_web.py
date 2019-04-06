# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :19-3-30
import json

import re


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
                                         levelName=j['userInfo']['levelName']).save()







# 保存京东标签
def saveJDhotTag(*args):
    JDHotCommentTagItem.objects.create(name=args[0], count=args[1], productid=args[2]).save()


# 保存京东评论信息
def saveJDcomment(*args):

    jdcomment = JDCommentItem.objects.create(content=args[0], nickname=args[1], referenceId=args[2],
                                             score=args[3], userLevelName=args[4], productid=args[5])
    jdcomment.save()



