from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .forms import CreateUserForm
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
@unauthenticated_user
def registerPage(request):
    form = CreateUserForm(request.POST or None)

    # if request.method == "GET":
    #     return form

    if request.method == "POST":
        # form = CreateUserForm()
        if form.is_valid():
            Account.role = 'Customer'
            user=form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, "Account sucessfully created for " + username)
            return redirect('login')
        else:
            print("Not registered")
            print(form.errors)

    context = {'form': form}
    return render(request, 'signup.html', context)
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            print("In Post Method...!!!")
            usern = request.POST.get("username")
            pswd = request.POST.get("password")
            user_obj = authenticate(username=usern, password=pswd)
            if user_obj:
                login(request,user_obj)
                return redirect('home')
            return HttpResponse('Invalid Credentials...!!!')
        return render(request, 'login.html')
    else:
        return redirect('home')
  
    
@login_required
def home(request):
  return render(request, 'home.html')
  # Logout view 
def user_logout(request):
   logout(request)
   return redirect('login')

