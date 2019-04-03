# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :19-3-19
import re
import requests
url = '''https://search.suning.com/{}/'''.format('小米9')

r = requests.get(url=url).text

'''<span class="def-price" datasku="10887042490|||||0000000000">
<i>¥</i>2999<i>.00</i></span>'''

# text = re.compile('''<span class="def-price" datasku=".*?"><i>¥</i>(.*?)<i>.00</i></span>''', re.S).findall(r)
# print(text)
print(r)