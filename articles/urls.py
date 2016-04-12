from django.conf.urls import url

from . import views

app_name = 'articles'
urlpatterns = [
    url(r'^$', views.article_list, name='index'),
    url(r'^publish/$', views.PublishView.as_view(), name='publish'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^signup/$', views.SignupView.as_view(), name='signup'),
    url(r'^(?P<article_id>[0-9]+)/$', views.article, name='article'),
]