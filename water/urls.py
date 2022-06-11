from django.urls import path
from water import views

urlpatterns=[
   
    path('water_assigned_complain',views.water_assigned_complain,name='water_assigned_complain'),
    path('water_reader',views.water_reader,name ='water_reader'),
    path('complain',views.complain,name='complain'),
    path('water_admin',views.water_admin,name='water_admin'),
    path('reporwatertsolved',views.reportwatersolved,name='reportwatersolved'),
    path('viewwaterbill',views.viewwaterbill,name='viewwaterbill'),
    path('waterpayment',views.waterpayment, name='waterpayment'),
    path('viewwatercomplain',views.viewwatercomplain,name='viewwatercomplain'),
    path('report',views.report,name='report'),
    path('assignedwatercomplain',views.assignedwatercomplain,name='assignedwatercomplain'),
    path('new/<int:pk>/',views.compeln_ditel,name='new'),
    path('waterreaderpage',views.waterreaderpage,name='waterreaderpage'),
    path('ispaid/<int:pk>/',views.ispaid,name='ispaid'),
    path('wateryenepay',views.wateryenepay, name='wateryenepay'),
    path('success',views.success,name='success'),
    path('cancel',views.cancel, name='cancel'),
    path('ipn/', views.ipn, name='ipn'),

]