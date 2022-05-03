# from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import *
from .models import Customer
from django.contrib.auth.admin import UserAdmin



class CompanyAdminConfig(UserAdmin):
    site_header = 'My Super Administration'
    model =CompanyAdmin,
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
    site_header = 'My Super Administration'
    model =Customer
    search_fields = ('email', 'username', 'first_name',)
    search_fields = ('email', 'username', 'first_name',)
    list_filter = ('email', 'username', 'first_name','last_name', 'is_active', 'is_staff',)
    #ordering = ('-date_joined',)
    list_display = ('email', 'username', 'first_name',
                    'is_active', 'is_staff','balance',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name','balance', 'password1', 'password2', 'is_active', 'is_staff','house_number')}
         ),
    )
    readonly_fields=('date_joined',)
    exclude_fields= ('is_superuser',)
    
# admin_site = UserAdminConfig(Account,'admin_site')
admin.site.register(CompanyAdmin,CompanyAdminConfig)

admin.site.register(Customer,CustomerAdminConfig)


# admin.site.register(CompanyAdmin)

# Register your models here.
