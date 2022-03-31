from django.db import models
from users.models import Customer

# Create your models here.
# class Customer(models.Model):
#     username = models.CharField(null=False,max_length=100,primary_key = True)#on_delete=models.CASCADE, to=WaterCustomer)
#     f_name = models.CharField(max_length=50,null=True)
#     m_name = models.CharField(max_length=50,null=True)
#     l_name = models.CharField(max_length=50,null=True)
#     email =  models.EmailField(max_length=50,null=True)
#     house_no = models.IntegerField(null=True)
#     gender = models.CharField(max_length=10,null=True)
#     age = models.IntegerField(null=True)
#     class Meta:
#         db_table = "customer"

class WaterCustomer(models.Model):
    meter_id=models.IntegerField(primary_key=True)
    username = models.ForeignKey(null=True,max_length=100,on_delete=models.CASCADE, to=Customer)
   
    # def __str__(self):
    #     return self.meter_id
    class Meta:
        db_table = "water_customer"

class WaterBillInfo(models.Model):
    meter_id=models.ForeignKey(on_delete=models.CASCADE, to=WaterCustomer)
    prev_reading = models.DecimalField(max_digits=50,decimal_places=2)
    current_reading = models.DecimalField(max_digits=50,decimal_places=2)
    date =models.DateField(null=True)
    status = models.CharField(max_length=50,null=True)
    class Meta:
        db_table = "billinfo"
class Complain(models.Model):
    meter_id = models.ForeignKey(on_delete=models.CASCADE, to=WaterCustomer)
    complain = models.TextField()
    date = models.DateField(null=True)
    status = models.CharField(max_length=50,null=True)
    class Meta:
        db_table = "water_complain"