from django.db.models import Avg, Sum, Count, F, Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from .models import *


# Create your views here.

def addbook_views(request):
    # 方式1 : Entry.objects.create()
    # book = Book.objects.create(title="Python编程基础", publicate_date='2015-10-12')
    # print("新增加的书籍的ID为:%d" % book.id)

    # 方式2 : 通过Entry创建对象, 对象.save()
    # book = Book(title='数据库基础')
    # book.publicate_date = '2018-01-15'
    # book.save()
    # print("新增加的书籍的ID为:%d" % book.id)

    Book.objects.create(title='WEB开发基础', publicate_date='2018-01-15')
    Book.objects.create(title="人工智能的发展", publicate_date='2015-10-12')
    Book.objects.create(title='数据库的高级进阶', publicate_date='2015-10-12')
    Book.objects.create(title='网络爬虫', publicate_date='2018-01-15')

    return HttpResponse('Add Book Success')


def query_views(requst):
    # 1. 基本查询操作 - all()
    # books = Book.objects.all()
    # print(type(books))
    # for i in books:
    #     print('ID:%d,书名:%s,出版日期:%s'%(i.id, i.title, i.publicate_date))
    # print(books.query)

    # 2.查询返回部分列 - values()
    # books = Book.objects.values('title', 'publicate_date')
    # for book in books:
    #     print("书名:%s,出版日期:%s" % (book['title'], book['publicate_date']))

    # 3.查询返回指定列
    # books = Book.objects.values_list('title', 'publicate_date')
    # for i in books:
    #     print("书名:%s,出版日期:%s" % (i[0], i[1]))

    # 4.查询只返回一条(对象)数据  可以使用.方法调值 - get()
    # book = Book.objects.get(id=1)
    # print(book.title)

    # 5.查询id为1的Book的信息
    # list = Book.objects.filter(id=1)
    # print(list)

    # 6. 查询publicate_date为2015-10-12的Book的信息
    # books = Book.objects.filter(publicate_date='2015-10-12')
    # for i in books:
    #     print(i.title, i.publicate_date)
    # books = Book.objects.filter(publicate_date='2015-10-12',id=1)
    # print(books)

    # 7. 查询publicate_date是2015年的所有的数据
    # list = Book.objects.filter(publicate_date__year__gt=2015)
    # for i in list:
    #     print("ID:%s,书名:%s,出版日期:%s" % (i.id,i.title,i.publicate_date))

    # 8. 练习
    # 1. 查询Author表中age大于等于30的Author的信息
    '''
    list = Author.objects.filter(age__gte=30)
    for i in list:
        print("年龄大于等于30的有:%s" % i.name)

    # 2. 查询Author表中所有姓"王"的信息
    list = Author.objects.get(name__contains='王')
    print("所有姓王的有:%s" % list.name)

    # 3. 查询Author表中Email中包含"wang"的Author的信息
    list = Author.objects.get(email__contains='wang')
    print("email中包含wang的:%s" % list.name)

    # 4. 查询Author表中age小于"RapWang"的age的所有的信息
    list2 = Author.objects.filter(age__lt=(Author.objects.get(name='RapWang').age))
    for i in list2:
        print(i.id, i.name, i.age, i.email)

    # 13. 查询Author表中所有人的平均年龄 - 聚合函数 aggregate()
    result = Author.objects.aggregate(avg=Sum('age'))
    print("总年龄为:%d" % result['avg'])
    '''
    # 14. 查询Book表中每个publicate_date所发行的书籍的数量
    a = Book.objects.values('publicate_date').annotate(count=Count('title')).values('publicate_date', 'count').all()
    list = Book.objects.filter(id__gt=1).values('publicate_date').annotate(count=Count('title')).values(
        'publicate_date', 'count').all()
    print(list)
    # print(a)
    return HttpResponse("<script>alert('查询成功!')</script>")


def home_views(request):
    # author = Author.objects.all()
    authors = Author.objects.filter(isActive=True)
    return render(request, 'homework.html', locals())


def update_views(request):
    # author = Author.objects.get(id=1)
    # author.age = 45
    # author.save()

    authors = Author.objects.exclude(id=1)
    authors.update(age=45)
    return HttpResponse("Update OK")


def delete_views(request, id):
    # 单条修改, 运行快
    # author = Author.objects.get(id=id)
    # author.isActive = False
    # author.save()

    # 运行慢,多条修改
    list = Author.objects.filter(id=id)
    list.update(isActive=False)
    return redirect('/03-homework')


def show_views(request, id):
    Author.objects.all().update(age=F('age') + 10)
    return HttpResponse("<script>alert('修改成功')</script>")


def doQ_views(request):
    # 获取id=1 或者isActive=True的Author们的信息
    authors = Author.objects.filter(Q(id=1) | Q(isActive=True))
    for au in authors:
        print(au.id, au.name)
    return HttpResponse("OK")


def oto_views(request):
    # 声明一个 wife 对象, 并指定其author信息
    # wife = Wife()
    # wife.name = "魏超夫人"
    # wife.age = 30
    # wife.author_id = 4
    # wife.save()

    # wife = Wife()
    # wife.name = "麻蛋 Girl"
    # wife.age = 19
    # author = Author.objects.get(id=3)
    # wife.author = author
    # wife.save()

    # 查询之正向查询(通过wife查找author)
    # wife = Wife.objects.get(id=1)
    # author = wife.author

    author = Author.objects.get(id=1)
    wife = author.wife

    print("Wife:%s,Author:%s" % (wife.name, author.name))
    return HttpResponse("OTO OK")


def otm_views(request):
    # 1.正向查询: Book 查询 Publisher
    book = Book.objects.get(id=3)
    publisher = book.publisher
    print("书籍名称"+book.title)
    print("所在出版社:"+publisher.name)
    # 2.反向查询: Publisher 查询 Book
    # pub = Publisher.objects.get(id=1)
    # books = pub.book_set.all()
    # print("出版社名称:"+pub.name)
    # print("所出版的图书:")
    # for book in books:
    #     print("Book Title:"+book.title)
    return HttpResponse("Query OK")

def mtm_views(request):
    # book = Book.objects.get(id=2)
    # print(book)
    # authors = book.authors.all()
    # print("书名:"+book.title)
    # for au in authors:
    #     print("作者:"+au.name)

    # 查询Rapwang出版的书籍
    # author = Author.objects.get(name='Rapwang')
    # books = author.book_set.all()
    # print(author.name+"所出版的书籍有:")
    # for book in books:
    #     print("书名:"+book.title)
    return HttpResponse;("OJBK")