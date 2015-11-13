from django.test import TestCase
from news.models import News, Categories
from django.contrib.auth.models import User


class CategoriesTestCase(TestCase):
    def setUp(self):
        Categories.objects.create(name="hello")

    def test_categories(self):
        test_category = Categories.objects.get(name="hello")
        self.assertEquals(test_category.name, "hello")


class NewsTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="hello")
        cat = Categories.objects.create(name="hello")
        news = News.objects.create(title="Test Case", description="Lorem", author_id=user.id, is_active=True)
        news.save()
        news.categories.add(cat)

    def test_news(self):
        test_news = News.objects.get(title="Test Case")
        self.assertEquals(test_news.title, "Test Case")
        self.assertEquals(test_news.count_views, 0)
