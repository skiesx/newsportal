from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
from redactor.fields import RedactorField

# Create your models here.


class Categories(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    def __unicode__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Galleries(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    image = models.ImageField(upload_to='media/news/%Y/%m/%d', verbose_name='Image')
    author = models.ForeignKey(User, verbose_name="Author")

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    categories = models.ManyToManyField(Categories, verbose_name="Categories")
    image = models.ImageField(upload_to='media/news/%Y/%m/%d', verbose_name='Image')
    description = RedactorField(verbose_name="Description")
    author = models.ForeignKey(User, verbose_name="Aumthor")
    create_date = models.DateTimeField(verbose_name='Create date', auto_now_add=True)
    pub_date = models.DateTimeField(verbose_name='Publish date')
    is_active = models.BooleanField(verbose_name="Publish?")
    gallery = models.ManyToManyField(Galleries, blank=True, verbose_name="Gallery")
    count_views = models.IntegerField(default=0, verbose_name="Views")
    slug = models.SlugField(verbose_name="Slug")

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"


class Comments(models.Model):
    user = models.ForeignKey(User, verbose_name="User")
    news = models.ForeignKey(News, verbose_name='news')
    comment = models.CharField(max_length=255, verbose_name="Comment")

    def __unicode__(self):
        return self.comment

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"