from django import forms
from django.contrib.auth.models import User


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=100, label="", widget=forms.TextInput(attrs={'placeholder': "Title"}))
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': "Content"}))


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="", widget=forms.TextInput(attrs={'placeholder': "Username"}))
    password = forms.CharField(max_length=100, label="", widget=forms.PasswordInput(attrs={'placeholder': "Password"}))


class SignupForm(forms.Form):
    username = forms.CharField(max_length=100, label="", widget=forms.TextInput(attrs={'placeholder': "Username"}))
    password = forms.CharField(max_length=100, label="", widget=forms.PasswordInput(attrs={'placeholder': "Password"}))
