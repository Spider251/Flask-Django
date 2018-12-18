from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def login_views(request):
    return HttpResponse('这是login_views视图访问路径')


def register_views(request):
    return HttpResponse("这是register_views视图访问路径")


def index_views(request):
    return HttpResponse("这是index_views视图访问路径")


def temp_views(request):
    # 1. 通过loader加载模板
    t = loader.get_template("01-temp.html")
    # 2. 将模板渲染成字符串
    html = t.render()
    # 3. 将字符串通过HttpResponse响应给客户端
    return HttpResponse(html)


def temp_views02(request):
    return render(request, '01-temp.html')


def var_views(request):
    str = "这是模板中的字符串"
    num = 3306
    tup = ("西游记", '水浒传', '三国演义', '红楼梦')
    list = ['孙悟空', '西门庆', '曹操', '贾宝玉']
    dic = {
        'BJ': '北京',
        'SZ': '深圳',
        'SH': '上海',
    }
    dog = Animal()
    ret = sayHi()
    return render(request,'02-var.html',locals())


def sayHi():
    return "Hello, this is a function ..."


class Animal(object):
    name = '狗蛋'

    def eat(self):
        return "eat" + self.name
