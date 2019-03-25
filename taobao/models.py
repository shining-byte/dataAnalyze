from django.db import models

# Create your models here.

class ShopItem(models.Model):
    _id = models.CharField('id', max_length=100, blank=True)
    name = models.CharField('店铺名称', max_length=100, blank=True)  #
    shopId = models.CharField('shop id',max_length=50 ,primary_key=True)  #
    url1 = models.CharField('店铺url1', max_length=100, blank=True)  #
    url2 = models.CharField('店铺url2', max_length=100, blank=True)  #
    venderId = models.IntegerField('vender id', blank=True )  #

    class Meta:
        db_table = 'shop'
        verbose_name = '商店信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



    
class ProductsItem(models.Model):
    _id =models.CharField('产品id', primary_key=True, max_length=100)  #
    category =models.CharField('产品分类名', max_length=50, blank=True)  #
    description =models.TextField('产品描述', blank=True)  #
    name =models.CharField('产品名称',max_length=100, blank=True)  #
    originalPrice =models.FloatField('原价', blank=True)  #

    reallyPrice =models.FloatField('当前价格', blank=True)  #
    shopId =models.ForeignKey(ShopItem, on_delete=models.CASCADE)  #
    url = models.URLField('商品地址', blank=True)
    # venderId =models.CharField('vender id', max_length=100)  #
    # commentCount =models.CharField('评价总数', max_length=100)  #
    # goodComment =models.CharField('好评数', max_length=100)  #
    # generalComment =models.CharField('中评数', max_length=100)  #
    # poolComment =models.CharField('差评数', max_length=100)  #
    favourableDesc1 =models.CharField('优惠描述1', max_length=300, blank=True)  #
    # favourableDesc2 =models.CharField('优惠描述2', max_length=100)  #

    class Meta:
        db_table = 'product'
        verbose_name = '评论简述'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class CommentSummaryItem(models.Model):
    _id = models.ForeignKey(ProductsItem, on_delete=models.CASCADE)
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
    score = models.IntegerField('星级', blank=True)
    showCount = models.IntegerField('待定', blank=True)

    soType = models.IntegerField('待定', blank=True)
    # skuId = models.CharField('待定', max_length=100)
    # goodRateStyle = models.CharField('待定', max_length=100)
    # skuIds = models.CharField('待定', max_length=100)
    # poorRateStyle = models.CharField('待定', max_length=100)
    # generalRateStyle = models.CharField('待定', max_length=100)
    # productId = models.CharField('待定', max_length=100)  #同ProductsItem的id相同
    # generalRateShow = models.CharField('待定', max_length=100)
    # jwotestProduct = models.CharField('待定', max_length=100)
    # maxPage = models.CharField('待定', max_length=100)


    class Meta:
        db_table = 'commentsummary'
        verbose_name = '评论总详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self._id
    
class HotCommentTagItem(models.Model):
    _id = models.CharField('id', max_length=100, blank=True)
    name = models.CharField('名字', max_length=100, blank=True)
    # status = models.CharField('待定', max_length=100)
    # rid = models.CharField('待定', max_length=100)
    productId = models.ForeignKey(ProductsItem, on_delete=models.CASCADE, blank=True)
    count = models.CharField('数量', max_length=100, blank=True)
    # created = models.CharField('待定', max_length=100)
    # modified = models.CharField('待定', max_length=100)
    type = models.CharField('类型', max_length=100, blank=True)
    # canBeFiltered = models.CharField('待定', max_length=100)


    class Meta:
        db_table = 'hotcomment'
        verbose_name = '热评'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self._id

class CommentItem(models.Model):
    _id =models.CharField('评论用户id', max_length=100, blank=True)
    # afterDays =models.IntegerField('待定')
    # anonymousFlag =models.CharField('待定', max_length=100)
    content =models.TextField('评论内容', blank=True)
    creationTime = models.CharField('评论时间', max_length=100, blank=True)
    days =models.IntegerField('已评论参数', blank=True)
    # discussionId =models.IntegerField('待定')
    firstCategory =models.IntegerField('第一级分类', blank=True)
    # guid =models.CharField('待定', max_length=100)
    imageCount =models.SmallIntegerField('评论图片数量', blank=True, null=True)
    # integral =models.IntegerField('待定')
    # isMobile =models.CharField('待定', max_length=100)
    # isReplyGrade =models.CharField('待定', max_length=100)
    # isTop =models.CharField('待定', max_length=100)
    # mergeOrderStatus =models.CharField('待定', max_length=100)
    nickname =models.CharField('用户名', max_length=100, blank=True)
    # orderId =models.CharField('订单号', max_length=100)
    # plusAvailable =models.CharField('待定', max_length=100)
    productColor =models.CharField('产品颜色', max_length=100, blank=True)
    productId =models.ForeignKey(ProductsItem, on_delete=models.CASCADE)  #同ProductsItem的id相同
    productSize =models.CharField('产品型号', max_length=100, blank=True)
    # recommend =models.CharField('待定', max_length=100)

    referenceId =models.CharField('产品总id', blank=True, max_length=100)
    referenceName =models.CharField('产品描述', max_length=100, blank=True)
    # referenceType =models.CharField('待定', max_length=100)
    # referenceTypeId =models.CharField('待定', max_length=100)
    # replyCount =models.IntegerField('待定')
    score =models.IntegerField('评分', blank=True)
    secondCategory =models.IntegerField('第二级分类', blank=True)
    shop_id = models.ForeignKey(ShopItem, on_delete=models.CASCADE)
    # status =models.CharField('待定', max_length=100)
    thirdCategory =models.IntegerField('第三级分类', blank=True)
    # title =models.CharField('待定', max_length=100)
    # usefulVoteCount =models.CharField('待定', max_length=100)
    # uselessVoteCount =models.CharField('待定', max_length=100)
    # userClient =models.CharField('待定', max_length=100)
    # userClientShow =models.CharField('待定', max_length=100)
    # userImage =models.CharField('待定', max_length=100)
    # userImageUrl =models.CharField('待定', max_length=100)
    # userImgFlag =models.CharField('待定', max_length=100)
    # userLevelColor =models.CharField('待定', max_length=100)
    userLevelId =models.CharField('用户等级id', max_length=100, blank=True)
    # userProvince =models.CharField('待定', max_length=100)
    userLevelName =models.CharField('用户等级名称', max_length=100, blank=True)
    # viewCount =models.CharField('待定', max_length=100)


    class Meta:
        db_table = 'comment'
        verbose_name = '评论详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self._id
        
class AfterComment(models.Model):
    commentid = models.CharField('评论人ID', max_length=100)
    product_id = models.CharField('产品id', max_length=100)
    content = models.TextField('追评内容')

    class Meta:
        db_table = 'aftercomment'
        verbose_name = '追评'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.product_id
    



