from django.contrib import admin
from news.models import Categories, Galleries, News, Comments
from mptt.admin import MPTTModelAdmin
from embed_video.admin import AdminVideoMixin


class CustomCategoriesModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20


class NewsAdmin(AdminVideoMixin, admin.ModelAdmin):
    # fields = ('title', 'categories', 'image', 'description', 'author', 'pub_date', 'is_active', 'tag')
    list_display = ('title', 'pub_date', 'author')
    fieldsets = ((None, {
        'fields': ('title', 'categories', 'image', 'description', 'author', 'video')
    }),
                 ('Advanced options', {
                     'classes': ('collapse',),
                     'fields': ('pub_date', 'is_active', 'tag')
                 }),
                 ('Comments', {
                     'classes': ('collapse',),
                     'fields': ('comments',)
                 }),
    )

admin.site.register(Categories, CustomCategoriesModelAdmin)
admin.site.register(Galleries)
admin.site.register(News, NewsAdmin)
admin.site.register(Comments)
