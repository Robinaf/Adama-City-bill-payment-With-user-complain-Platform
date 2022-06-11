from django.contrib.admin import AdminSite
from django.contrib import admin
from . import models
from .models import *
from .models import Customer,WaterTechnician,WaterCustomer,WaterReader

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

#     readonly_fields = ('balance',)
    search_fields= []
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
   
class WaterComplainAdmin(admin.ModelAdmin):
     model=WaterComplain
     readonly_fields = ('complain',)
class WaterUserAdmin(UserAdmin):
     # readonly_fields = ('prev_reading','current_reading','amount','month','year')
     add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'password1', 'password2', 'is_active', 'is_staff',)}
         ),
    )

class WaterAdmin(admin.ModelAdmin):
     site_header ='Water Admin Area'
     model= WaterCustomer,WaterBillInfo,WaterComplain,WaterReader,WaterTechnician
     # list_display = ('meter_id', 'username',
     #                )
     add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('employee_id','email', 'username', 'first_name', 'password1', 'password2','is_active', 'is_staff',),

            'Other_info': ('employee_id',)
            }
         ),
    )
     list_display =('meter_id','username',)
class WaterBillAdmin(admin.ModelAdmin):
     model =WaterBillInfo
     readonly_fields = ('prev_reading','current_reading','amount',)
     list_display =('id','meter_id','prev_reading','current_reading','amount','is_paid')
     def has_change_permission(self, request, obj=None):
        return False
     def has_add_permission(self, request, obj=None):
        return False
class WaterReaderAdmin(admin.ModelAdmin):
     model: WaterReader
     search_fields= [ ]

class WaterComplainAdmin(admin.ModelAdmin):
     model = WaterComplain
     readonly_fields = ('id','complain','is_solved','date','meter_id','phone_number')
     # list_display = ('email', 'username', 'first_name',
     #                'is_active', 'is_staff','balance',)
     list_display =('id','meter_id','complain','date','is_solved','phone_number','assigned_to')
     # def has_change_permission(self, request, obj=None):
     #    return False
     def has_add_permission(self, request, obj=None):
        return False

class AssignComplainAdmin(admin.ModelAdmin):
     model: AssignComplain
     list_display = ('complain_id','assign_to')




class WaterAdminArea(AdminSite):
     model=WaterComplain
     site_header='Water Admin Area'
     readonly_fields = ('prev_reading','current_reading','amount','complain')
     list_filter=('Water_Technician','Water_Reader')

water_site = WaterAdminArea(name='WaterAdmin')
# water_site.register(WaterCustomer)
# water_site.register(WaterBillInfo)
# water_site.register(WaterComplain)
# water_site.register(WaterTechnician)
# water_site.register(WaterReader,WaterAdmin)
admin.site.register(WaterCustomer,WaterAdmin)
admin.site.register(WaterReader,WaterUserAdmin)
admin.site.register(WaterTechnician,WaterUserAdmin)
admin.site.register(WaterBillInfo,WaterBillAdmin)
admin.site.register(WaterBalance,WaterBalanceAdmin)
admin.site.register(WaterComplain,WaterComplainAdmin)
admin.site.register(AssignComplain,AssignComplainAdmin)




