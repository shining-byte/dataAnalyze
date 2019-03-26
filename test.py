# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :19-3-19
list = ['//item.jd.com/100000400010.html', '//item.jd.com/8656283.html', '//item.jd.com/100000503295.html', '//item.jd.com/8051104.html', '//item.jd.com/7652013.html', '//item.jd.com/100003895136.html', '//item.jd.com/8264403.html', '//item.jd.com/7120000.html', '//item.jd.com/7437710.html', '//item.jd.com/7437564.html', '//item.jd.com/6735790.html', '//item.jd.com/28445462537.html', '//item.jd.com/100003438274.html', '//item.jd.com/8457421.html', '//item.jd.com/33277169973.html', '//item.jd.com/33278877170.html', '//item.jd.com/28917601601.html', '//item.jd.com/30911025510.html', '//item.jd.com/20903273963.html', '//item.jd.com/28779745128.html', '//item.jd.com/33276636524.html', '//item.jd.com/41578142821.html', '//item.jd.com/41563312675.html', '//item.jd.com/28756072327.html', '//item.jd.com/40922103042.html', '//item.jd.com/41566114375.html', '//item.jd.com/29038940952.html', '//item.jd.com/33955078555.html', '//item.jd.com/41306818658.html', '//item.jd.com/28858935461.html']
import re

id = []


# imageUrl = re.compile('com/(.*?).html', re.S).findall(str)
# imageUrl2 = re.compile('\d').findall(str)
# print(imageUrl2)
# print(imageUrl)
list2 = ['https:'+i for i in list]
print(list2)