from django.conf.urls import url
from .views import *

urlpatterns = [
    # 当访问路径为 index/ 的时候,则将请求交给index_views()
    # 完整请求路径为 http://localhost:8000/music/index
    # 当访问路径为空的时候, 则将请求交给index_views去处理
    url(r'^$', index_views),
    url(r'^index/$', index_views),

]
