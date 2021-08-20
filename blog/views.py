from django.shortcuts import render 
from .models import Problem
from django.contrib.auth.decorators import login_required

# from django.http import HttpResponse

# def home(request):
#     return HttpResponse('<h1> Blog Home Hakuna Matata</h1>')

# def about(request):
#     return HttpResponse('<h1> Blog About </h1>')

# posts = [
#     {
#         'author': 'CoreyMS',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27, 2018'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'August 28, 2018'
#     }
# ]

def home(request):
    return render(request,'blog/home.html',{'title':'OJ Home'})

# @login_required(login_url='blog-home')

def problems(request):
    context = {
        'problems': Problem.objects.all()
    }
    return render(request,'blog/problems.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About_title'})
