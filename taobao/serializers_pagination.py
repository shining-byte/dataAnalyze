# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :2019/4/1
from rest_framework.pagination import PageNumberPagination


class JDProductPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'  # 可以设置url一页有多少个
    page_query_param = "p"  # 用于url传参数第几页
    max_page_size = 100


class JDHotTagPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'  # 可以设置url一页有多少个
    page_query_param = "p"  # 用于url传参数第几页
    max_page_size = 100


class JDCommentPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'  # 可以设置url一页有多少个
    page_query_param = "p"  # 用于url传参数第几页
    max_page_size = 100


class JDCommentSumPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'  # 可以设置url一页有多少个
    page_query_param = "p"  # 用于url传参数第几页
    max_page_size = 100


class JDAfterCommentPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'  # 可以设置url一页有多少个
    page_query_param = "p"  # 用于url传参数第几页
    max_page_size = 100


class TaobaoProductPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'  # 可以设置url一页有多少个
    page_query_param = "p"  # 用于url传参数第几页
    max_page_size = 100


class TaobaoCommentPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'  # 可以设置url一页有多少个
    page_query_param = "p"  # 用于url传参数第几页
    max_page_size = 100


class TaobaoTagPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'  # 可以设置url一页有多少个
    page_query_param = "p"  # 用于url传参数第几页
    max_page_size = 100


class SuNingTagPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'  # 可以设置url一页有多少个
    page_query_param = "p"  # 用于url传参数第几页
    max_page_size = 100


class SuNingCommentPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'  # 可以设置url一页有多少个
    page_query_param = "p"  # 用于url传参数第几页
    max_page_size = 100
