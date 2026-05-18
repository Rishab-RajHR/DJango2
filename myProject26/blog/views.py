from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

# List View
class PostListView(ListView):
   model = Post
   template_name = 'blog/post_list.html'
   context_object_name = 'posts'

#detail view
class PostDetailView(DetailView):
   model = Post
   template_name = 'blog/post_detail.html'
   context_object_name = 'post'