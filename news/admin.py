from django.contrib import admin
from news.models import Categories, Galleries, News, Comments
# Register your models here.

admin.site.register(Categories)
admin.site.register(Galleries)
admin.site.register(News)
admin.site.register(Comments)