# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.CharField(max_length=255, verbose_name=b'Comment'),
        ),
        migrations.AlterField(
            model_name='news',
            name='gallery',
            field=models.ManyToManyField(to='news.Galleries', verbose_name=b'Gallery', blank=True),
        ),
    ]
