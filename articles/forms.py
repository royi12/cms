from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
