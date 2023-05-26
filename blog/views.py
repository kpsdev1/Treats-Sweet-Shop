from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class BlogListView(ListView):
    # view to deisplay reviews
    template_name = "blog/blog.html"
    model = Post
