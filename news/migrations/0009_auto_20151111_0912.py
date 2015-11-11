# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20151108_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='news',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='user',
        ),
        migrations.RemoveField(
            model_name='news',
            name='comments',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
