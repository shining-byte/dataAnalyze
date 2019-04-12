import re
from scrapy import Selector
import requests
from pypinyin import lazy_pinyin
from scrapy import Selector
pinyin = ''.join(lazy_pinyin('鸡肉'))
#
# url = 'http://shiwuxiangke.00cha.com/'
url2 = 'http://shiwuxiangke.00cha.com/{}.html'.format(pinyin)


'''<p>

<strong>(.*?)</strong><br>(.*?)(.*?)<br><br><strong>(.*?)</strong><br>(.*?)</p>'''
response = requests.get(url2)
response.encoding = 'gb2312'
# selector = Selector(response)
# info2 = selector.xpath('/html/body/div/div[4]/div[1]/div[1]/p[5]/text()').extract()
# print(info2)
info = re.compile('<div class="zynr">.*?<h1.*?">(.*?)</h1>.*?<img.*?src="(.*?)".*?>.*?</div>', re.S).findall(response.text)

# info = re.compile('<p>(.*?)</p>', re.S).findall(response.text)
print(info)
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
#            'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20'}
# data = {'shi': '鲍鱼'.encode('gb2312')}
# response = requests.post(url=url, data=data)
# response.encoding = 'gb2312'
# print(response.text)


