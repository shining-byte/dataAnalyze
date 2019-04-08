import re
from scrapy import Selector
import requests

url = 'http://s.tuniu.com/search_complex/whole-shz-0-{}/'.format('北京')

response = requests.get(url=url).text

# print(response.text)
# text = selector.xpath('//*[@id="niuren_list"]/div[2]/div[2]/div[1]/div[2]').extract()
# print(text)
url = re.compile('''<li>.*?<a.*?href="(.*?)".*?>.*?</li>''', re.S).findall(response)[:20] # 链接
imgurl = re.compile('''<li>.*?<img.*?data-src="(.*?)".*?>.*?</li>''', re.S).findall(response)[:20] # 图片链接
# print(len(imgurl))
# print(url)
# print(len(imgurl))
title = re.compile('''<li>.*?<span.*?title="&lt;(.*?)">.*?</span>.*?</li>''', re.S).findall(response)[:20] # 标题
de2 = re.compile('''<li>.*?<dd class="overview" title="(.*?)">.*?</dd>.*?</li>''', re.S).findall(response)[:20] # 标题
price = re.compile('''<li>.*?<em>(.*?)</em>.*?</li>''', re.S).findall(response)[:20] # 标题
# print(title)
# imgurl = selector.xpath('//*[@id="niuren_list"]/div[2]/div[2]/div[1]/div[3]/ul/li[1]/div/a/dl/dt/p[3]').extract()
# de = selector.xpath('//*[@id="niuren_list"]/div[2]/div[2]/div[1]/div[3]/ul/li/div/a/dl/dd[1]').extract()[0]
# print(de)
#
# price = selector.xpath('//*[@id="niuren_list"]/div[2]/div[2]/div[1]/div[2]/ul/li/div/a/div[2]/div[1]/em/text()').extract()[:20]
# print(info)
# print(de)

# print(len(text))
print(len(url))
print(len(imgurl))
print(len(title))
print(len(de2))
print(price)
# print(price)

