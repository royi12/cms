from django import forms
from django.core.validators import int_list_validator


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField()


class CommentForm(forms.Form):
    content = forms.CharField()
    path = forms.CharField(validators=[int_list_validator(sep=".")])
    article_id = forms.IntegerField()
