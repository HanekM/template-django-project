from django.contrib import admin
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _

from blog.models import (
    Article,
    Category,
    ArticleImage
)
from blog.forms import ArticleImageForm


class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    form = ArticleImageForm
    extra = 0
    fieldsets = (
        ('Image', {
                'fields': ('title', 'image',),
            }
        ),
    )


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_published', 'category', 'slug', 'main_page')
    inlines = [ArticleImageInline]
    multiupload_form = True
    multiupload_list = False
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('category',)
    fieldsets = (
        ('', {
            'fields': ('title', 'description', 'category', 'main_page'),
        }),
            ((_('Additionally')), {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('slug',),
        }),
    )

    def delete_file(self, pk, request):
        '''
        Delete an image
        '''
        obj = get_object_or_404(ArticleImage, pk=pk)

        return obj.delete()


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')
    fieldsets = (
        ('', {
            'fields': ('category', ),
        }),
    )


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
