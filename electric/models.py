from django.db import models
from users.models import Customer
from users.models import *
from django.utils import timezone
from datetime import datetime, timedelta 

# Create your models here.

class ElectricTechnician(Account):
    employee_id = models.IntegerField(null=True)
    # username=models.OneToOneField(Account,null=False,max_length=100,on_delete=models.CASCADE)
    class Meta:
        db_table = "electric_technician"
    def __str__(self):
        return str(self.username)
class ElectricReader(Account):
    employee_id=models.IntegerField(null=True)
    # username=models.OneToOneField(Account,null=False,max_length=100,on_delete=models.CASCADE)
    class Meta:
        db_table ="electric_reader"
    def __str__(self):
        return str(self.username)
class ElectricCustomer(models.Model):
    meter_id=models.IntegerField(primary_key=True)
    username = models.ForeignKey(null=False,max_length=100, on_delete=models.CASCADE, to = Customer)
    class Meta:
        db_table = "electric_customer"
    def __str__(self):
        return str(self.meter_id )
    def __unicode__(self):
        return self.meter_id
class ElectricEmployee(Account):
    employee_id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = "electric_employee"
class ElectricBillInfo(models.Model):
    meter_id=models.ForeignKey(on_delete=models.CASCADE, to=ElectricCustomer)
    prev_reading = models.DecimalField(max_digits=50,decimal_places=2)
    current_reading = models.DecimalField(max_digits=50,decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(max_digits=50,decimal_places=2,null=True)
    is_paid = models.BooleanField(max_length=50,default=False)
    deadline =models.DateTimeField(default=timezone.now() + timedelta(minutes=3))
    class Meta:
        db_table = "electricbillinfo"

class ElectricComplain(models.Model):
    meter_id = models.ForeignKey(on_delete=models.CASCADE, to=ElectricCustomer)
    complain = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    is_solved = models.BooleanField(max_length=50,default=False )
    phone_number=models.IntegerField(null=True)
    assigned_to =models.ForeignKey(ElectricTechnician,null=True,max_length=100, on_delete=models.CASCADE,)
    tec_reported=models.BooleanField(max_length=50,default=False)

    class Meta:
        db_table = "electric_complain"
    def __str__(self):
        return str(self.meter_id)
class AssignComplain(models.Model):
    complain_id=models.ForeignKey(on_delete = models.CASCADE , to=ElectricComplain)
    assign_to =models.ForeignKey(on_delete=models.CASCADE, to =ElectricTechnician)
    def __str__(self):
        return str(self.assign_to)
class ElectricBalance(models.Model):
     balance = models.DecimalField(max_digits=50,default=0.00,decimal_places=2)
     def __str__(self):
        return str(self.balance)

