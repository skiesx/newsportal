# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('news', '0004_auto_20151105_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='like',
            field=models.IntegerField(default=0, verbose_name=b'Likes'),
        ),
        migrations.AddField(
            model_name='news',
            name='tag',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
    ]
