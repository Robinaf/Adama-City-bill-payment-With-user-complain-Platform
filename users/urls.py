from xml.etree.ElementInclude import include
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# from .admin import admin_site

urlpatterns=[
    path("registerPage",views.registerPage, name= "registerPage"),
    path('user_login/', views.user_login, name = 'user_login'),
    path('home/',views.home,name = 'home'),
    path('',views.index,name='index'),
    path('payment',views.payment, name='payment'),
    path('success',views.success,name='success'),
    path('cancel',views.cancel, name='cancel'),
    path('ipn/', views.ipn, name='ipn'),
    
]