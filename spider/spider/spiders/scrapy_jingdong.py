# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :19-3-15
import re
import json
import scrapy
from scrapy.http import Request

from scrapy.selector import Selector

import requests
from spider.items import *
price_url = 'https://p.3.cn/prices/mgets?skuIds=J_'
favourable_url = 'https://cd.jd.com/promotion/v2?skuId=%s&area=1_72_2799_0&shopId=%s&venderId=%s&cat=%s'
# start_urls = ['https://item.jd.com/100002544828.html']

shop_id = 1
# aftercomment = 0
# from myFirstScrapy
comment_url = 'https://club.jd.com/comment/productPageComments.action?productId=%s&score=0&sortType=6&page=%s&pageSize=10'

class JDSpider(scrapy.Spider):
    # name = 'taobao'
    name = 'JD'
    allowed_domains = ['jd.com']
    # start_urls = ['https://rate.tmall.com/list_detail_rate.htm?itemId=580731960102&spuId=1089679943&sellerId=197232874&order=3&currentPage=1&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvppvEvbQvUvCkvvvvvjiPRLqWtjDUPszWzjivPmPpgj3Cn2sv1jYUPsLvzjtbiQhvCvvvpZptvpvhvvCvpvGCvvpvvPMMmphvLUvWqRQa0fJ6W3CQcExre8TJeVQEfwmK5iIffvDrz8TJhBH%2Bm7zZdiT1dcZI%2B87J%2Bu04jobZ1CQ4jBitL%2BoQRqJ6WeCpqU0QKfUpwymtvpvIvvCv7QvvvvvvvhNjvvmvxQvvBGwvvvUwvvCj1QvvvIgvvhNjvvvmFuyCvv9vvhhI1oREHIyCvvOCvhEvzW9CvpvVvvBvpvvv3QhvCvmvphv%3D&needFold=0&_ksTS=1552392132598_529&callback=jsonp530']
    # start_urls = ['https://search.jd.com/Search?keyword=%E5%B0%8F%E7%B1%B38&enc=utf-8&wq=%E5%B0%8F%E7%B1%B38&pvid=72f362cdd9774eefa743f71f843034e3']
    start_urls = 0
    # start_urls = ['https://www.xicidaili.com/']
    def parse(self, response):
        selector = Selector(response)
        # 获取商品的图片链接，价钱，介绍

        # print(selector.xpath('//*[@id="J_goodsList"]/ul').extract()[0])
        print(selector.xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[1]/a/img').extract()[0])
        print(selector.xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[1]/a').extract()[0])
        print(selector.xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[3]/strong/i/text()').extract()[0])
        print(selector.xpath('//*[@id="J_goodsList"]/ul').extract()[0])
        print(selector.xpath('//*[@id="J_goodsList"]/ul').extract()[0])
        # yield Request(url='', callback=self.parse_comments)



        # yield productsItem
        # for i in['1','2','3', '5']:
            # yield Request(url=comment_url % (product_id, '0'), callback=self.parse_comments, meta=data)

        # parse_product 传入是product的id
    def parse_product(self, response):
        # meta = dict()
        categorylink = response.xpath('//*[@id="crumb-wrap"]/div/div[1]/div[5]/a').extract()[0]
        re_categoy = re.compile('<a href=".*?cat=(.*?)".*?>(.*?)</a>').findall(categorylink)
        categoryname = re_categoy[0][1]
        """商品页获取title,price,product_id"""
        # category = response.xpath('//*[@id="crumb-wrap"]/div/div[1]/div[5]/a/text()').extract()[0]
        # categorylevel = response.meta['category']
        # category = 1
        ids = re.findall(r"venderId:(.*?),\s.*?shopId:'(.*?)'", response.text)
        if not ids:
            ids = re.findall(r"venderId:(.*?),\s.*?shopId:(.*?),", response.text)
        vender_id = ids[0][0]
        global shop_id
        shop_id = ids[0][1]

        # shop
        shopItem = ShopItem()
        shopItem['shopId'] = shop_id
        shopItem['venderId'] = vender_id
        shopItem['url1'] = 'http://mall.jd.com/index-%s.html' % (shop_id)
        try:
            shopItem['url2'] = 'https:' + response.xpath('//ul[@class="parameter2 p-parameter-list"]/li/a/@href').extract()[0]
        except:
            shopItem['url2'] = shopItem['url1']

        name = ''
        if shop_id == '0':
            name = '京东自营'
        else:
            try:
                name = response.xpath('//ul[@class="parameter2 p-parameter-list"]/li/a//text()').extract()[0]
            except:
                try:
                    name = response.xpath('//div[@class="name"]/a//text()').extract()[0].strip()
                except:
                    try:
                        name = response.xpath('//div[@class="shopName"]/strong/span/a//text()').extract()[0].strip()
                    except:
                        try:
                            name = response.xpath('//div[@class="seller-infor"]/a//text()').extract()[0].strip()
                        except:
                            name = u'京东自营'
        shopItem['name'] = name
        shopItem['_id'] = name
        yield shopItem
        # 产品
        productsItem = ProductsItem()
        productsItem['shopId'] = shop_id
        productsItem['category'] = categoryname
        try:
            title = response.xpath('//div[@class="sku-name"]/text()').extract()[0].replace(u"\xa0", "").strip()
        except Exception as e:
            title = response.xpath('//div[@id="name"]/h1/text()').extract()[0]
        productsItem['name'] = title
        product_id = response.url.split('/')[-1][:-5]
        productsItem['_id'] = product_id
        productsItem['url'] = response.url

        # description
        desc = response.xpath('//ul[@class="parameter2 p-parameter-list"]//text()').extract()
        productsItem['description'] = ';'.join(i.strip() for i in desc)

        # price
        response = requests.get(url=price_url + product_id)
        price_json = response.json()
        productsItem['reallyPrice'] = price_json[0]['p']
        productsItem['originalPrice'] = price_json[0]['m']

        # 优惠
        res_url = favourable_url % (product_id, shop_id, vender_id, re_categoy[0][0].replace(',', '%2c'))
        # category = quote(category)
        # res_url = favourable_url % (product_id, shop_id, vender_id, category)
        # print(res_url)
        response = requests.get(res_url)
        fav_data = response.json()
        if fav_data['skuCoupon']:
            desc1 = []
            for item in fav_data['skuCoupon']:
                start_time = item['beginTime']
                end_time = item['endTime']
                time_dec = item['timeDesc']
                fav_price = item['quota']
                fav_count = item['discount']
                fav_time = item['addDays']
                desc1.append(u'有效期%s至%s,满%s减%s' % (start_time, end_time, fav_price, fav_count))
            productsItem['favourableDesc1'] = ';'.join(desc1)
        # 若商品没有活动
        else:
        # if (productsItem['favourableDesc1']):
            productsItem['favourableDesc1'] = '无活动'

        # if fav_data['prom'] and fav_data['prom']['pickOneTag']:
        #     desc2 = []
        #     for item in fav_data['prom']['pickOneTag']:
        #         desc2.append(item['content'])
        #     productsItem['favourableDesc1'] = ';'.join(desc2)

        data = dict()
        data['product_id'] = product_id
        yield productsItem
        for i in['1','2','3', '5']:
            yield Request(url=comment_url % (product_id, '0'), callback=self.parse_comments, meta=data)

    def parse_comments(self, response):
        """获取首页商品comment"""
        try:
            data = json.loads(response.text)

        except Exception as e:
            print('get comment failed:', e)
            return None

        product_id = response.meta['product_id']
        # 评论总情况
        commentSummaryItem = CommentSummaryItem()
        commentSummary = data.get('productCommentSummary')
        commentSummaryItem['_id'] = commentSummary.get('productId')

        commentSummaryItem['afterCount'] = commentSummary.get('afterCount')

        # commentSummaryItem['goodRateShow'] = commentSummary.get('goodRateShow')
        # commentSummaryItem['poorRateShow'] = commentSummary.get('poorRateShow')
        commentSummaryItem['averageScore'] = commentSummary.get('averageScore')
        commentSummaryItem['commentCount'] = commentSummary.get('commentCount')
        commentSummaryItem['generalCount'] = commentSummary.get('generalCount')
        commentSummaryItem['generalRate'] = commentSummary.get('generalRate')
        commentSummaryItem['goodCount'] = commentSummary.get('goodCount')
        commentSummaryItem['goodRate'] = commentSummary.get('goodRate')

        commentSummaryItem['imageListCount'] = data.get('imageListCount')
        commentSummaryItem['poorCount'] = commentSummary.get('poorCount')
        commentSummaryItem['poorRate'] = commentSummary.get('poorRate')

        commentSummaryItem['showCount'] = commentSummary.get('showCount')
        # commentSummaryItem['skuId'] = commentSummary.get('skuId')
        # commentSummaryItem['goodRateStyle'] = commentSummary.get('goodRateStyle')
        # commentSummaryItem['skuIds'] = commentSummary.get('skuIds')
        # commentSummaryItem['poorRateStyle'] = commentSummary.get('poorRateStyle')
        # commentSummaryItem['generalRateStyle'] = commentSummary.get('generalRateStyle')
        # commentSummaryItem['productId'] = commentSummary.get('productId')  # 同ProductsItem的id相同
        # commentSummaryItem['generalRateShow'] = commentSummary.get('generalRateShow')
        # commentSummaryItem['jwotestProduct'] = data.get('jwotestProduct')
        # commentSummaryItem['maxPage'] = data.get('maxPage')
        commentSummaryItem['score'] = data.get('score')
        commentSummaryItem['soType'] = data.get('soType')
        commentSummaryItem['defaultGoodCount'] = commentSummary.get('defaultGoodCount')
        yield commentSummaryItem
            # 商品特性
        for hotComment in data['hotCommentTagStatistics']:
            hotCommentTagItem = HotCommentTagItem()
            hotCommentTagItem['_id'] = hotComment.get('id')
            hotCommentTagItem['count'] = hotComment.get('count')

            hotCommentTagItem['name'] = hotComment.get('name')
            # hotCommentTagItem['status'] = hotComment.get('status')
            # hotCommentTagItem['rid'] = hotComment.get('rid')
            # hotCommentTagItem['productId'] = hotComment.get('productId')
            hotCommentTagItem['productId'] = product_id
            # hotCommentTagItem['created'] = hotComment.get('created')
            # hotCommentTagItem['modified'] = hotComment.get('modified')
            hotCommentTagItem['type'] = hotComment.get('type')
            # hotCommentTagItem['canBeFiltered'] = hotComment.get('canBeFiltered')
            yield hotCommentTagItem

        for comment_item in data['comments']:
            # if (comment_item.get('content')[:7] in '此用户未及时填写评价内容，系统默认评价！'):
            #     pass
            if(len(comment_item.get('content'))<=6):
                pass
            else:
                comment = CommentItem()
                comment['shop_id'] = shop_id
                # global comment_item
                comment['_id'] = comment_item.get('id')
                comment['content'] = comment_item.get('content')
                comment['creationTime'] = comment_item.get('creationTime')
                comment['days'] = comment_item.get('days')
                comment['firstCategory'] = comment_item.get('firstCategory')
                comment['imageCount'] = comment_item.get('imageCount')
                comment['nickname'] = comment_item.get('nickname')
                comment['productColor'] = comment_item.get('productColor')
                comment['productId'] = product_id
                comment['productSize'] = comment_item.get('productSize')
                comment['referenceId'] = comment_item.get('referenceId')
                comment['referenceName'] = comment_item.get('referenceName')
                comment['score'] = comment_item.get('score')
                comment['secondCategory'] = comment_item.get('secondCategory')
                comment['thirdCategory'] = comment_item.get('thirdCategory')
                comment['userLevelId'] = comment_item.get('userLevelId')
                comment['userLevelName'] = comment_item.get('userLevelName')

                yield comment


        # next page
        max_page = int(data.get('maxPage', '1'))
        if max_page > 60:
            max_page = 60
        for j in [1, 2, 3, 5]:
            for i in range(1, max_page):
                if j == 5:
                    url = 'https://club.jd.com/comment/productPageComments.action?productId=%s&score=%s&sortType=6&page=%s&pageSize=10' % (
                    product_id, j, str(i))
                    text = requests.get(url).json()
                    # text1 = re.compile(r'[(](.*?)[)];', re.S).findall(text.text)
                    # jsontext = text['comments'][0]['afterUserComment']
                    # global aftercomment
                    aftercomment = AfterCommentItem()
                    # for comment_item in data['comments']:
                    for after in text['comments']:

                        if (after['afterUserComment']['hAfterUserComment']['content'][:7] in
                                '此用户未及时填写评价内容，系统默认评价！'):
                            pass
                        elif(len(after['afterUserComment']['hAfterUserComment']['content'])<=6):
                            pass
                        else:
                            aftercomment['commentid'] = after['id']
                            aftercomment['product_id'] = after['afterUserComment']['productId']
                            aftercomment['content'] = after['afterUserComment']['hAfterUserComment']['content']
                            yield aftercomment
                url ='https://club.jd.com/comment/productPageComments.action?productId=%s&score=%s&sortType=6&page=%s&pageSize=10' % (product_id, j, str(i))
                meta = dict()
                meta['product_id'] = product_id
                yield Request(url=url, callback=self.parse_comments2, meta=meta)

    # 进行翻页评论
    def parse_comments2(self, response):
        """获取商品comment"""
        try:
            data = json.loads(response.text)
        except Exception as e:
            print('get comment failed:', e)
            return None

        product_id = response.meta['product_id']

        for comment_item in data['comments']:
            if (comment_item.get('content')[:7] in '此用户未及时填写评价内容，系统默认评价！'):
                pass
            elif (len(comment_item.get('content')) <= 6):
                pass
            else:
                comment = CommentItem()

                comment['shop_id'] = shop_id
                comment['_id'] = comment_item.get('id')
                comment['content'] = comment_item.get('content')
                comment['creationTime'] = comment_item.get('creationTime')
                comment['days'] = comment_item.get('days')
                comment['firstCategory'] = comment_item.get('firstCategory')
                comment['imageCount'] = comment_item.get('imageCount')
                comment['nickname'] = comment_item.get('nickname')
                comment['productColor'] = comment_item.get('productColor')
                comment['productId'] = product_id
                comment['productSize'] = comment_item.get('productSize')
                comment['referenceId'] = comment_item.get('referenceId')
                comment['referenceName'] = comment_item.get('referenceName')
                comment['score'] = comment_item.get('score')
                comment['secondCategory'] = comment_item.get('secondCategory')
                comment['thirdCategory'] = comment_item.get('thirdCategory')
                comment['userLevelId'] = comment_item.get('userLevelId')
                comment['userLevelName'] = comment_item.get('userLevelName')
                # if (comment_item[0]['afterUserComment']):
                #     aftercomment = AfterComment()
                #     aftercomment['commentid'] = comment['_id'] = comment_item.get('id')

                yield comment



