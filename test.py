# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :19-3-19
import re
import json

str = '''({"tags":{"rateSum":5196,"structuredRateStatisticList":[],"tagClouds":[{"posi":true,"count":1248,"weight":0,"id":"620","tag":"手机不错"},{"posi":true,"count":1070,"weight":0,"id":"121","tag":"外型不错"},{"posi":true,"count":961,"weight":0,"id":"921","tag":"性能强大"},{"posi":true,"count":543,"weight":0,"id":"721","tag":"操作顺畅"},{"posi":true,"count":385,"weight":0,"id":"420","tag":"快递不错"},{"posi":true,"count":292,"weight":0,"id":"40221","tag":"拍照好清晰"},{"posi":false,"count":248,"weight":0,"id":"921","tag":"性能一般"},{"posi":false,"count":243,"weight":0,"id":"421","tag":"屏稍小"},{"posi":true,"count":167,"weight":0,"id":"520","tag":"划算"},{"posi":true,"count":39,"weight":0,"id":"1020","tag":"机子是正品"}],"dimenSum":9,"innerTagCloudList":[],"userTagCloudList":[]}})'''

str = str.replace('(', '')
str = str.replace(')', '')
tag = json.loads(str)['tags']['tagClouds']
for i in tag:
    print(i['count'])
    print(i['tag'])

print([tag[i]['count'] for i in range(len(tag))])