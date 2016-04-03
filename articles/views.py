from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.core.urlresolvers import reverse

from .models import Article


def article_list(request):
    context = {'articles': Article.objects.order_by('-publish_date')}
    return render(request, 'articles/index.html', context)

    
def article(request, article_id):
    context = {'article': Article.objects.get(id=article_id)}
    return render(request, 'articles/article.html', context)
    
    
def publish(request):
    new_article = Article(title=request.POST['title'], content=request.POST['content'], publish_date=timezone.now())
    new_article.save()
    return HttpResponseRedirect(reverse('articles:article', args=(new_article.id,)))
    