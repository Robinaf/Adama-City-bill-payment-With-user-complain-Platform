
from re import template
from django.contrib import admin
from django.urls import path,include
from django.urls import path as url
from water.admin import water_site
# from electric.admin import electric_site
from users import views
# from users.admin import admin_site
from django.contrib import admin
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/',admin.site.urls),
    # path('wateradmin/', water_site.urls),
    # path('electricadmin/',electric_site.urls),
    path('',include('users.urls')),
    path('',include('water.urls')),
    path('',include('electric.urls')),
    path('',views.index,name ='index'),
    path("login/", views.user_login, name='login'),
    path("signup/", views.registerPage, name='registerPage'),
    path('logout/',views.user_logout,name='logout'),
    path('', include('django.contrib.auth.urls')),
   


    #url('superadmin/', admin_site.urls),
    



]
