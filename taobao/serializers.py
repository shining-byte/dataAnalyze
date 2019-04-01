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
        fields = "__all__"


class JDHotCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = JDHotCommentTagItem
        fields = "__all__"


class JDCommentItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = JDCommentItem
        fields = "__all__"


class JDAfterCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = JDAfterComment
        fields = "__all__"


class TaobaoProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaobaoProduct
        fields = "__all__"


class TaobaoCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaobaoComment
        fields = "__all__"


class TaobaoTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaobaoTag
        fields = "__all__"
