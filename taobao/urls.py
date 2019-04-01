# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :19-3-18

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from taobao.views import index
from .views import search, show, JDHotCommentViewSet

router = DefaultRouter()
router.register('JDHotTag', JDHotCommentViewSet)


app_name = 'taobao'
urlpatterns = [
    # 用户信息
    # path('search/', search, name="search"),
    path('', index, name="index"),
    path('search', search, name='search'),
    path('show/<int:id>/', show, name="show"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
]