# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :19-3-21
from snownlp import sentiment

if __name__ == '__main__':
    sentiment.train('neg.txt', 'pos.txt')
    sentiment.save('mysentiment.marshal')