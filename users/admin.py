# from django.contrib.admin import AdminSite
from django.contrib.admin import ModelAdmin
from dataclasses import fields
from django.contrib import admin
from .models import *
from .models import Customer
from django.contrib.auth.admin import UserAdmin



class CompanyAdminConfig(UserAdmin):
    site_header = 'My Super Administration'
    search_fields = ('email', 'username', 'first_name',)
    search_fields = ('email', 'username', 'first_name',)
    list_filter = ('email', 'username', 'first_name','last_name', 'is_active', 'is_staff',)
    #ordering = ('-date_joined',)
    list_display = ('email', 'username', 'first_name',
                    'is_active', 'is_staff',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'password1', 'password2', 'is_active', 'is_staff',)}
         ),
    )
    readonly_fields=('date_joined',)
class CustomerAdminConfig(UserAdmin):
    # def has_add_permission(self, request, obj=None):
    #     return False
    # def has_change_permission(self, request, obj=None):
    #     return False
    site_header = 'My Super Administration'
    model =Customer
    search_fields = ('email', 'username', 'first_name',)
    search_fields = ('email', 'username', 'first_name',)
    list_filter = ('email', 'username', 'first_name','last_name', 'is_active', 'is_staff',)
    #ordering = ('-date_joined',)
    list_display = ('email', 'username', 'first_name',
                    'is_active', 'is_staff','balance',)
    
    
    
    readonly_fields=('date_joined','last_login')
    exclude_fields= ('is_superuser',)
    fieldsets = (
    (None, {'fields': ('username', 'password')}),

    (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),        
    (('Permissions'), {'fields': ('is_active',  'groups', 'user_permissions')}),
                                   

    (('Important dates'), {'fields': ('last_login', 'date_joined',)}),
    (('Additional info'),{'fields': ('balance','house_number')}),

    )


    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('gender', 'houser_number', 'balance','balance')}
    #      ),)
  
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'username', 'first_name','balance', 'password1', 'password2', 'is_active', 'is_staff','house_number')}
    #      ),)
  
# class CustomerAdmin(models.ModelAdmin):
#     fields =[ ]
    
# admin_site = UserAdminConfig(Account,'admin_site')
# admin.site.register(CompanyAdmin,CompanyAdminConfig)

admin.site.register(Customer,CustomerAdminConfig)


# admin.site.register(CompanyAdmin)

# Register your models here.
