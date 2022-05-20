from django.urls import path
from water import views

urlpatterns=[
    path('water_reader',views.water_reader,name ='water_reader'),
    path('complain',views.complain,name='complain'),
    path('water_admin',views.water_admin,name='water_admin'),
    path('water_technician',views.water_technician, name='water_technician'),
    path('reportsolved',views.reportsolved,name='reportsolved'),
    path('viewbill',views.viewbill,name='viewbill'),
    path('waterpayment',views.waterpayment, name='waterpayment'),

]