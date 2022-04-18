
from django.contrib import admin
from django.urls import path,include
from django.urls import path as url
from water.admin import water_site
from users import views
from users.admin import admin_site
from django.contrib import admin


urlpatterns = [
    #path('admin/',admin.site.urls),
    path('wateradmin/', water_site.urls),
    path('',include('users.urls')),
    path("login/", views.user_login, name='login'),
    path("signup/", views.registerPage, name='registerPage'),
    path('logout/',views.user_logout,name='logout'),
    url(r'^myadmin/', admin_site.urls),
]
