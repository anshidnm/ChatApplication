from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import RegisterForm,LoginForm
from django.views import View
from django.contrib import messages


# Create your views here.
class Register(View):
    def get(self,request,*args, **kwargs):
        form = RegisterForm()
        return render(request,'register.html',{"form":form})

    def post(self,request,*args, **kwargs):
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            username = request.POST.get("username")
            password = request.POST.get("password1")
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("/")
        return render(request,'register.html',{"form":form})

class Login(View):
    def get(self,request,*args, **kwargs):
        form = LoginForm()
        return render(request,'login.html',{"form":form})
    
    def post(self,request,*args, **kwargs):
        form = LoginForm(request.POST or None)
        username = request.POST.get("username")
        password = request.POST.get("password")
        if form.is_valid():
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("/")
        messages.info(request,"Invalid username or password")
        return render(request,'login.html',{"form":form})

class Logout(View):
    def get(self,request,*args, **kwargs):
        logout(request)
        return redirect("/authentication/login")