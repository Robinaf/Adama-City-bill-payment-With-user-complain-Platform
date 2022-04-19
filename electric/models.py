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
class ElectricBillInfo(models.Model):
    meter_id=models.ForeignKey(on_delete=models.CASCADE, to=ElectricCustomer)
    prev_reading = models.DecimalField(max_digits=50,decimal_places=2)
    current_reading = models.DecimalField(max_digits=50,decimal_places=2)
    date =models.DateField(null=True)
    status = models.CharField(max_length=50,null=True)
    class Meta:
        db_table = "electricbillinfo"

class ElectricComplain(models.Model):
    meter_id = models.ForeignKey(on_delete=models.CASCADE, to=ElectricCustomer)
    complain = models.TextField()
    date = models.DateField(null=True)
    status = models.CharField(max_length=50,null=True)
    class Meta:
        db_table = "electric_complain"
