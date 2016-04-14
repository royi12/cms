from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.views.generic import View

from .models import Article
from .forms import ArticleForm, LoginForm, SignupForm


def article_list(request):
    article_form = ArticleForm()
    context = {'articles': Article.objects.order_by('-publish_date'), 'article_form': article_form,
               'username': request.user.username}
    return render(request, 'articles/index.html', context)


def article(request, article_id):
    article = Article.objects.get(id=article_id)
    article.view_count += 1
    article.save()
    return render(request, 'articles/article.html', {'article': article})


class PublishView(View):
    @method_decorator(login_required)
    def post(self, request):
        form = ArticleForm(request.POST)
        if not form.is_valid():
            return HttpResponseRedirect(reverse('articles:index'))

        new_article = Article(title=form.cleaned_data['title'], content=form.cleaned_data['content'],
                              publish_date=timezone.now(), author=request.user)
        new_article.save()
        return HttpResponseRedirect(reverse('articles:article', args=(new_article.id,)))


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('articles:index'))
        return render(request, 'articles/login.html', {'form': LoginForm()})

    def post(self, request):
        login_page = render(request, 'articles/login.html', {'form': LoginForm()})
        received_form = LoginForm(request.POST)
        if not received_form.is_valid():
            return login_page

        user = authenticate(username=received_form.cleaned_data['username'],
                            password=received_form.cleaned_data['password'])
        if user is None:
            return login_page

        login(request, user)
        return HttpResponseRedirect(reverse('articles:index'))


class SignupView(View):
    def get(self, request):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('articles:index'))
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
        return HttpResponseRedirect(reverse('articles:index'))


class IsUserExistView(View):
    """
    Used by signup form validation in client side using ajax.
    """
    def get(self, request):
        username = request.GET.get('username')
        try:
            User.objects.get(username=username);
        except  User.DoesNotExist:
            return HttpResponse('false')
        return HttpResponse('true')