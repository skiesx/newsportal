from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from news.models import News, Categories
from django.utils import timezone


class NewsList(ListView):
    model = News, Categories
    queryset = News.objects.order_by('-pub_date')
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(NewsList, self).get_context_data(**kwargs)
        context['categories'] = Categories.objects.all()
        context['popular_post'] = News.objects.order_by('-count_views')[:5]
        context['older_post'] = News.objects.order_by('-pub_date')[5:11]
        context['now'] = timezone.now()
        return context


class NewsDetailView(DetailView):
    model = News

    queryset = News.objects.all()

    # add +1 in count_views when page is open
    def get_object(self):
        news_views = super(NewsDetailView, self).get_object()
        news_views.count_views += 1
        news_views.save()
        return news_views

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['popular_post'] = News.objects.order_by('-count_views')[:5]
        context['older_post'] = News.objects.order_by('-pub_date')[5:11]
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
        context['popular_post'] = News.objects.order_by('-count_views')[:5]
        context['older_post'] = News.objects.order_by('-pub_date')[5:11]
        context['now'] = timezone.now()
        return context
