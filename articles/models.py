from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    publish_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.title