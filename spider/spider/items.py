# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
from scrapy_djangoitem import DjangoItem
from taobao.models import *


class ProductName(DjangoItem):
    django_model = ProductName


class JDProductsItem(DjangoItem):
    django_model = JDProductsItem


class JDCommentSummaryItem(DjangoItem):
    django_model = JDCommentSummaryItem


class JDHotCommentTagItem(DjangoItem):
    django_model = JDHotCommentTagItem


class JDCommentItem(DjangoItem):
    django_model = JDCommentItem


class JDAfterComment(DjangoItem):
    django_model = JDAfterComment


class TaobaoProduct(DjangoItem):
    django_model = TaobaoProduct


class TaobaoComment(DjangoItem):
    django_model = TaobaoComment


class TaobaoTag(DjangoItem):
    django_model = TaobaoTag
