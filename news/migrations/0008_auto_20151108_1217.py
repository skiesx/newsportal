# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20151108_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='video',
            field=embed_video.fields.EmbedVideoField(verbose_name=b'Video', blank=True),
        ),
    ]
