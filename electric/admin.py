from django.contrib.admin import AdminSite
from .models import Customer
from . import models
from django.contrib.admin import AdminSite
from django.contrib import admin
from . import models
from .models import *
from .models import Customer,ElectricTechnician,ElectricCustomer,ElectricReader

from django.contrib.auth.admin import UserAdmin


# # Register your models here.


class ElectricBalanceAdmin(admin.ModelAdmin):
    model = ElectricBalance

    readonly_fields = ('balance',)
    search_fields= []
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

class ElectricUserAdmin(UserAdmin):
     # readonly_fields = ('prev_reading','current_reading','amount','month','year')
     add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'password1', 'password2', 'is_active', 'is_staff',)}
         ),
    )
class ElectricReaderAdmin(admin.ModelAdmin):
     model: ElectricReader
     search_fields= [ ]
class ElectricTechnicianAdmin(admin.ModelAdmin):
     model: ElectricTechnician
     search_fields= [ ]
class ElectricAdmin(admin.ModelAdmin):
     site_header ='Electric Admin Area'
     model= ElectricCustomer,ElectricBillInfo,ElectricComplain,ElectricReader,ElectricTechnician,AssignComplain
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
class AssignComplainAdmin(admin.ModelAdmin):
     model: AssignComplain
     list_display = ('complain_id','assign_to')

class ElectricBillAdmin(admin.ModelAdmin):
     model =ElectricBillInfo
     readonly_fields = ('prev_reading','current_reading','amount',)
     list_display =('id','meter_id','prev_reading','current_reading','amount','is_paid')
     def has_change_permission(self, request, obj=None):
        return False
     def has_add_permission(self, request, obj=None):
        return False


class ElectricComplainAdmin(admin.ModelAdmin):
     model = ElectricComplain
     readonly_fields = ('id','complain','is_solved','date','meter_id','phone_number')
     # list_display = ('email', 'username', 'first_name',
     #                'is_active', 'is_staff','balance',)
     list_display =('id','meter_id','complain','date','is_solved','phone_number','assigned_to')
     # def has_change_permission(self, request, obj=None):
     #    return False
     def has_add_permission(self, request, obj=None):
        return False


# class ElectricAdminArea(AdminSite):
#      site_header='electric Admin Area'
# electric_site = ElectricAdminArea(name='ElectricAdmin')

# electric_site.register(models.ElectricCustomer)
# electric_site.register(models.ElectricEmployee)
admin.site.register(ElectricBillInfo,ElectricBillAdmin)
admin.site.register(ElectricComplain,ElectricComplainAdmin)
admin.site.register(ElectricCustomer,ElectricAdmin)
admin.site.register(ElectricBalance,ElectricBalanceAdmin)
admin.site.register(ElectricReader,ElectricUserAdmin)
admin.site.register(ElectricTechnician,ElectricUserAdmin)
admin.site.register(AssignComplain,AssignComplainAdmin)


