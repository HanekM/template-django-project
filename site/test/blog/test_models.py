from django.test import TestCase

from blog.models import Category


class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(category='innovations')

    def test_get_absolute_url(self):
        self.assertEquals(self.category.get_absolute_url(), '/blog/articles/category/innovations/')
