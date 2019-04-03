# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :19-3-19
import re
import requests
from scrapy import Selector
keyword = '小米9'
url = 'https://search.suning.com/{}/'.format(keyword)

response = requests.get(url=url)
selector = Selector(response)
# li = selector.xpath('//*[@id="product-list"]/ul').extract()[0]
# print(li)
print(response.text)
# li = re.compile('<li doctype="1".*?class=item-wrap.*?>(.*?)</li>').findall(response.content)
# print(li)