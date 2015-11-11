# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20151111_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, unique_with=(b'pub_date',), populate_from=b'title', max_length=40, verbose_name=b'Slug'),
        ),
    ]
