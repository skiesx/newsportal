# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20151105_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, verbose_name=b'Slug'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.ForeignKey(verbose_name=b'Aumthor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=redactor.fields.RedactorField(verbose_name=b'Description'),
        ),
    ]
