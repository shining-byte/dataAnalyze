# Generated by Django 2.1.7 on 2019-04-01 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JDAfterComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentid', models.CharField(max_length=100, verbose_name='评论人ID')),
                ('content', models.TextField(verbose_name='追评内容')),
            ],
            options={
                'verbose_name': '京东追评',
                'verbose_name_plural': '京东追评',
                'db_table': 'jdaftercomment',
            },
        ),
        migrations.CreateModel(
            name='JDCommentItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, verbose_name='评论内容')),
                ('nickname', models.CharField(blank=True, max_length=100, verbose_name='用户名')),
                ('referenceId', models.CharField(blank=True, max_length=100, verbose_name='产品总id')),
                ('score', models.IntegerField(blank=True, verbose_name='评分')),
                ('userLevelName', models.CharField(blank=True, max_length=100, verbose_name='用户等级名称')),
            ],
            options={
                'verbose_name': '京东评论详情',
                'verbose_name_plural': '京东评论详情',
                'db_table': 'jdcomment',
            },
        ),
        migrations.CreateModel(
            name='JDHotCommentTagItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='标签名字')),
                ('count', models.CharField(blank=True, max_length=100, verbose_name='数量')),
            ],
            options={
                'verbose_name': '京东热评',
                'verbose_name_plural': '京东热评',
                'db_table': 'jdhotcomment',
            },
        ),
        migrations.CreateModel(
            name='JDProductsItem',
            fields=[
                ('productid', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='产品id')),
                ('category', models.CharField(blank=True, max_length=50, verbose_name='产品分类名')),
                ('description', models.TextField(blank=True, verbose_name='产品描述')),
                ('imgurl', models.CharField(max_length=300, verbose_name='封面地址')),
                ('reallyPrice', models.FloatField(blank=True, verbose_name='当前价格')),
                ('url', models.URLField(blank=True, verbose_name='商品地址')),
            ],
            options={
                'verbose_name': '京东商品信息',
                'verbose_name_plural': '京东商品信息',
                'db_table': 'jdproduct',
            },
        ),
        migrations.CreateModel(
            name='ProductName',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='名字')),
                ('jdProductId', models.CharField(default=1, max_length=50, verbose_name='京东产品id')),
                ('taobaoProductId', models.CharField(default=0, max_length=50, verbose_name='淘宝产品id')),
            ],
            options={
                'verbose_name': '产品名字',
                'verbose_name_plural': '产品名字',
                'db_table': 'productname',
            },
        ),
        migrations.CreateModel(
            name='TaobaoComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('displayUserNick', models.CharField(max_length=50, verbose_name='卖家')),
                ('rateContent', models.TextField(verbose_name='评论')),
            ],
            options={
                'verbose_name': '淘宝产品评论',
                'verbose_name_plural': '淘宝产品评论',
                'db_table': 'taobaocomment',
            },
        ),
        migrations.CreateModel(
            name='TaobaoProduct',
            fields=[
                ('productid', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='产品id')),
                ('productprice', models.FloatField(verbose_name='价钱')),
                ('producturl', models.URLField(verbose_name='商品购买地址')),
                ('productname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taobao.ProductName')),
            ],
            options={
                'verbose_name': '淘宝商品',
                'verbose_name_plural': '淘宝商品',
                'db_table': 'taobaoproduct',
            },
        ),
        migrations.CreateModel(
            name='TaobaoTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagname', models.CharField(max_length=50, verbose_name='特性名字')),
                ('tagcount', models.CharField(max_length=50, verbose_name='数量')),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taobao.TaobaoProduct')),
            ],
            options={
                'verbose_name': '淘宝产品特性',
                'verbose_name_plural': '淘宝产品特性',
                'db_table': 'taobaotag',
            },
        ),
        migrations.CreateModel(
            name='JDCommentSummaryItem',
            fields=[
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='taobao.JDProductsItem')),
                ('afterCount', models.IntegerField(blank=True, verbose_name='追加评论')),
                ('averageScore', models.IntegerField(blank=True, verbose_name='平均评分')),
                ('commentCount', models.IntegerField(blank=True, verbose_name='评分总人数')),
                ('defaultGoodCount', models.IntegerField(blank=True, verbose_name='默认好评')),
                ('generalCount', models.IntegerField(blank=True, verbose_name='中评总人数')),
                ('goodCount', models.IntegerField(blank=True, verbose_name='好评人数')),
                ('imageListCount', models.IntegerField(blank=True, verbose_name='晒图评论人数')),
                ('poorCount', models.IntegerField(blank=True, verbose_name='差评人数')),
                ('score', models.IntegerField(blank=True, verbose_name='评论等级')),
            ],
            options={
                'verbose_name': '京东评论总详情',
                'verbose_name_plural': '京东评论总详情',
                'db_table': 'jdcommentsummary',
            },
        ),
        migrations.AddField(
            model_name='taobaocomment',
            name='productid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taobao.TaobaoProduct'),
        ),
        migrations.AddField(
            model_name='jdproductsitem',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taobao.ProductName'),
        ),
        migrations.AddField(
            model_name='jdhotcommenttagitem',
            name='productid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taobao.JDProductsItem'),
        ),
        migrations.AddField(
            model_name='jdcommentitem',
            name='productid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taobao.JDProductsItem'),
        ),
        migrations.AddField(
            model_name='jdaftercomment',
            name='productid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taobao.JDProductsItem'),
        ),
    ]
