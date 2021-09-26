from django.urls import path

from blog.views import (
    HomePageView,
    ArticleList,
    ArticleCategoryList,
    ArticleDetail
)


urlpatterns = [
    # Api root: blog/
    path('', HomePageView.as_view(), name='blog-home'),
    path('articles/', ArticleList.as_view(), name='articles-list'),
    path(
        'articles/category/<slug>/', ArticleCategoryList.as_view(), name='articles-category-list'
    ),
    path(
        'articles/<year>/<month>/<day>/<slug>/', ArticleDetail.as_view(), name='news-detail'
    ),
]
