# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :19-3-18

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from taobao.views import index
from .views import search
from taobao.serializer_view_set import *

router = DefaultRouter()
router.register('JDHotTag', JDHotTagViewSet)
router.register('JDProduct', JDProductsViewSet)
router.register('JDComment', JDCommentViewSet)
router.register('JDCommntSum', JDCommentSummaryViewSet)
router.register('TaobaoProduct', TaobaoProductViewSet)
router.register('TaobaoComment', TaobaoCommentViewSet)
router.register('TaobaoTag', TaobaoTagViewSet)
router.register('SuNingTag', SuNingTagViewSet)
router.register('SuNingComment', SuNingCommentViewSet)


app_name = 'taobao'
urlpatterns = [
    # 用户信息
    # path('search/', search, name="search"),
    path('', index, name="index"),
    path('search', search, name='search'),
    # path('show/<int:id>/', show, name="show"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
]