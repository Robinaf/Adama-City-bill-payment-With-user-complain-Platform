from django.db import models
from users.models import Customer
from users.models import * 

# Create your models here.
class ElectricCustomer(models.Model):
    meter_id=models.IntegerField(primary_key=True)
    username = models.ForeignKey(null=False,max_length=100, on_delete=models.CASCADE, to = Customer)
    class Meta:
        db_table = "electric_customer"
class ElectricEmployee(Account):
    employee_id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = "electric_employee"