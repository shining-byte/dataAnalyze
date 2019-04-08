import re
from scrapy import Selector
import requests

url = 'https://s.taobao.com/search?q=华为'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
           'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20'}
response = requests.get(url=url, headers=headers)
prices = re.findall('"view_price":"(.*?)",', response.text)[:5]  # 正则提示商品价格
nid = re.findall('"nid":"(.*?)"', response.text)[:5]
title = re.findall('"raw_title":"(.*?)"', response.text)[:5]
pic_url = re.findall('"pic_url":"(.*?)"', response.text)[:5]
detail_url = re.findall('"detail_url":"(.*?)"', response.text)[:5]
list = []
print(nid)
for i in nid:
    detail_url = ['https://detail.tmall.com/item.htm?spm=a230r.1.14.6.70de7ffcZej9q8&id={}&cm_id=140105335569ed55e27b&abbucket=20&sku_properties=10004:1617715035;5919063:6536025'.format(i)]
    list.append(detail_url)
print(list)