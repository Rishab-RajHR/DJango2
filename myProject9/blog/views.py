from django.shortcuts import render

def home(request):
  return render(request, 'blog.html')

def blog(request):
   students_list=[
      {"name":"Alex", "class":"10th"},
      {"name":"Sohit", "class":"9th"},
      {"name":"Aman", "class":"8th"},
   ]
   return render(request, 'blog.html', {'students': students_list})
