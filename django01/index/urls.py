from django.conf.urls import url
from .views import *

urlpatterns = [
    # 如果访问路径是 login/ 的时候, 则交给login_views去处理
    url(r'^login/$', login_views),
    # 如果访问路径是 register/ 的时候, 则交给register_views去处理
    url(r'^register/$', register_views),
    # 如果访问路径是 http:127.0.0.1/8000 的时候, 则交给index_views去处理
    url(r'^$', index_views),
    url(r'^01-temp/$', temp_views),
    url(r'^02-temp/$', temp_views02),
    url(r'03-var/$',var_views),

]
