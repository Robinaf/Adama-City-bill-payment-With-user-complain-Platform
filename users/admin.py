from django.contrib.admin import AdminSite
from .models import *


class MyAdminSite(AdminSite):
    site_header = 'My Super Administration'

admin_site = MyAdminSite(name='myadmin')
admin_site.register(CompanyAdmin)
# admin.site.register(Customer)
# admin.site.register(CompanyAdmin)

# Register your models here.
