from django.shortcuts import render
from multiprocessing import context
from pyexpat import model
from django.db.models import IntegerField
from django.db.models.functions import Cast
from django.shortcuts import render,redirect
from pymysql import NULL
from .models import ElectricBalance, ElectricBillInfo,ElectricCustomer,ElectricComplain, ElectricTechnician
from django.http import HttpResponse
from users.models import Customer,Account
#from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import requests


# Create your views here.
def home(request):
    return render(request,'electric_admin/electric_dashboard.html',)


def electric_reader(request):
    x=request.user.username
    print(x)

    if request.method=="POST":
        
        meter_id_id =request.POST.get('meter_id_id')
        
        current_reading = float(request.POST.get('current_reading'))
        wc = ElectricCustomer.objects.get(meter_id=meter_id_id)
        try:
            
            prev_read = float(ElectricBillInfo.objects.filter(meter_id=meter_id_id).order_by('-date')[0].current_reading)          
            print(prev_read)
        except:
            prev_read = 0
        ################################################
         # when reading is less than 50
        #################################################
        if current_reading-prev_read <=0:
             print('current cannot be less than previous reading')
             messages.warning(request, 'Incorrect Current Reading')
             return render(request,'electric_reader/electric_reader.html')

        elif current_reading-prev_read <= 50:
            print('is less tan 50')

            new_bill = ElectricBillInfo.objects.create(
                meter_id_id = wc.meter_id,
                current_reading=float(current_reading), 
                amount=(current_reading-prev_read)*0.2730, 
                prev_reading=prev_read,
               

            )
         ################################################
         # when reading is less than 100
        #################################################
        elif current_reading-prev_read <= 100:
            print('is less tan 100')
            new_bill = ElectricBillInfo.objects.create(
                meter_id_id = wc.meter_id,
                current_reading=float(current_reading), 
                amount=(current_reading-prev_read)*0.6644, 
                prev_reading=prev_read,
               

            )
        elif current_reading-prev_read <= 200:
            print('is less tan 200')
            new_bill = ElectricBillInfo.objects.create(
                meter_id_id = wc.meter_id,
                current_reading=float(current_reading), 
                amount=(current_reading-prev_read)*1.3436, 
                prev_reading=prev_read,
                

            )
        elif current_reading < prev_read:
            print('current cannot be less than previous reading')
        else:
            print(current_reading)
            print(prev_read)
            pass
               
        messages.success(request, 'You sent the data to server successfully')
        return render (request,'electric_reader/electricreaderhome.html')
    
    return render(request,'electric_reader/electric_reader.html')
##########################Electric Complain ############
def electriccomplain(request):
    if request.method=="POST":
        phone_number=request.POST.get('phone_number')
        complain=request.POST.get('complain')
        if complain ==NULL:
            messages.warning(request,'your complain is empty')
            return(request,'customer/electriccomplain.html')
        else:
            x=request.user.username
            y=ElectricCustomer.objects.get(username=x)
            m=y.meter_id
            complaindetail = ElectricComplain(
            meter_id_id =m,
             complain=complain,
             phone_number=phone_number
                    )
            complaindetail.save()
            messages.success(request,'Complain sent successfully')
            return render(request,'customer/viewelectriccomplain.html')
    return render(request,'customer/electriccomplain.html',)
def viewelectricbill(request):
    x=request.user.username
    print(x)
    y=ElectricCustomer.objects.get(username=x)
    m=y.meter_id
    billinfo=ElectricBillInfo.objects.filter(meter_id_id = y)
    context = {
             'billinfo': billinfo
            
        }
   
    return render(request,'customer/viewelectricbill.html',context)
def viewelectriccomplain(request):
    x=request.user.username
    print(x)
    y= ElectricCustomer.objects.get(username=x)
    electriccomplaindata = ElectricComplain.objects.filter(meter_id_id =y)
    
    context = {
        'electriccomplaindata':electriccomplaindata
    }
    
    return render(request,'customer/viewelectriccomplain.html',context)
