# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :2019/4/1

from rest_framework import mixins, viewsets, filters
from django.db import connection
from django.db.utils import OperationalError

from taobao.filter import JDHotCommentTagFilter
from taobao.models import *
from taobao.serializers import *
from django_filters.rest_framework import DjangoFilterBackend

from taobao.serializers_pagination import *


class JDHotTagViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    queryset = JDHotCommentTagItem.objects.all()
    serializer_class = JDHotTagSerializer
    pagination_class = JDHotTagPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)

    filter_class = JDHotCommentTagFilter


class JDProductsViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    queryset = JDProductsItem.objects.all()
    serializer_class = JDProductsSerializer
    pagination_class = JDProductPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)

    # filter_class =


class JDCommentViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    queryset = JDCommentItem.objects.all()
    serializer_class = JDCommentItemSerializer
    pagination_class = JDCommentPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)

    # filter_class = JD


class JDCommentSummaryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    queryset = JDCommentSummaryItem.objects.all()
    serializer_class = JDCommentSummarySerializer
    pagination_class = JDCommentSumPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)

    # filter_class = JDHotCommentTagFilter


class TaobaoProductViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    queryset = TaobaoProduct.objects.all()
    serializer_class = TaobaoProductSerializer
    pagination_class = TaobaoProductPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)

    # filter_class = JDHotCommentTagFilter


class TaobaoCommentViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    queryset = TaobaoComment.objects.all()
    serializer_class = TaobaoCommentSerializer
    pagination_class = TaobaoCommentPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)

    # filter_class = JDHotCommentTagFilter


class TaobaoTagViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    queryset = TaobaoTag.objects.all()
    serializer_class = TaobaoTagSerializer
    pagination_class = TaobaoTagPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)

    # filter_class = JDHotCommentTagFilter
