from django.urls import path
from water import views

urlpatterns=[
    path('water_reader',views.water_reader,name ='water_reader'),
    path('complain',views.complain,name='complain'),
    path('water_admin',views.water_admin,name='water_admin'),
    path('water_technician',views.totalwatercomplain, name='water_technician'),
    path('reporwatertsolved',views.reportwatersolved,name='reportwatersolved'),
    path('viewwaterbill',views.viewwaterbill,name='viewwaterbill'),
    path('waterpayment',views.waterpayment, name='waterpayment'),
    path('viewwatercomplain',views.viewwatercomplain,name='viewwatercomplain'),
    path('report',views.report,name='report'),
    path('totalwatercomplain',views.totalwatercomplain,name='totalwatercomplain'),
    path('new/<int:pk>/',views.compeln_ditel,name='new'),
    path('ispaid/<int:pk>/',views.ispaid,name='ispaid'),
    path('wateryenepay',views.wateryenepay, name='wateryenepay'),
    path('success',views.success,name='success'),
    path('cancel',views.cancel, name='cancel'),
    path('ipn/', views.ipn, name='ipn'),

]