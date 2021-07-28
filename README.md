[B站演示视频](https://www.bilibili.com/video/BV1xE411u7Rm)
# dataAnalyze
项目文件结构:
```
├── dataAnalyze（django 主目录)
├── spider（scrapy主目录）
├── taobao( django 的一个app)
├── templates(django前端文件目录)
 ```
 
 ## 通过django的view去调用部署在scrapyd上的scrapy任务的spider爬虫
 
这个项目的index页面django+scrapy动态爬取京东淘宝,苏宁,淘宝,三家电商的相同商品的评论和标签信息, show2.html用了echarts.js调用rest frameworkde的接口饼图来展示
效果图:
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200503212605282.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQwOTY1MTc3,size_16,color_FFFFFF,t_70)
用scrapy框架,并部署在scrapyd上.django调用接口数据
api 接口格式如下,show2.html有通过ajax访问接口提取数据.
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200503212603163.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQwOTY1MTc3,size_16,color_FFFFFF,t_70)
index3 页面用requests爬取的马蜂窝的美食，美团的酒店，还有途牛的旅游
主页面
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200503212602861.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQwOTY1MTc3,size_16,color_FFFFFF,t_70)
商品搜索:
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200503212603424.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQwOTY1MTc3,size_16,color_FFFFFF,t_70)
旅游搜索:
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200503212607133.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQwOTY1MTc3,size_16,color_FFFFFF,t_70)
美食搜索:
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200503212607338.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQwOTY1MTc3,size_16,color_FFFFFF,t_70)

