from django.urls import path

from blog.views import HomaPageView


urlpatterns = [
    path('', HomaPageView.as_view(), name='blog-home'),
    
]
