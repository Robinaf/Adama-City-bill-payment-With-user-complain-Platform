from django.contrib.admin import AdminSite
from django.contrib import admin
from . import models
from .models import *
from .models import Customer,WaterEmployee,WaterCustomer

from django.contrib.auth.admin import UserAdmin

# # Register your models here.
# class UserAdminConfig(UserAdmin,AdminSite):
#     site_header = 'Water Admin Area'
#     model =WaterEmployee
    
#     search_fields = ('email', 'username', 'first_name',)
#     search_fields = ('email', 'username', 'first_name',)
#     list_filter = ('email', 'username', 'first_name','last_name', 'is_active', 'is_staff')
#     #ordering = ('-date_joined',)
#     list_display = ('email', 'username', 'first_name',
#                     'is_active', 'is_staff')
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'username', 'first_name', 'password1', 'password2', 'is_active', 'is_staff',)}
#          ),
#     )
#     readonly_fields=('date_joined',)
# water_site = UserAdminConfig(WaterEmployee,'water_site')
# water_site.register(WaterEmployee,UserAdminConfig)

class WaterBalanceAdmin(admin.ModelAdmin):
    model = WaterBalance
    readonly_fields = ('balance',)

class WaterUserAdmin(UserAdmin):
     readonly_fields = ('prev_reading','current_reading','amount','month','year')

class WaterAdminArea(AdminSite):
     site_header='Water Admin Area'
     readonly_fields = ('prev_reading','current_reading','amount','month','year')
     list_filter=('Water_Technician','Water_Reader')
water_site = WaterAdminArea(name='WaterAdmin')
water_site.register(WaterCustomer)
water_site.register(WaterEmployee)
water_site.register(WaterBillInfo)
#admin.site.register(WaterBillInfo,WaterUserAdmin)
admin.site.register(WaterBalance,WaterBalanceAdmin)
