from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

app_name = 'articles'
urlpatterns = [
    url(r'^$', views.article_list, name='index'),
    url(r'^publish/$', views.PublishView.as_view(), name='publish'),
    url(r'^login/$', login, {'template_name': 'articles/login.html'}, name='login'),
    url(r'^signup/$', views.SignupView.as_view(), name='signup'),
    url(r'^(?P<article_id>[0-9]+)/$', views.article, name='article'),
    url(r'^is_user_exist/$', views.is_user_exist, name='is_user_exist'),
]