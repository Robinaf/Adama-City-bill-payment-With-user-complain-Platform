from django.contrib.admin import AdminSite
from .models import Customer
from . import models

# # Register your models here.
class ElectricAdminArea(AdminSite):
     site_header='electric Admin Area'
electric_site = ElectricAdminArea(name='ElectricAdmin')

electric_site.register(models.ElectricCustomer)
electric_site.register(models.ElectricEmployee)