# dataAnalyze
这个项目的index页面django+scrapy动态爬取京东淘宝,苏宁,淘宝,三家电商的相同商品的评论和标签信息, show2.html用了echarts.js调用rest frameworkde的接口饼图来展示
效果图:
![Image text](https://github.com/XZHhengge/dataAnalyze/blob/master/img-storage/image0005.png)
其中爬取淘宝用了框架,因为在学校里爬取信息,不需要验证登录.
所以用了scrapy框架,并部署在scrapyd上.再用frp内网穿透.

index3 页面用requests爬取的马蜂窝的美食，美团的酒店，还有途牛的旅游
主页面


旅游搜索:
