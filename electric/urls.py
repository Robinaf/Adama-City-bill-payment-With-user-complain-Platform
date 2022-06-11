
from django.urls import path
from . import views

urlpatterns=[
   
    # path('', views.home, name = 'electrical_admin'),
    path('electricreaderpage',views.electricreaderpage,name='electricreaderpage'),
    path('electriccomplain/',views.electriccomplain,name='electriccomplain'),
    path('electric_reader/',views.electric_reader,name='electric_reader'),
    path('electric_technician',views.electric_technician,name ='electric_technician'),
    path('viewelectricbill/',views.viewelectricbill,name='viewelectricbill'),
    path('viewelectriccomplain/',views.viewelectriccomplain,name='viewelectriccomplain'),
    path('electricpayment/',views.electricpayment,name='electricpayment'),
    path('elec_assigned_complain',views.elec_assigned_complain,name='elec_assigned_complain'),
    path('e_ispaid/<int:pk>/',views.e_ispaid,name='e_ispaid'),

   
    
]