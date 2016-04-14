from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)


def validate_username(username):
    if User.objects.filter(username=username).first() is not None:
        raise ValidationError("{} already exist".format(username))

class SignupForm(forms.Form):
    username = forms.CharField(max_length=100, validators=[validate_username])
    password = forms.CharField(max_length=100)

