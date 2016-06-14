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
    Materialized Path saves a path in each comment.
    Example for comments and their path:
        comment 1
            comment 1.1
            comment 1.2
        comment 2
            comment 2.1
                comment 2.1.1
            comment 2.2
    Each number is padded to be 3 digits long, so 1 becomes 001.
    That way, when sorting, 100 will be after 99 and not after 10 and 1.
    With the same example:
        comment 001
            comment 001.001
            comment 001.002
        comment 002
            comment 002.001
                comment 002.001.001
            comment 002.002
    """
    article = models.ForeignKey(Article)
    content = models.TextField()
    author = models.ForeignKey(User, models.SET_NULL, null=True)
    path = models.TextField()

    # Level in hierarchy comment tree. Highest level is 0.
    # Saved in order to generate comment tree without having to calculate it every time from path field.
    level = models.IntegerField()

    def __str__(self):
        return "{} - {}".format(self.path, self.author)