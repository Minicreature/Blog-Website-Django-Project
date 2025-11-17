from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'   # <app>/<template>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']        # newest first
    paginate_by = 5                    # optional: 5 posts per page

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
