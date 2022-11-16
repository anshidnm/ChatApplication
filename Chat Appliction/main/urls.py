from django.urls import path
from django.views.generic import TemplateView
from  . import views

urlpatterns = [
    path('',views.Home.as_view(),name="home"),
    path('<str:room>/',views.Room.as_view(),name="room")
]
