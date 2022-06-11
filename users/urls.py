from xml.etree.ElementInclude import include
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from . import views
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
# from .admin import admin_site

urlpatterns=[
    path("registerPage",views.registerPage, name= "registerPage"),
    path('user_login/', views.user_login, name = 'user_login'),
    path('home/',views.home,name = 'home'),
    path('',views.index,name='index'),
    path('email/',views.sendemail,name ='email'),
    path('view_balance',views.view_balance,name='view_balance'),
     path('reset_password/',
    auth_views.PasswordResetView.as_view(template_name='password_reset.html',  success_url=reverse_lazy('password_reset_done')),
    name='reset_password'),
    path('reset_password_sent/',
    auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'),
    name='password_reset_done'),
    path('reset/<uidb64>/<token>',
    auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html',success_url=reverse_lazy('password_reset_complete')),
    name='password_reset_confirm'),
    path('reset_password_complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'),
    name='password_reset_complete'),
    
]