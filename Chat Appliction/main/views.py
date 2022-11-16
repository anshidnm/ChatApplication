from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class Home(View):
    def get(self,request,*args, **kwargs):
        return render(request,'index.html')

class Room(View):
    def get(self,request,*args, **kwargs):
        room = kwargs.get('room')
        return render(request,'room.html',{'room_name':room})