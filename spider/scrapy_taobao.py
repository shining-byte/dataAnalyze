# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :19-3-25
from scrapy import cmdline
import os
import sys
import django
from django.core.wsgi import get_wsgi_application
sys.path.append(os.path.dirname(os.path.abspath('.')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'dataAnalyze.settings'
application = get_wsgi_application()
django.setup()
cmdline.execute("scrapy crawl taobao -a keyword=魅族note6".split())