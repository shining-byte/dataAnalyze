from django.db import models

# Create your models here.

# class ShopItem(models.Model):
#     _id = models.CharField('id', max_length=100, blank=True)
#     name = models.CharField('店铺名称', max_length=100, blank=True)  #
#     shopId = models.CharField('shop id',max_length=50 ,primary_key=True)  #
#     url1 = models.CharField('店铺url1', max_length=100, blank=True)  #
#     url2 = models.CharField('店铺url2', max_length=100, blank=True)  #
#     venderId = models.IntegerField('vender id', blank=True )  #
#
#     class Meta:
#         db_table = 'shop'
#         verbose_name = '商店信息'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name



    
class ProductsItem(models.Model):
    productid =models.CharField('产品id', primary_key=True, max_length=100)  #
    category =models.CharField('产品分类名', max_length=50, blank=True)  #
    description =models.TextField('产品描述', blank=True)  #
    name =models.CharField('产品名称',max_length=100, blank=True)  #
    # originalPrice =models.FloatField('原价', blank=True)  #
    imgurl = models.CharField('封面地址', max_length=300)
    reallyPrice =models.FloatField('当前价格', blank=True)  #
    # shopId =models.ForeignKey(ShopItem, on_delete=models.CASCADE)  #
    url = models.URLField('商品地址', blank=True)
    # favourableDesc1 =models.CharField('优惠描述1', max_length=300, blank=True)  #

    class Meta:
        db_table = 'product'
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CommentSummaryItem(models.Model):
    productid = models.ForeignKey(ProductsItem, on_delete=models.CASCADE)
    afterCount = models.IntegerField('追加评论', blank=True)
    averageScore = models.IntegerField('平均评分', blank=True)
    commentCount = models.IntegerField('评分总人数', blank=True)
    defaultGoodCount = models.IntegerField('默认好评', blank=True)

    generalCount = models.IntegerField('中评总人数', blank=True)
    generalRate = models.FloatField('中评比率', blank=True)
    goodCount = models.IntegerField('好评人数', blank=True)
    goodRate = models.FloatField('好评比率', max_length=100, blank=True)
    imageListCount = models.IntegerField('晒图评论人数', blank=True)
    poorCount = models.IntegerField('差评人数', blank=True)
    poorRate = models.FloatField('差评比率', max_length=100, blank=True)

    # goodRateShow = models.CharField('待定', max_length=100)
    # poorRateShow = models.CharField('待定', max_length=100)
    score = models.IntegerField('评论等级', blank=True)
    # showCount = models.IntegerField('待定', blank=True)

    # soType = models.IntegerField('待定', blank=True)


    class Meta:
        db_table = 'commentsummary'
        verbose_name = '评论总详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id
    
class HotCommentTagItem(models.Model):
    _id = models.CharField('id', max_length=100, blank=True)
    name = models.CharField('名字', max_length=100, blank=True)
    productId = models.ForeignKey(ProductsItem, on_delete=models.CASCADE, blank=True)
    count = models.CharField('数量', max_length=100, blank=True)
    type = models.CharField('类型', max_length=100, blank=True)


    class Meta:
        db_table = 'hotcomment'
        verbose_name = '热评'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id

class CommentItem(models.Model):
    userid =models.CharField('评论用户id', max_length=100, blank=True)
    content =models.TextField('评论内容', blank=True)
    creationTime = models.CharField('评论时间', max_length=100, blank=True)
    days =models.IntegerField('已评论参数', blank=True)
    firstCategory =models.IntegerField('第一级分类', blank=True)
    imageCount =models.SmallIntegerField('评论图片数量', blank=True, null=True)
    nickname =models.CharField('用户名', max_length=100, blank=True)
    productColor =models.CharField('产品颜色', max_length=100, blank=True)
    productId =models.ForeignKey(ProductsItem, on_delete=models.CASCADE)  #同ProductsItem的id相同
    productSize =models.CharField('产品型号', max_length=100, blank=True)
    referenceId =models.CharField('产品总id', blank=True, max_length=100)
    referenceName =models.CharField('产品描述', max_length=100, blank=True)
    score =models.IntegerField('评分', blank=True)
    secondCategory =models.IntegerField('第二级分类', blank=True)
    # shop_id = models.ForeignKey(ShopItem, on_delete=models.CASCADE)
    thirdCategory =models.IntegerField('第三级分类', blank=True)
    userLevelId =models.CharField('用户等级id', max_length=100, blank=True)
    userLevelName =models.CharField('用户等级名称', max_length=100, blank=True)


    class Meta:
        db_table = 'comment'
        verbose_name = '评论详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id
        
class AfterComment(models.Model):

    productid = models.ForeignKey(ProductsItem, on_delete=models.CASCADE)
    commentid = models.CharField('评论人ID', max_length=100)
    content = models.TextField('追评内容')

    class Meta:
        db_table = 'aftercomment'
        verbose_name = '追评'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.productid
    


# class ProductLink(models.Model):
#     id = models.CharField('产品id' ,primary_key=True, max_length=50)
#     imgurl = models.TextField('产品封面')
#
#     class Meta:
#         db_table = 'productlink'
#         verbose_name = '产品链接'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.id

