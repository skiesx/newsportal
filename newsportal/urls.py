from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView


urlpatterns = [
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/home/hellpirat/work/newsportal/media'}),

    url(r'^redactor/', include('redactor.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # url(r'^$', include('news.urls', namespace='news')),
    url(r'^news/', include('news.urls', namespace='news')),

    url(r'^home/', TemplateView.as_view(template_name='base.html'))


]

if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)