# dataAnalyze
这个项目的index页面django+scrapy动态爬取京东淘宝,苏宁,淘宝,三家电商的相同商品的评论和标签信息, show2.html用了echarts.js调用rest frameworkde的接口饼图来展示
项目文件结构:
.
├── dataAnalyze
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── dbs
│   └── spider.db
├── db.sqlite3
├── eggs
│   └── spider
│       └── 1554265543.egg
├── img-storage
├── manage.py
├── media
├── README.md
├── snownlp_test.py
├── spider
│   ├── build
│   │   ├── bdist.linux-x86_64
│   │   └── lib
│   │       └── spider
│   │           ├── __init__.py
│   │           ├── items.py
│   │           ├── middlewares.py
│   │           ├── pipelines.py
│   │           ├── settings.py
│   │           └── spiders
│   │               ├── __init__.py
│   │               ├── scrapy_jingdong.py
│   │               └── taobao.py
│   ├── mysentiment.marshal.3
│   ├── neg.txt
│   ├── pos.txt
│   ├── project.egg-info
│   │   ├── dependency_links.txt
│   │   ├── entry_points.txt
│   │   ├── PKG-INFO
│   │   ├── SOURCES.txt
│   │   └── top_level.txt
│   ├── runScrapyJD.py(命令行启动scrapy脚本)
│   ├── scrapy.cfg
│   ├── scrapy_taobao.py(命令行启动scrapy脚本)
│   ├── setup.py
│   ├── snowtrain.py
│   ├── spider(scrapy框架)
│   │   ├── items.py
│   │   ├── middlewares.py
│   │   ├── pipelines.py
│   │   ├── settings.py
│   │   └── spiders
│   │       ├── scrapy_jingdong.py
│   │       └── taobao.py
│   └── twistd.pid
├── static(静态文件)
├── taobao
│   ├── admin.py
│   ├── apps.py
│   ├── filter.py
│   ├── __init__.py
│   ├── migrations(django数据库迁移)
│   ├── models.py
│   ├── run.py
│   ├── serializers_pagination.py
│   ├── serializers.py
│   ├── serializer_view_set.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates(前端文件)
├── test.py
├── twistd.pid
└── utils
    └── scrapy_web.py(爬取网站的主要文件)

59 directories, 266 files

效果图:
![Image text](https://github.com/XZHhengge/dataAnalyze/blob/master/img-storage/image0005.png)
其中爬取淘宝用了框架,因为在学校里爬取信息,不需要验证登录.
所以用了scrapy框架,并部署在scrapyd上.再用frp内网穿透.

index3 页面用requests爬取的马蜂窝的美食，美团的酒店，还有途牛的旅游
主页面
![Image text](https://github.com/XZHhengge/dataAnalyze/blob/master/img-storage/image0002.png)
商品搜索:
![Image text](https://github.com/XZHhengge/dataAnalyze/blob/master/img-storage/image0003.png)
旅游搜索:
![Image text](https://github.com/XZHhengge/dataAnalyze/blob/master/img-storage/image0004.png)

