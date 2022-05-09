from django.urls import path
from water import views

urlpatterns=[
    path('water_reader',views.water_reader,name ='water_reader'),
    path('complain',views.complain,name='complain'),
    path('water_admin',views.water_admin,name='water_admin'),

]