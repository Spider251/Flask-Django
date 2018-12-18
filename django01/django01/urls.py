"""django01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from .views import *

dic = {
    'name': 'wangwc',
    'age': 18,
}

# 这是day01的例子
# urlpatterns = [
#     url('login/', admin.site.urls),
#     # 当访问路径为 /sh
#     # url(r'sh', sh_views),
#     # 当访问路径为 http://localhost:8000/show
#     url(r'^show/$', show_views),
#     # 当访问路径时 / show/四位数字/ 的时候
#     url(r'^show/(\d{4})/$', show1_views),
#     # 当访问路径为 /show/四位数字/两位数字/两位数字
#     url(r'^show/(\d{4})/(\d{2})/(\d{2})$', show2_views),
#     # 当访问路径为 /show3/ 的时候
#     url(r'^show3/$', show3_views, dic),
# ]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 访问路径是以 music/ 做为开始的时候, 将请求交给music中urls.py去处理
    url(r'^music/', include('music.urls')),
    # 访问路径是以 sport/ 做为开始的时候, 将请求交给sport中urls.py去处理
    url(r'^sport/', include('sport.urls')),
    # 访问路径是以 news/ 做为开始的时候, 将请求交给news中urls.py去处理
    url(r'^news/', include('news.urls')),
    # 访问路径中不包含指定的路径时(admin/,music/,sport/,news/), 交给index中的urls.py去处理
    url(r'^', include('index.urls')),
]