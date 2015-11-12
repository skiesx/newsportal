from django.test import TestCase
from news.models import News, Categories
from django.contrib.auth.models import User


class NewsTestCase(TestCase):
    def setUp(self):
        test_cat = Categories.objects.create(name="hello")
        test_user = User.objects.create(username='test_user')
        News.objects.create(title="test", image="1.jpg", description="Lorem", author=test_user,
                            pub_date="2015-11-08 08:38:08")
        # Categories.objects.create(name="Tv-show", parent=self)
        # Categories.objects.create(name="Music", parent=Categories.)

    def test_categories(self):
        pass
        # tv_show = Categories.objects.get(name="Tv-show")
        # music = Categories.objects.get(name="Music")
        # self.assertEquals(tv_show.name, "adasd")

    # def test_animals_can_speak(self):
    #     """Animals that can speak are correctly identified"""
    #     lion = Animal.objects.get(name="lion")
    #     cat = Animal.objects.get(name="cat")
    #     self.assertEqual(lion.speak(), 'The lion says "roar"')
    #     self.assertEqual(cat.speak(), 'The cat says "meow"')
