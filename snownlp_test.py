# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :19-3-20
from snownlp import SnowNLP

s = SnowNLP('超级好')
print(s.sentences)
print(s.sentiments)