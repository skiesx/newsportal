from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from news.views import CategoryNewsList


urlpatterns = [
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/home/hellpirat/work/newsportal/media'}),

    url(r'^redactor/', include('redactor.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', include('news.urls')),

    url(r'^news/', include('news.urls', namespace='news')),

    url(r'^cat/([\w-]+)/$', CategoryNewsList.as_view(), name='category_list'),

]

if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)