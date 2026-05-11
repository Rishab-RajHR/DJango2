from django.shortcuts import render
from .models import Post
from django.db.models import Q

def post_list(request):
    query = request.GET.get('q') # search keyword
    category = request.GET.get('category') # category filter

    posts = Post.objects.all()

    # Search using Q objects
    if query:
        posts = posts.filter(
           Q(title_icontains=query) |
           Q(content_icontains=query)
        )

    # Filter by category
    if category:
        posts = posts.filter(category__iexact=category)

    return render(request, 'blog/post_list.html', {
          'posts': posts,
          'query': query,
          'category': category,
    })
