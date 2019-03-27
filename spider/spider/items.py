# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

#
# class CategoriesItem(Item):
#     name = Field()  #分类名称
#     url = Field()  #分类url
#     _id = Field()  #分类id
#     index = Field()  #分类的index


class ProductsItem(Item):
    productid = Field()  #产品id
    category = Field()  # 产品分类
    description = Field()  #产品描述
    name = Field()  #产品名称
    imgurl = Field()  #产品url
    reallyPrice = Field()  # 产品价格
    url = Field()
    # favourableDesc1 = Field()  #优惠描述1


# class ShopItem(Item):
#     _id = Field()  #店铺名称
#     name = Field()  #店铺名称
#     url1 = Field()  #店铺url1
#     url2 = Field()  #店铺url2
#     shopId = Field()  #shop id
#     venderId = Field()  #vender id


class CommentItem(Item):
    userid = Field()
    productId = Field()  #同ProductsItem的id相同
    content = Field()
    creationTime = Field()
    firstCategory = Field()
    secondCategory = Field()
    thirdCategory = Field()
    score = Field()
    userLevelId = Field()
    nickname = Field()
    productColor = Field()
    productSize = Field()
    imageCount = Field()
    userLevelName = Field()
    referenceId = Field()
    days = Field()
    referenceName = Field()




class CommentSummaryItem(Item):
    productid_id = Field()
    averageScore = Field()
    goodCount = Field()
    generalRate = Field()
    generalCount = Field()
    poorRate = Field()
    afterCount = Field()
    poorCount = Field()
    commentCount = Field()
    productId = Field()  #同ProductsItem的id相同
    goodRate = Field()
    score = Field()
    imageListCount = Field()
    defaultGoodCount = Field()


class HotCommentTagItem(Item):
    _id = Field()
    name = Field()
    productId = Field()
    count = Field()
    type = Field()

class AfterCommentItem(Item):
    commentid = Field()
    product_id = Field()
    content = Field()

