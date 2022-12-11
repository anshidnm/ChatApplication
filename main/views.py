from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginRequiredMixin,View):
    login_url = "/authentication/login/"
    def get(self,request,*args, **kwargs):
        return render(request,'index.html')

class Room(LoginRequiredMixin,View): 
    login_url = "/authentication/login/"
    def get(self,request,*args, **kwargs):
        room = kwargs.get('room')
        today = date.today()
        return render(request,'room.html',{'room_name':room,'date':today})

