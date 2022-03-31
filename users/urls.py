from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path("registerPage",views.registerPage, name= "registerPage"),
    path('user_login/', views.user_login, name = 'user_login'),
    path('home/',views.home,name = 'home')
]