from django.shortcuts import render

# Create your views here.
def addemployee(request):
    return render(request,'admin_home.html')