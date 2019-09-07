# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :19-3-20
from snownlp import SnowNLP

s = SnowNLP('目前在用 感觉不错 价格高了点')
print(s.keywords())
print(s.summary())
print(s.sentiments)
