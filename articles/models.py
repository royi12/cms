from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    publish_date = models.DateTimeField('date published')
    view_count = models.IntegerField(default=0)
    author = models.ForeignKey(User, models.SET_NULL, null=True)

    def __str__(self):
        return self.title
