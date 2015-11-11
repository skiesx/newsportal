# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import embed_video.fields
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20151108_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='video',
            field=embed_video.fields.EmbedVideoField(default=datetime.datetime(2015, 11, 8, 12, 16, 56, 462994, tzinfo=utc), verbose_name=b'Video'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(verbose_name=b'Publish date', blank=True),
        ),
    ]
