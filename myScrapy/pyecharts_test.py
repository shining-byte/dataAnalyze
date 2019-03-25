# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :19-3-14
from pyecharts import Pie

dict1 = {'goodRateShow': 98, 'poorRateShow': 1, 'poorCountStr': '8100+', 'averageScore': 5, 'generalCountStr': '7000+', 'oneYear': 0, 'showCount': 71000, 'showCountStr': '7.1万+', 'goodCount': 1190000, 'generalRate': 0.005, 'generalCount': 7000, 'skuId': 100000400010, 'goodCountStr': '119万+', 'poorRate': 0.015, 'sensitiveBook': 0, 'afterCount': 10000, 'goodRateStyle': 147, 'poorCount': 8100, 'skuIds': None, 'videoCount': 6000, 'poorRateStyle': 2, 'generalRateStyle': 1, 'commentCountStr': '121万+', 'commentCount': 1210000, 'productId': 100000400010, 'videoCountStr': '6000+', 'afterCountStr': '1万+', 'defaultGoodCount': 820000, 'goodRate': 0.98, 'generalRateShow': 1, 'defaultGoodCountStr': '82万+'}

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
pie = Pie("饼图示例")
pie.add("", attr, v1, is_label_show=True)
pie.show_config()
pie.render()
