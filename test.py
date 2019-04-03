# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :19-3-19
# import json
# import re
#
# import requests
#
# url = '''http://rate.tmall.com/list_detail_rate.htm?itemId={0}&sellerId=1652490016&currentPage=1'''.format(577150493893)
#
# text = requests.get(url).text
# text = text.replace('jsonp128(', '')
# text = text.replace(')', '')
# jsons = json.loads(text)
# comment = jsons['rateDetail']['rateList']
# print(comment[0])
# print(comment[1])
#
# # text = re.compile('"rateList":(.*?),"tags"').findall(text)[0]
# # print(text)
# # text = eval(text)
# # print(text)
# # print(json.loads(text), strict=False)

import requests

url = 'http://94.191.87.62:6800/schedule.json'
dictdata = {"project": 'default', "spider": 'taobao', 'keyword': '华为P30'}

r = requests.post(url=url, data=dictdata)

print(r.text)


