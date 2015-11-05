from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from news.models import News
from django.utils import timezone


class NewsListView(ListView):
    model = News


class NewsDetailView(DetailView):
    model = News

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
