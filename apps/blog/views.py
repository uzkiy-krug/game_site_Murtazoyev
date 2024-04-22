from django.shortcuts import render

from django.views.generic import TemplateView, DetailView

# Create your views here.


class BlogListView(TemplateView):
    template_name = 'blog/blogs.html'


class BlogDetailView(TemplateView):
    template_name = 'blog/blog_detail.html'

