from django.urls import path
from water import views

urlpatterns=[
    path('addemploye',views.addemployee, name = 'addemployee'),
    path('water_reader',views.water_reader,name ='water_reader'),
    path('water_bill',views.admin_cheek_bill,name ='water_bill'),
    #path('water_admin',views.bill_generate,name='water_admin')
]