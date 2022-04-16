from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User




class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['username','first_name','middle_name','last_name', 'email','age','house_number','gender','password1', 'password2','role']
class CreateCompanyAdminForm(UserCreationForm):
    class Meta:
        model = CompanyAdmin
        fields = ['username','first_name','email','password1','password2','role']