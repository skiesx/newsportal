from django.contrib import admin
from news.models import Categories, Galleries, News, Comments
from mptt.admin import MPTTModelAdmin


class CustomCategoriesModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20


admin.site.register(Categories, CustomCategoriesModelAdmin)
admin.site.register(Galleries)
admin.site.register(News)
admin.site.register(Comments)
