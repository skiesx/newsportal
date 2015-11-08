from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from news.models import News
from django.utils import timezone


class NewsListView(ListView):
    model = News
    queryset = News.objects.order_by('-pub_date')
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class NewsDetailView(DetailView):
    model = News

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
