from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(null=False,max_length=100,primary_key = True)#on_delete=models.CASCADE, to=WaterCustomer)
    f_name = models.CharField(max_length=50,null=True)
    m_name = models.CharField(max_length=50,null=True)
    l_name = models.CharField(max_length=50,null=True)
    email =  models.EmailField(max_length=50,null=True)
    house_no = models.IntegerField(null=True)
    gender = models.CharField(max_length=10,null=True)
    age = models.IntegerField(null=True)
    class Meta:
        db_table = "customer"