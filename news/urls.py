from django.conf.urls import url
from news.views import NewsListView, NewsDetailView
from . import views

urlpatterns = [

    url(r'^$', NewsListView.as_view(), name='news_list'),
    url(r'^(?P<slug>[-\w]+)/$', NewsDetailView.as_view(), name='news_detail'),

    # url(r'^blog/$', 'myapp.views.blog', name='blog'),
    # url(r'^blog/(?P<slug>[\w-]+)/$', 'myapp.views.blog_detail', name='blog_detail'),
]

# urlpatterns = [
#     url(r'^$', MoviesListView.as_view(), name="movies_list"),
#     url(r'^(?P<slug>[-\w]+)/$', MoviesDetailView.as_view(), name='movie_detail'),
# ]