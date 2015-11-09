from django.conf.urls import url
from news.views import NewsList, NewsDetailView, CategoryNewsList
from . import views

urlpatterns = [

    url(r'^$', NewsList.as_view(), name='news_list'),
    url(r'^(?P<slug>[-\w]+)/$', NewsDetailView.as_view(), name='news_detail'),


    # url(r'^cat/(?P<slug>[-\w]+)/$', NewsDetailView.as_view(), name='news_detail'),
    url(r'^cat/([\w-]+)/$', CategoryNewsList.as_view(), name='category_list'),

    # url(r'^page(?P<page>[0-9]+)/$', NewsListView.as_view(), name='news_list'),

]
