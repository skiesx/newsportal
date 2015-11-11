# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20151107_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='comments',
            field=models.ManyToManyField(related_name='comments_news', verbose_name=b'Comments', to='news.Comments', blank=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='news',
            field=models.ForeignKey(related_name='comments_news', verbose_name=b'news', to='news.News'),
        ),
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.ForeignKey(verbose_name=b'Author', to=settings.AUTH_USER_MODEL),
        ),
    ]
