from django.shortcuts import render
from datetime import datetime

class User:
   def __init__(self,name,age):
      self.name = name
      self.age = age
def home(request):
   context = {
       "name":"Alex Pandian",
       "age": 25,
       "skill":["python", "django", "React"],
       "user":User("Kumar", 30),
       "blog":{
          "title": "Django Template Intro",
          "author": {
               "name": "Alex Pandian",
          },
          "content":"<b>This is Bold</b>",
          "created_at": datetime(2025,8,18,10,30)
       },
       "empty_value": None,
   }
   return render(request,"blog/home.html",context)
