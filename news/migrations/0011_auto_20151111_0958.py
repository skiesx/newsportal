# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20151111_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from=models.CharField(max_length=255, verbose_name=b'Title'), verbose_name=b'Slug', unique_with=(b'pub__date',), editable=False),
        ),
    ]
