from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
from redactor.fields import RedactorField
from taggit.managers import TaggableManager
from embed_video.fields import EmbedVideoField
from autoslug import AutoSlugField
import datetime
# Create your models here.


class Categories(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    def __unicode__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


# class Galleries(models.Model):
#     title = models.CharField(max_length=255, verbose_name="Title")
#     image = models.ImageField(upload_to='media/news/%Y/%m/%d', verbose_name='Image')
#     author = models.ForeignKey(User, verbose_name="Author")
#
#     def __unicode__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = "Gallery"
#         verbose_name_plural = "Galleries"


# class Comments(models.Model):
#     user = models.ForeignKey(User, verbose_name="User")
#     news = models.ForeignKey('News', related_name='comments_news',  verbose_name='news')
#     comment = models.CharField(max_length=255, verbose_name="Comment")
#
#     def __unicode__(self):
#         return self.comment
#
#     class Meta:
#         verbose_name = "Comment"
#         verbose_name_plural = "Comments"


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    categories = models.ManyToManyField(Categories, verbose_name="Categories")
    image = models.ImageField(upload_to='media/news/%Y/%m/%d', verbose_name='Image')
    description = RedactorField(verbose_name="Description", upload_to='media/news/redactor/%Y/%m/%d')
    author = models.ForeignKey(User, verbose_name="Author")
    create_date = models.DateTimeField(verbose_name='Create date', auto_now_add=True)
    pub_date = models.DateTimeField(verbose_name='Publish date', blank=True, null=True)
    is_active = models.BooleanField(verbose_name="Publish?")
    # gallery = models.ManyToManyField(Galleries, blank=True, verbose_name="Gallery")
    count_views = models.IntegerField(default=0, verbose_name="Views")
    # like = models.IntegerField(default=0, verbose_name="Likes")
    # slug = models.SlugField(unique=True, blank=True, verbose_name="Slug")
    slug = AutoSlugField(populate_from='title', unique_with='pub_date', unique=True,
                         max_length=40, verbose_name="Slug")
    video = EmbedVideoField(verbose_name="Video", blank=True)
    # comments = models.ManyToManyField(Comments, related_name='comments_news', verbose_name="Comments", blank=True)
    tag = TaggableManager()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.is_active:
            self.pub_date = datetime.datetime.now()
        super(News, self).save(*args, **kwargs)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('news:news_detail', args=[str(self.slug)])

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
