# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-29 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_view_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='publish_date',
            field=models.DateTimeField(),
        ),
    ]
