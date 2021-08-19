from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User ,auth


def register(request) :

    if request.method == 'POST' :

        name = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user = User.objects.create_user(username=name,email=email,password=password1)
        user.save()
        messages.success(request,f'Account Created for {name} !')
        return redirect('blog-home')

    else :
        return render(request,'users/register.html')


def login(request) :
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            messages.info(request,'logged In')
            return redirect('blog-home')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login_n')
    else:
        return render(request,'users/login.html',{'title':'OJ-login'})


def logout(request):
    auth.logout(request)
    return redirect('blog-home')