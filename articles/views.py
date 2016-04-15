from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_safe
from django.views.generic import View
from django.views.generic.edit import CreateView

from .forms import ArticleForm
from .models import Article


@require_safe
def article_list(request):
    context = {'articles': Article.objects.order_by('-publish_date')}
    return render(request, 'articles/index.html', context)


@require_safe
def article(request, article_id):
    article = Article.objects.get(id=article_id)
    article.view_count += 1
    article.save()
    return render(request, 'articles/article.html', {'article': article})


@require_safe
def is_user_exist(request):
    """
    Used by signup form validation in client side using ajax.
    """
    username = request.GET.get('username')
    try:
        User.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponse('false')
    return HttpResponse('true')


class PublishView(View):
    @method_decorator(login_required)
    def post(self, request):
        form = ArticleForm(request.POST)
        if not form.is_valid():
            return redirect('articles:index')

        new_article = Article(title=form.cleaned_data['title'], content=form.cleaned_data['content'],
                              publish_date=timezone.now(), author=request.user)
        new_article.save()
        return redirect('articles:article', article_id=new_article.id)


class SignupView(CreateView):
    template_name = 'articles/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('articles:index')

    def form_valid(self, form):
        # Signup and login user
        response = super(SignupView, self).form_valid(form)
        user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
        login(self.request, user)
        return response
