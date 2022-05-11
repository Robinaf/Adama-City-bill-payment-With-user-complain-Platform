from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *


class CreateCompanyAdminForm(UserCreationForm):
    class Meta:
        model = WaterTechnician,WaterReader
        fields = ['username','first_name','email','password1','password2','role']
