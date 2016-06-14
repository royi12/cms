from django import forms
from django.core.validators import int_list_validator

from articles.models import Comment


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField()


class CommentForm(forms.Form):
    # path is used for comment of a comment.
    # If it's a regular comment and not a comment of a comment, then path is not sent.
    path = forms.CharField(required=False, validators=[int_list_validator(sep=".")])
    content = forms.CharField()
    article_id = forms.IntegerField()

    def clean(self):
        cleaned_data = super(CommentForm, self).clean()
        if self._errors or not self.cleaned_data.get('path'):
            return cleaned_data

        path = cleaned_data['path']
        article_id = cleaned_data['article_id']
        if Comment.objects.filter(article_id=article_id, path=path).count() != 1:
            self.add_error('path', "There is no comment {} in article {}".format(path, article_id))
        return cleaned_data
