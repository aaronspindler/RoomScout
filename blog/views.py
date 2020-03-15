from django.views.generic import ListView, DetailView

from .models import BlogPost


class BlogListView(ListView):
    model = BlogPost
    context_object_name = 'blog_list'
    template_name = 'blog/blog.html'


class BlogDetailView(DetailView):
    model = BlogPost
    context_object_name = 'blog'
    template_name = 'blog/blog_post.html'
