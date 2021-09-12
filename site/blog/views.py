from typing import Any

from django import http
from django.shortcuts import render
from django.views.generic import TemplateView


class HomaPageView(TemplateView):

    def get(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:

        return render(request, 'blog/index.html', context=None)
