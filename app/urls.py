from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.index, name='index'),
]