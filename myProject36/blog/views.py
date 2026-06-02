from django.http import HttpResponse
from django.shortcuts import render
from .models import UserList
from django.views.decorators.cache import cache_page
from django.core.cache import cache

# @cache_page(30) # Cache the view for 30 seconds
# def users_list(request):
#     print("Fetching user list from database")
#     users = UserList.objects.all()
#     return render(request, 'users.html', {'users': users})

def users_list(request):
    users = UserList.objects.all()
    return render(request, 'users.html', {'users': users})
  
def clear_catch(request):
    cache.clear()
    return HttpResponse("All Cache Cleared")
  

