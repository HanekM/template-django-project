from django.views.generic import (
    TemplateView,
    ListView,
    DateDetailView
)

from blog.models import Article, Category


class HomePageView(TemplateView):

    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(main_page=True)[:5]
        context['categories'] = Category.objects.all()
        return context


class ArticleDetail(DateDetailView):

    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'item'
    date_field = 'date_published'
    query_pk_and_slug = True
    month_format = '%m'
    allow_future = True

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetail, self).get_context_data(*args, **kwargs)
        try:
            context['images'] = context['item'].images.all()
        except:
            pass
        return context


class ArticleList(ListView):

    model = Article
    queryset = Article.objects.all().select_related(
        'category'
    ).prefetch_related(
        'images'
    ).order_by('-date_published')
    template_name = 'blog/articles_list.html'
    context_object_name = 'items'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleList, self).get_context_data(*args, **kwargs)
        try:
            context['category'] = Category.objects.get(slug=self.kwargs.get('slug'))
        except Exception:
            context['category'] = None

        return context


class ArticleCategoryList(ArticleList):

    def get_queryset(self, *args, **kwargs):
        articles = Article.objects.filter(
            category__category__in=[self.kwargs['slug']]
        ).distinct()

        return articles
