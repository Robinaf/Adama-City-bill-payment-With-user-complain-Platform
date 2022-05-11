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
# class LoginForm(forms.Form):
#     username = forms.CharField(
#         widget= forms.TextInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     password = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )

class CreateUserForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['username','first_name','middle_name','last_name', 'email','age','house_number','gender','password1', 'password2','role']
# class CreateCompanyAdminForm(UserCreationForm):
#     class Meta:
#         model = CompanyAdmin
#         fields = ['username','first_name','email','password1','password2','role']
