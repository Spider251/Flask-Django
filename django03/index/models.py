from django.db import models


# Create your models here.
# 创建一个实体类 - Publisher(读音:'怕不离身') 表示"出版社"
# 1.name:出版社名称 - varchar
# 2.address:出版社地址 - varchar
# 3.city:出版社所在城市 - varchar
# 4.country:出版社所在国家 - varchar
# 5.website:出版社网址 - varchar

class Publisher(models.Model):
    name = models.CharField(max_length=30, verbose_name='姓名')
    address = models.CharField(max_length=200, verbose_name='地址')
    city = models.CharField(max_length=30, verbose_name='城市')
    country = models.CharField(max_length=30, verbose_name='国家')
    website = models.URLField(null=True, verbose_name='网站')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'publisher'
        verbose_name = '出版社'
        verbose_name_plural = verbose_name



class Author(models.Model):
    name = models.CharField(max_length=30, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    email = models.EmailField(null=True, verbose_name='邮箱')
    isActive = models.BooleanField(default=True, verbose_name='有效用户')


    # 重写__str__ 函数, 以便定义对象在后台的表现名称
    def __str__(self):
        return self.name

    class Meta:
        # 表名称
        db_table = 'author'
        # 2. 指定在 admin 中显示的名称
        verbose_name = '作者'
        # 3. 指定在 admin 中显示的名称
        verbose_name_plural = verbose_name
        # 4. 指定在 admin 中按照年龄降序排序
        ordering = ['-age']


class Book(models.Model):
    title = models.CharField(max_length=50, verbose_name='书名')
    publicate_date = models.DateTimeField(verbose_name='发行时间')
    # 增加对Publisher(一)的一对多的引用关系
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True)
    authors = models.ManyToManyField(Author)
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'book'
        verbose_name = '书籍'
        verbose_name_plural = verbose_name
        ordering = ['-publicate_date']


class Wife(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    # 增加对Author的一对一的关联关系
    author = models.OneToOneField(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'wife'
