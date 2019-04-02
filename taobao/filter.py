# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :2019/4/1

from django_filters import rest_framework as filters
from .models import *


# 过滤器
class JDHotCommentTagFilter(filters.FilterSet):
    productid = filters.NumberFilter(field_name="productid", lookup_expr='gte')
    max_time = filters.NumberFilter(field_name="productid", lookup_expr='lte')

    class Meta:
        model = JDHotCommentTagItem
        fields = ['productid',]