def electricpayment(request):
    if request.method == "POST":
        x=request.user.username      
        c=ElectricCustomer.objects.get(username=x)
        mm=c.meter_id
        customer =Customer.objects.get(username=x)
        y=customer.balance
        print(y)
        billinfo =ElectricBillInfo.objects.get(meter_id_id =c)
        amountt= ElectricBillInfo.objects.filter(meter_id_id=mm).order_by('-date')[0].amount
        print(amountt)
        status = ElectricBillInfo.objects.filter(meter_id_id=mm).order_by('-date')[0].is_paid
        electricbalance =ElectricBalance.objects.get(id =1)
        print(electricbalance.balance)


        
        print(status)
        payed =y-amountt
        
        print(payed)
        if status == False:
            if payed>=0: 
                electricbalance.balance += amountt             
                billinfo.is_paid=True
                customer.balance =payed
                billinfo.save()
                customer.save()
                electricbalance.save()
                messages.success(
                request, "You paid successfully ")
                return render(request,'customer/viewelectricbill.html')
                


                # billinfo=WaterBillInfo( 
                #     is_paid =True)
                # cus=Customer(balance=payed)
                # billinfo.save()

                # cus.save() 
        messages.warning(request,'It is already paid')
        return render(request,'customer/viewelectricbill.html')

        
    
    return render(request, 'customer/payment.html')

def electric_technician(request):
    x=request.user.username
    print(x)
    assignn=ElectricComplain.objects.filter(assigned_to_id=x )
    context={
        'assignn':assignn
    }
    return render(request,'electric_technician/assigned_complain.html',context)
    ############ electric reader page############  
def electricreaderpage(request):
    return render(request,'electric_reader/electricreaderhome.html')
############ Electric technician check assigned complain#####

def elec_assigned_complain(request):
    x=request.user.username
    print(x)
    # y= ElectricTechnician.objects.get(username=x)
    
    assignn=ElectricComplain.objects.filter(assigned_to_id=x )
   
    #print(assign)
    # print(assign.id)
    context={
        'assignn':assignn
    }
    return render(request,'electric_technician/assigned_complain.html',context) 
     ######Electric payment #########
def e_ispaid(request,pk):
    x=request.user.username
    # y=x.balance
    customer =Customer.objects.get(username=x)
    y=customer.balance
    pay=ElectricBillInfo.objects.get(pk=pk)
    electricbalance =ElectricBalance.objects.get(id =1)
    billinfo=ElectricBillInfo.objects.filter(meter_id_id = y)
    amountt=pay.amount
    
    if pay.is_paid ==False:
        electricbalance.balance+=amountt
        payed =y-amountt
        pay.is_paid=True
        customer.balance=payed
        customer.save()
        electricbalance.save()
        pay.save()
        context={
            'billinfo':billinfo
        }
        messages.success(request,"You paid successfully")
        return render(request,'customer/viewelectricbill.html',context)
    else:
        messages.warning(request,"It is paid before")
        return render(request,'customer/viewelectricbill.html')
def solve_complain(request,pk):
    x=request.user.username
    y= ElectricCustomer.objects.get(username=x)
    updatemytabel=ElectricComplain.objects.get(pk=pk)
    electriccomplaindata = ElectricComplain.objects.filter(meter_id_id =y)
    assigned=updatemytabel.assigned_to_id
    solved=updatemytabel.is_solved
    if solved==True:
        messages.warning(request,'It is solved before')
        return render(request,'customer/viewelectriccomplain.html')
        
    if assigned==None:
        messages.warning(request,'It is not assigned yet')
        return render(request,'customer/viewelectriccomplain.html')
            
    updatemytabel.is_solved=True
    updatemytabel.save()
    context = {
        'electriccomplaindata':electriccomplaindata
          }
        
    messages.success(request,'You  confirmed the solution successfully')
    return render(request,'customer/viewelectriccomplain.html',context)