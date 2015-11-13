# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_auto_20151111_1001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='like',
        ),
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name=b'Publish date', blank=True),
        ),
    ]
