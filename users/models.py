import email
from enum import unique
from xml.dom.minidom import CharacterData
from django.db import models
#from django.contrib.auth.models import User
from django.forms import CharField, DecimalField, EmailField
from django.contrib.auth.models import AbstractBaseUser,UserManager,PermissionsMixin
#from water.models import WaterCustomer

# Create your models here.
# class Role(models.Model):
#     Water_Admin =1
#     Electric_Admin = 2
#     Water_Reader = 3
#     Water_Technician = 4
#     Electric_Reader = 5
#     Electric_Technician = 6
#     Customer = 7
#     ROLE_CHOICES = ((1,'Water_Admin'),(2,'Electric_Admin'),(3,'Water_Reader'),(4,'Water_Technician'),(5,'Electric_Reader'),(6,'Electric_Technician'),(7,'Customer'))
#     id = models.PositiveIntegerField(choices=ROLE_CHOICES,primary_key=True)
#     def __str__(self):
#       return self.get_id_display()
class Account(AbstractBaseUser,PermissionsMixin):
    #user= models.OneToOneField(User,null = True, blank = True, on_delete=models.CASCADE)
    username = models.CharField(null=False,max_length=100,primary_key = True)
    first_name = models.CharField(max_length=50,null=True)
    middle_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    email =  models.EmailField(max_length=50,null=True)
    #gender = models.CharField(max_length=10,null=True)
    #age = models.IntegerField(null=True)
    date_joined = models.DateTimeField(auto_now=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    #is_human = models.BooleanField(default=True)
    #is_customer = models.BooleanField(default=False)
    
    
    #roles = models.ManyToManyField(Role)
    #role = models.CharField(max_length= 10)

    ROLE_CHOICES = [(1,'Water_Admin'),(2,'Electric_Admin'),(3,'Water_Reader'),(4,'Water_Technician'),(5,'Electric_Reader'),(6,'Electric_Technician'),(7,'Customer')]
    role=models.PositiveSmallIntegerField(choices=ROLE_CHOICES,blank=True,null = True)
    objects = UserManager()
   
    # class Meta:
    #     db_table = "customer"
    def __str__(self):
        return self.first_name + "  "+ self.middle_name
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'
class Customer(Account):
    gender = models.CharField(max_length=10,null=True)
    age = models.IntegerField(null=True)
    is_customer = models.BooleanField(default=False)
    house_number = models.IntegerField(null=True)

    


class CompanyAdmin(Account):
    company_name = models.CharField(max_length=100)









