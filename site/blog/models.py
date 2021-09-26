from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    category = models.CharField(
        verbose_name=_('Categories'), max_length=250, help_text=_('No more than 250 characters')
    )

    objects = models.Manager()

    class Meta:
        verbose_name = _('News catagory')
        verbose_name_plural = _('News catagories')

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        try:
            url = reverse('articles-category-list', kwargs={'slug': self.category})
        except Exception:
            url = '/'
        return url


class Article(models.Model):
    title = models.CharField(
        _('Title'), max_length=250, help_text=_('No more than 250 characters')
    )
    description = models.TextField(verbose_name=_('Description'), blank=True,)
    date_published = models.DateTimeField(_('Date published'), auto_now=True)
    slug = models.SlugField(_('Slag'), unique_for_date='date_published')
    main_page = models.BooleanField(_('Main'), default=False, help_text=_('Show'))
    category = models.ForeignKey(
        Category, 
        related_name='news', 
        blank=True, null=True,
        verbose_name=_('Categories'),
        on_delete=models.CASCADE
    )

    objects = models.Manager()

    class Meta:
        ordering = ('-id', )
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        try:
            url = reverse('news-detail', kwargs={
                    'year': self.date_published.strftime('%Y'),
                    'month': self.date_published.strftime('%m'),
                    'day': self.date_published.strftime('%d'),
                    'slug': self.slug,
                }
            )
        except Exception:
            url = '/'
        return url


class ArticleImage(models.Model):
    article = models.ForeignKey(Article,
        verbose_name=_('Article'),
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField(_('Image'), upload_to='images')
    title = models.CharField(
        _('Title'), blank=True, max_length=250, help_text=_('No more than 250 characters')
    )

    class Meta:
        verbose_name = _('Article image')
        verbose_name_plural = _('Article images')

    def __str__(self):
        return self.url

    @property
    def filename(self):
        return self.image.name.rsplit('/', 1)[-1]
