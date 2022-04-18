from django.contrib.admin import AdminSite
from .models import Customer
from . import models

# # Register your models here.
class WaterAdminArea(AdminSite):
     site_header='Water Admin Area'
water_site = WaterAdminArea(name='WaterAdmin')

water_site.register(models.WaterCustomer)