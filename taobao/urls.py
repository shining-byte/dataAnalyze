# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :19-3-18

from django.urls import path

from .views import search, show

app_name = 'taobao'
urlpatterns = [
    # 用户信息
    # path('search/', search, name="search"),
    path('show/<int:id>/', show, name="search"),
    # path('pdf/', SomeView.as_view(), name="user_pdf"),
    # path('update/pwd/', UpdatePwdView.as_view(), name="update_pwd"),
    # path('bespeak', BespeakView.as_view(), name="user_bespeak"),
    # path('word/',Word.as_view(),name="word"),
    # path('getSeat/', Seats.as_view(), name='getSeat'),
    # path(r'choice/', ChoiceTime.as_view(), name= 'choicetime'),
    # path('send_verification_code/', views.send_verification_code, name='send_verification_code'),
    # path('forgetpassword/', views.forgetpassword, name='fogetpassword'),
    # path('update_email/', UpdateEmailView.as_view(), name="update_email"),
    # path('sendemail_code/', SendEmailCodeView.as_view(), name="sendemail_code"),
    #注册链接
    # path('')

]