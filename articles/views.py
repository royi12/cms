from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_safe
from django.views.generic import View

from .models import Article
from .forms import ArticleForm, LoginForm, SignupForm


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


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated():
            return redirect('articles:index')
        return render(request, 'articles/login.html')

    def post(self, request):
        login_page = render(request, 'articles/login.html')
        received_form = LoginForm(request.POST)
        if not received_form.is_valid():
            return login_page

        user = authenticate(username=received_form.cleaned_data['username'],
                            password=received_form.cleaned_data['password'])
        if user is None:
            return login_page

        login(request, user)
        return redirect('articles:index')


class SignupView(View):
    def get(self, request):
        if request.user.is_authenticated():
            return redirect('articles:index')
        return render(request, 'articles/signup.html')

    def post(self, request):
        received_form = SignupForm(request.POST)
        if not received_form.is_valid():
            return render(request, 'articles/signup.html')

        new_user = User.objects.create_user(username=received_form.cleaned_data['username'],
                                            password=received_form.cleaned_data['password'])
        new_user.save()

        user = authenticate(username=received_form.cleaned_data['username'],
                            password=received_form.cleaned_data['password'])
        if user is None:
            return render(request, 'articles/signup.html')
        login(request, user)
        return redirect('articles:index')
