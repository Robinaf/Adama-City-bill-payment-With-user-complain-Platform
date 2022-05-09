# from email import message
# from pyexpat import model
# from turtle import title
# from unittest.util import _MAX_LENGTH
from django.db import models
from users.models import Customer
from users.models import *
from django.utils import timezone

# Create your models here.
class WaterCustomer(models.Model):
    meter_id=models.IntegerField(primary_key=True)
    username = models.ForeignKey(null=False,max_length=100, on_delete=models.CASCADE, to = Customer)
    
    class Meta:
        db_table = "water_customer"
    def __str__(self):
        return str(self.username.first_name )+"     "+str(self.username.last_name)

    # def __str__(self):
    #     return self.title
class WaterEmployee(Account):
    employee_id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = "water_employee"
class WaterBillInfo(models.Model):
    meter_id=models.ForeignKey(on_delete=models.CASCADE, to=WaterCustomer)
    prev_reading = models.DecimalField(max_digits=50,decimal_places=2,default=0)
    current_reading = models.DecimalField(max_digits=50,decimal_places=2)
    date =models.DateField(default=timezone.now)
    is_paid = models.BooleanField(max_length=50,default=False)
    Month_choice = [('january','january'),('february','february'),('march','march'),('april','april'),
    ('may','may'),('june','june'),('july','july'),('august','august'),('september','september'),('october','october'),('november','november'),('december','december')]
    month=models.CharField(max_length=50,choices=Month_choice,blank=True,null = True)
    year = models.IntegerField(null=True)
    amount = models.DecimalField(max_digits=50,decimal_places=2,null=True)
    
    class Meta:
        db_table = "waterbillinfo"
    def __str__(self):
        return str(self.meter_id)

class WaterComplain(models.Model):
    meter_id = models.ForeignKey(on_delete=models.CASCADE, to=WaterCustomer)
    complain = models.TextField()
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=50,null=True,default='not solved')
    
    class Meta:
        db_table = "water_complain"
    def __str__(self):
        return str(self.meter_id)
class WaterBalance(models.Model):
    balance = models.DecimalField(max_digits=50,default=0.00,decimal_places=2)
    def __str__(self):
        return str(self.balance)
