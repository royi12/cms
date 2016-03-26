from django.conf.urls import url

from . import views

app_name = 'articles'
urlpatterns = [
    url(r'^$', views.article_list, name='index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^publish/$', views.publish, name='publish'),
    url(r'^(?P<article_id>[0-9]+)/$', views.article, name='article'),
]