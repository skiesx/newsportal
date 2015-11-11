from django.conf.urls import url
from news.views import NewsList, NewsDetailView


urlpatterns = [

    url(r'^$', NewsList.as_view(), name='news_list'),
    url(r'^(?P<slug>[-\w]+)/$', NewsDetailView.as_view(), name='news_detail'),
]
