from django.conf.urls import url
from .views import *

from django.conf.urls import url

urlpatterns = [
    url(r'^$', index_views),
    url(r'^login/$', login_views,name='login'),
    url(r'^register/$', register_views,name='reg'),
]
