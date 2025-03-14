from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import User
from .models import *


def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST['password']
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('todoapp:home')
        else:
            messages.error(request,"Invalid Account")
            return render(request,'users:login.html',{'username' : username})
    else:
        return render(request,'users/login.html',)
    
def logout_page(request):
    logout(request)
    return redirect('todoapp:home')


def register_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "Username already taken")
            return redirect('users:register')
        
        if password != password2:
            messages.info(request, "Passwords do not match")
            return redirect('users:register')


        User.objects.create_user(username=username, password=password, email=email)

        messages.success(request, "Account created successfully!")
        return redirect('users:login')

    return render(request, 'users/register.html')
