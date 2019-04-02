# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :2019/3/31

from rest_framework import serializers
from .models import *


class JDProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JDProductsItem
        fields = "__all__"


class JDCommentSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = JDCommentSummaryItem
        fields = ['commentCount', 'generalCount', 'goodCount', 'poorCount', 'score']


class JDHotTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = JDHotCommentTagItem
        fields = ['name', 'count']


class JDCommentItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = JDCommentItem
        fields = ['nickname', 'score', 'userLevelName']


class JDAfterCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = JDAfterComment
        fields = ['content', ]


class TaobaoProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaobaoProduct
        fields = ['productprice', 'producturl']


class TaobaoCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaobaoComment
        fields = ['displayUserNick', 'rateContent']


class TaobaoTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaobaoTag
        fields = ['tagname', 'tagcount']
