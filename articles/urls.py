from django.conf.urls import url

from . import views

app_name = 'articles'
urlpatterns = [
    url(r'^$', views.article_list, name='index'),
    url(r'^publish/$', views.publish, name='publish'),
    url(r'^login$', views.login_view, name='login'),
    url(r'^(?P<article_id>[0-9]+)/$', views.article, name='article'),
]