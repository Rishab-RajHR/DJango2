from django.shortcuts import render
from datetime import datetime

def blog_details(request):
    blogs  = [
        {"title":"Django Basics","is_featured":True,"author":"Alex Pandain"},
        {"title":"Django Advanced","is_featured":False,"author":""},
        {"title":"Django REST Framework","is_featured":False,"author":"Raman Lamba"},
    ]
    context = {
        "blogs":blogs,
        "today": datetime.now(),
        "html_code":"<h1>Welcome to My Blog</h1>",
    }
    return render(request, 'blog/blog_list.html', context)
