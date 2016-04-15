from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField()