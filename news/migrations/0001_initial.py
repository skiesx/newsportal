# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mptt.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='news.Categories', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=255, verbose_name=b'Csomment')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Galleries',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'Title')),
                ('image', models.ImageField(upload_to=b'media/news/%Y/%m/%d', verbose_name=b'Image')),
                ('author', models.ForeignKey(verbose_name=b'Author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Galleries',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'Title')),
                ('image', models.ImageField(upload_to=b'media/news/%Y/%m/%d', verbose_name=b'Image')),
                ('description', models.TextField(verbose_name=b'Description')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Create date')),
                ('pub_date', models.DateTimeField(verbose_name=b'Publish date')),
                ('is_active', models.BooleanField(verbose_name=b'Publish?')),
                ('count_views', models.IntegerField(default=0, verbose_name=b'Views')),
                ('author', models.ForeignKey(verbose_name=b'Author', to=settings.AUTH_USER_MODEL)),
                ('categories', models.ManyToManyField(to='news.Categories', verbose_name=b'Categories')),
                ('gallery', models.ManyToManyField(to='news.Galleries', verbose_name=b'Gallery')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
        ),
        migrations.AddField(
            model_name='comments',
            name='news',
            field=models.ForeignKey(verbose_name=b'news', to='news.News'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(verbose_name=b'User', to=settings.AUTH_USER_MODEL),
        ),
    ]
