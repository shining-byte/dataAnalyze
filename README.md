# dataAnalyze
这个项目的index页面django+scrapy动态爬取京东淘宝,苏宁,淘宝,三家电商的相同商品的评论和标签信息, show2.html用了echarts.js调用rest frameworkde的接口饼图来展示
效果图:
![image0002](../../图片/截图/image0002.png)
其中爬取淘宝用了框架,因为在学校里爬取信息,不需要验证登录.
所以用了scrapy框架,并部署在scrapyd上.再用frp内网穿透.

index3 页面用requests爬取的马蜂窝的美食，美团的酒店，还有途牛的旅游
主页面
![image0002](image0002.png)

商品搜索:

![image0003](image0003.png)

酒店搜索:
![image0004](image0004.png)

旅游搜索:
