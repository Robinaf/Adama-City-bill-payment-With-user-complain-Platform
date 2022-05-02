from django.urls import path
from water import views

urlpatterns=[
    path('addemploye',views.addemployee, name = 'addemployee'),
    path('water_reader',views.water_reader,name ='water_reader')
]