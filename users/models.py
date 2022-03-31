import email
from enum import unique
from xml.dom.minidom import CharacterData
from django.db import models
#from django.contrib.auth.models import User
from django.forms import CharField, DecimalField, EmailField
from django.contrib.auth.models import AbstractBaseUser,UserManager
#from water.models import WaterCustomer

# Create your models here.
class Customer(AbstractBaseUser):
    #user= models.OneToOneField(User,null = True, blank = True, on_delete=models.CASCADE)
    username = models.CharField(null=False,max_length=100,primary_key = True)
    first_name = models.CharField(max_length=50,null=True)
    middle_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    email =  models.EmailField(max_length=50,null=True,unique=True)
    house_number = models.IntegerField(null=True)
    gender = models.CharField(max_length=10,null=True)
    age = models.IntegerField(null=True)
    date_joined = models.DateTimeField(auto_now=True)
    #is_customer = models.BooleanField(default=True)
    #role = models.CharField(max_length= 10)

    # CHOICES = [('M','Male'),('F','Female')]
    # gender=models.CharField(label='Gender', widget=models.RadioSelect(choices=CHOICES))
    objects = UserManager()
   
    # class Meta:
    #     db_table = "customer"
    def __str__(self):
        return self.first_name
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'
   




