from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from news.models import News
from django.utils import timezone
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger


class NewsListView(ListView):
    model = News
    queryset = News.objects.order_by('-pub_date')
    paginate_by = 3



    def get_context_data(self, **kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    # def get_context_data(self, **kwargs):
    #     context = super(NewsListView, self).get_context_data(**kwargs)
    #     list_news = News.objects.all()
    #     paginator = Paginator(list_news, self.paginate_by)
    #
    #     page = self.request.GET.get('page')
    #
    #     try:
    #         list_news = paginator.page(page)
    #     except PageNotAnInteger:
    #         list_news = paginator.page(1)
    #     except EmptyPage:
    #         list_news = paginator.page(paginator.num_pages)
    #
    #     context['list_news'] = list_news
    #     return context


class NewsDetailView(DetailView):
    model = News

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
