from django.urls import reverse

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
    return render(request, '02-var.html', locals())


def sayHi():
    return "Hello, this is a function ..."


class Animal(object):
    name = '狗蛋'

    def eat(self):
        return "eat" + self.name


def loop_views(request):
    list = ['孙悟空', '西门庆', '曹操', '贾宝玉']
    return render(request, '03-var.html', locals())


# 模板里面演示静态文件
def static_views(request):
    return render(request, '04-static.html')


def alias01_views(request):
    # 通过 a02 以及对应的参数, 反向解析成 a02 的地址
    url = reverse('a02',args=('2015',))
    print("a02的地址为:"+url)
    return render(request, '05-alias.html')


def alias02_views(request, year):
    url = reverse('a01')
    # 通过 a01 反向生成对应的地址
    print("a01的地址为:"+url)
    print("年份为:" + year)
    return render(request, '06-alias.html')
