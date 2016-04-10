from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login

from .models import Article
from .forms import ArticleForm, LoginForm


def article_list(request):
    article_form = ArticleForm()
    context = {'articles': Article.objects.order_by('-publish_date'), 'article_form': article_form, 'username': request.user.username}
    return render(request, 'articles/index.html', context)


def article(request, article_id):
    context = {'article': Article.objects.get(id=article_id)}
    return render(request, 'articles/article.html', context)

@login_required
def publish(request):
    if request.method != 'POST':
        return HttpResponseRedirect(reverse('articles:index'))

    form = ArticleForm(request.POST)
    if not form.is_valid():
        return HttpResponseRedirect(reverse('articles:index'))

    new_article = Article(title=form.cleaned_data['title'], content=form.cleaned_data['content'],
                          publish_date=timezone.now(), author=request.user)
    new_article.save()
    return HttpResponseRedirect(reverse('articles:article', args=(new_article.id,)))


def login_view(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('articles:index'))

    login_page = render(request, 'articles/login.html', {'form': LoginForm()})
    if request.method != 'POST':
        return login_page

    received_form = LoginForm(request.POST)
    if not received_form.is_valid():
        return login_page

    user = authenticate(username=received_form.cleaned_data['username'], password=received_form.cleaned_data['password'])
    if user is None:
        return login_page

    login(request, user)
    return HttpResponseRedirect(reverse('articles:index'))
