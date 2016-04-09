from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.core.urlresolvers import reverse

from .models import Article
from .forms import ArticleForm


def article_list(request):
    article_form = ArticleForm()
    context = {'articles': Article.objects.order_by('-publish_date'), 'article_form': article_form}
    return render(request, 'articles/index.html', context)


def article(request, article_id):
    context = {'article': Article.objects.get(id=article_id)}
    return render(request, 'articles/article.html', context)


def publish(request):
    if request.method != 'POST':
        return HttpResponseRedirect(reverse('articles:index'))

    form = ArticleForm(request.POST)
    if not form.is_valid():
        return HttpResponseRedirect(reverse('articles:index'))

    new_article = Article(title=form.cleaned_data['title'], content=form.cleaned_data['content'],
                          publish_date=timezone.now())
    new_article.save()
    return HttpResponseRedirect(reverse('articles:article', args=(new_article.id,)))
