# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :19-3-19
str = '''//item.jd.com/100000400010.html'''

import re
imageUrl = re.compile('com/(.*?).html', re.S).findall(str)
imageUrl2 = re.compile('\d').findall(str)
print(imageUrl2)
print(imageUrl)