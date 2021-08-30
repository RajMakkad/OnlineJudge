from django.shortcuts import redirect, render 
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


def problems(request):
    context = {
        'problems': Problem.objects.all()
    }
    return render(request, 'problems.html', context)


@login_required(login_url='problems')
def problem_page(request,prob_id):
    context = {
        'problem': Problem.objects.get(primarykey = prob_id)
    }
    return render(request, 'problem_page.html', context)

# Need to fix
def submit(request,prob_id):
    if request.method == 'POST' :
        context = {
        'problems': Problem.objects.all()
    }
    return render(request, 'problems.html', context)


def about(request):
    return render(request, 'about.html', {'title': 'About_title'})



