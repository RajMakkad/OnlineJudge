from django.shortcuts import redirect, render 
from .models import Problem
from django.contrib.auth.decorators import login_required


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



