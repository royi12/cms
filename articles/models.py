from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    publish_date = models.DateTimeField()
    view_count = models.IntegerField(default=0)
    author = models.ForeignKey(User, models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Comment can have comments, so each article has a tree of comments.
    The comment tree is saved using the materialized path method.
    Materialized Path saves a path to it in each comment.
    Example for comments and their path:
        comment 1
            comment 1.1
            comment 1.2
        comment 2
            comment 2.1
                comment 2.1.1
            comment 2.2
    """
    article = models.ForeignKey(Article)
    content = models.TextField()
    author = models.ForeignKey(User, models.SET_NULL, null=True)
    path = models.TextField()

    # Level in hierarchy comment tree.
    # Saved in order to generate comment tree without having to calculate it every time from path field.
    level = models.IntegerField()

    def __str__(self):
        return "{} - {}".format(self.path, self.author)