from django.urls import path
from water import views

urlpatterns=[
    path('addemploye',views.addemployee, name = 'addemployee')
]