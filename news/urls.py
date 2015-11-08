from django.conf.urls import url
from news.views import NewsListView, NewsDetailView
from . import views

urlpatterns = [

    url(r'^$', NewsListView.as_view(), name='news_list'),
    url(r'^(?P<slug>[-\w]+)/$', NewsDetailView.as_view(), name='news_detail'),

    # url(r'^page(?P<page>[0-9]+)/$', NewsListView.as_view(), name='news_list'),

]
