from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=100, label="", widget=forms.TextInput(attrs={'placeholder': "Title"}))
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "Content"}), label="")
