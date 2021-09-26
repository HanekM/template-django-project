from django.test import TestCase
from django.urls import reverse, resolve

from blog.views import HomePageView
from blog.models import (
    Category,
    Article
)
from test.mixins import TestCheckMixin


class HomeTests(TestCase, TestCheckMixin):

    @classmethod
    def setUpTestData(cls) -> None:
        
        cls.category = Category.objects.create(category='rest-framework')
        cls.article = Article.objects.create(
            title='Rest Framework Simple JWT',
            slug='rest-framework-simple-jwt',
            category=cls.category,
        )

        return super().setUpTestData()

    def test_home_view_status_code(self):
        url = reverse('blog-home')
        response = self.client.get(url)
        self.perform_common_check(response)

    def test_home_url_resolves_home_view(self):
        view = resolve('/blog/')
        self.assertEquals(view.func.view_class, HomePageView)

    def test_category_view_status_code(self):
        url = reverse('articles-category-list', args=('name',))
        response = self.client.get(url)
        self.perform_common_check(response)

    def test_article_list_url(self):
        url = reverse('articles-list')
        response = self.client.get(url)
        self.perform_common_check(response)

    def test_articles_category_url(self):
        url = reverse('articles-category-list', kwargs={'slug': self.category.category})
        response = self.client.get(url)
        self.perform_common_check(response)

    def test_article_detail(self):
        response = self.client.get(self.article.get_absolute_url())
        self.perform_common_check(response)
