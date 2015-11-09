from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from news.models import News, Categories
from django.utils import timezone


class NewsList(ListView):
    model = News, Categories
    queryset = News.objects.order_by('-pub_date')
    # queryset = Categories.objects.order_by('News')
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(NewsList, self).get_context_data(**kwargs)
        context['categories'] = Categories.objects.all()
        context['now'] = timezone.now()
        return context


class NewsDetailView(DetailView):
    model = News

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CategoryNewsList(ListView):
    model = News
    queryset = News.objects.order_by('-pub_date')
    paginate_by = 3
    template_name = 'news/news_list.html'

    def get_queryset(self):
        categories = get_object_or_404(Categories, name=self.args[0])
        return News.objects.filter(categories=categories)

    def get_context_data(self, **kwargs):
        context = super(CategoryNewsList, self).get_context_data(**kwargs)
        # context['category'] = News.objects.filter(categories__name='Celebrity')
        context['now'] = timezone.now()
        return context
