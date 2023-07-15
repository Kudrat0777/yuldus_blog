from django.shortcuts import render
from django.views.generic import TemplateView


class PostListView(TemplateView):
    template_name = 'index.html'