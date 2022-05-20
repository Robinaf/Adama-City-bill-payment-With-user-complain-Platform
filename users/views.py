from tokenize import group
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .forms import CreateUserForm
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .models import *
from .forms import CreateUserForm
#from .models import Customer
#from .filters import OrderFilter
from .decorators import unauthenticated_user, allowed_users, admin_only
from water.models import *


# Create your views here.
# def signup(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         #middle_name = request.POST['middle_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         email = request.POST['email']
#         #house_number = request.POST['house_number']
#         #age = request.POST['age']
#         user = User.objects.create_user(first_name=first_name,last_name=last_name,
#       username=username,
#         password1=password1,password2=password2,email=email)
#         user.save();
#         print('user created')
#         return redirect('/')

#     else: 
#         return render(request,'signup.html') 
def  index(request):
    return render(request,'index.html')
@unauthenticated_user
def registerPage(request):
    form = CreateUserForm(request.POST or None)

    # if request.method == "GET":
    #     return form

    if request.method == "POST":
        # form = CreateUserForm()
        if form.is_valid():
            # Account.role = 'Customer'
            user=form.save(commit=False)
            user.role = 7
            user.save()
            username = form.cleaned_data.get('username')
            group= Group.objects.get(name='customer')
            user.groups.add(group)
            messages.success(
                request, "Account sucessfully created for " + username)
            return redirect('login')
        else:
            print("Not registered")
            print(form.errors)
            return HttpResponse(form.errors)

    context = {'form': form}
    return render(request, 'signup.html', context)

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            print("In Post Method...!!!")
            usern = request.POST.get("username")
            pswd = request.POST.get("password")
            user = authenticate(username=usern, password=pswd)
            if user.groups.exists():
                a=user.groups.all()[0].name
                if a == 'customer':
                    login(request,user)
                    return redirect('home',)
                elif a == 'water-reader':
                    login(request,user)
                    return redirect('water_reader')
                elif a=='water_technician':
                     login(request,user)
                     return redirect('water_technician')
                # else:
                #     return render(request,'Account/login.html')
            else:
                messages.warning(request, 'Username or password is not correct !!')
                return redirect(request,'login.html')
            

                       
           
        return render(request, 'login.html')
    # else:
    #     return redirect('home')
  
    
@login_required
def home(request):
  return render(request, 'customer/customerbase.html')
  # Logout view
  # 
  #  
def user_logout(request):
   logout(request)
   return redirect('login')
######################## Payment##########################

       
        

       





