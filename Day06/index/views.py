from django.http import HttpResponse, request
from django.shortcuts import render
from .forms import *


# Create your views here.

def request_views(request):
    # print(dir(request))
    # print(request.META)

    scheme = request.scheme
    body = request.body
    path = request.path
    host = request.get_host()
    method = request.method
    get = request.GET
    post = request.POST
    cookies = request.COOKIES

    return render(request, '01-request.html', locals())


def referer_views(request):
    # 获取请求原地址, 如果没有原地址, 则获取一个/
    referer = request.META.get("HTTP_REFERER", '/')
    return HttpResponse("Referer is " + referer)


def login_views(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        # 接收前端传递过来的数据
        uname = request.POST['uname']
        upwd = request.POST['upwd']
        print("uname:%s,upwd:%s" % (uname, upwd))
        return HttpResponse("OK ")


def form_views(request):
    if request.method == 'GET':
        form = RemarkForm()
        return render(request, '04-form.html', locals())
    else:
        # 1. 通过RemarkForm的构造函数, 接收请求提交数据
        form = RemarkForm(request.POST)
        # 2. 通过验证
        if form.is_valid():
            # 3. 通过验证后取值
            cd = form.cleaned_data
            print(cd)
        return HttpResponse("取值成功")


def modelform_views(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, '05-modelform.html', locals())
    else:
        # 将 request.POST传递给RegisterForm的构造函数
        form = RegisterForm(request.POST)
        # 让form通过验证
        if form.is_valid():
            # 取值
            user = User(**form.cleaned_data)
            user.save()
            print("uname:%s,upwd:%s,email:%s" % (user.uname, user.upwd, user.uemail))
        return HttpResponse("OK")


def homework(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, '06-homework.html', locals())
    else:
        form = LoginForm(request.POST)
        user = User.objects.all()
        for i in user:
            upwd = i.upwd
            uname = i.uname
            if form.is_valid():
                login = Models(**form.cleaned_data)
                if login.uname == uname and login.upwd == upwd:
                    return HttpResponse("登录成功")
            print(login.uname,uname,login.upwd,upwd)
            return HttpResponse("登录失败")
