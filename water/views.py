from ast import Assign
from multiprocessing import context
from pyexpat import model
from django.db.models import IntegerField
from django.db.models.functions import Cast
from django.shortcuts import render,redirect
# from pymysql import NULL
from .models import WaterBalance, WaterBillInfo,WaterCustomer,WaterComplain,WaterReader,WaterTechnician
from django.http import HttpResponse
from users.models import Customer
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import requests
from datetime import datetime, timedelta
from electric.models import *


# Create your views here.
def water_admin(request):
    wc=WaterCustomer.objects.all()

    return render(request,'water_admin/index.html',{'WaterCustomer':wc})
@login_required
def water_reader(request):


    if request.method=="POST":
        
        meter_id_id =request.POST.get('meter_id_id')
        
        current_reading = float(request.POST.get('current_reading'))
       
        # ww=bb.meter_id
        # x=request.user.username
        # y=WaterCustomer.objects.get(username=x)
        # m=y.meter_id
        
        month = request.POST.get('month')
        year = request.POST.get('year')
        # bb=WaterBillInfo.objects.get(meter_id_id=meter_id_id)
        # prev =bb.prev_reading
        
        if WaterCustomer.objects.filter(meter_id=meter_id_id).exists():
            wc = WaterCustomer.objects.get(meter_id=meter_id_id)

            try:
            # prevv_read = WaterBillInfo.objects.filter(meter_id=meter_id_id).order_by('-date')[0]
            # prev_read=int(prevv_read.current_reading)
                prev_read = float(WaterBillInfo.objects.filter(meter_id=meter_id_id).order_by('-date')[0].current_reading)
            # prevv_read = float(WaterBillInfo.objects.filter(meter_id=meter_id_id))
            # prev_read =prevv_read.order_by('-date')[0].current_reading
                print(prev_read)
            except:
                prev_read = 0
        ################################################
         # when reading is less than 50
        #################################################

            if current_reading-prev_read <=0:
                print('current cannot be less than previous reading')
                messages.warning(request, 'Incorrect Current Reading')
                return render(request,'water_reader/water_reader.html')
            
        

            elif current_reading-prev_read <= 50:
                print('is less tan 50')
            

                new_bill = WaterBillInfo.objects.create(
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
               
           
                new_bill = WaterBillInfo.objects.create(
                meter_id_id = wc.meter_id,
                current_reading=float(current_reading), 
                amount=(current_reading-prev_read)*0.6644, 
                prev_reading=prev_read,
               

                    )
            elif current_reading-prev_read <= 200:
                 print('is less tan 200')
           
                 new_bill = WaterBillInfo.objects.create(
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
            return render (request,'water_reader/waterreaderhome.html')
        messages.warning(request, 'Invalid meter id')
        return render (request,'water_reader/water_reader.html')
       

        
       
        
    
    return render(request,'water_reader/water_reader.html')




# def admin_cheek_bill(request):
#     a=WaterBillInfo.objects.all()
 
#     context ={
#         'a':a
#     }
#     return render(request,'water_admin/water_admin.html',context)

# def complain(request):
#     if request.method=="POST":
#         # meter_id = request.user.meter_id
#         print("-"*50)
#         print(request.user)
#         print(request.user.first_name)
#         print(request.user.meter_id)
#         # print(meter_id)
#         print("-"*50)
#         # complain =request.POST.get('complain')
#         # wc=WaterCustomer.objects.get(meter_id=meter_id)
#         # user=WaterCustomer.objects.all()
#         # # if request.user.meter_id==meter_id:
#         # complaindetail = WaterComplain(
#         #      meter_id_id =wc.meter_id,
#         #      complain=complain
#         #        )
#         # complaindetail.save()
#         # return render(request,'customer/main.html')
#         # # return HttpResponse('Invalid Credentials...!!!')        
#     return render(request,'customer/complain1.html')

@login_required
def complain(request):
    if request.method=="POST":
        phone_number=request.POST.get('phone_number')
        complain=request.POST.get('complain')
        x=request.user.username
        y=WaterCustomer.objects.get(username=x)
        m=y.meter_id
        complaindetail = WaterComplain(
        meter_id_id =m,
            complain=complain,
            phone_number=phone_number
                    )
        complaindetail.save()
        messages.success(request,'Complain sent successfully')
        return render(request,'customer/viewwatercomplain.html')

        # phone_number=request.POST.get('phone_number')
        # complain=request.POST.get('complain')
        # if complain ==NULL:
        #     messages.warning(request,'your complain is impty')
        #     return(request,'customer/complain1.html')
        # else:
            

        

        

   
    return render(request,'customer/complain1.html',)
@login_required
def water_technician(request):
    return render(request,'water_technician/water_technician.html')
def reportwatersolved(request):
    if request.method =="POST":      
        x=request.user.username
        idd=int(request.POST.get('id'))
        y=WaterCustomer.objects.get(username=x)
        meter_id=y.meter_id
        complain=WaterComplain.objects.filter(meter_id_id =meter_id)
        # if id == WaterComplain.objects.get(id=id):
        #     print(id)
        # else:
        #     print('This is not correct id')
        #     messages.warning(request,"please input correct complain Id")
        #     return redirect(request, 'customer/reportsolved.html')


        bb=WaterComplain.objects.get(id=idd)
        print(bb.meter_id_id)
        print(meter_id)
        print(type(meter_id), int(bb.meter_id_id))
        if bb.meter_id_id==meter_id:
            bb.is_solved =True
            bb.save()  
        else:
            print("meter id doesn't match")
            messages.warning(request,"please input correct complain Id")
            return redirect(request, 'customer/reportsolved.html')
            


        
        # complaindetail = WaterComplain(
        #     meter_id_id =m,
        #      s=True
             
        #  )
        # complaindetail.save()
        messages.success(request, 'Solution reported successfully')
        return render(request,'customer/viewwaterbill.html')
    return render(request,'customer/reportsolved.html')
def report(request):
    if request.method =='POST':

        x=request.user.username
        y=WaterCustomer.objects.get(username=x)
        complain=WaterComplain.objects.filter(meter_id_id =y)
        idd=complain.id
        print(idd)



    
def viewwaterbill(request):
    x=request.user.username
    x=request.user.username
    print(x)
    # try:
    #     if WaterCustomer.objects.get(username=x).exists():
    y= WaterCustomer.objects.get(username=x)
    m=y.meter_id
    billinfo=WaterBillInfo.objects.filter(meter_id_id = y)
    context = {
            'billinfo': billinfo
            
        }
        
    return render(request,'customer/viewwaterbill.html',context)
    #         return render(request,'customer/customer.html')
    # except Exception as e:
    #     messages.warning(request,'you are not registered for water supply')
    #     return render(request,'customer/customer.html')
    
def waterpayment(request):
    if request.method == "POST":
        x=request.user.username      
        c=WaterCustomer.objects.get(username=x)
        mm=c.meter_id
        customer =Customer.objects.get(username=x)
        y=customer.balance
        print(y)
        billinfo = WaterBillInfo.objects.get(meter_id_id =c)
        amountt= WaterBillInfo.objects.filter(meter_id_id=mm).order_by('-date')[0].amount
        print(amountt)
        deadline=WaterBillInfo.objects.filter(meter_id_id=mm).order_by('-date')[0].deadline
        status = WaterBillInfo.objects.filter(meter_id_id=mm).order_by('-date')[0].is_paid
        waterbalance =WaterBalance.objects.get(id =2)
        print(waterbalance.balance)
        if deadline<=datetime.now():
            print('date')
            # return render(request,'customer/viewwaterbill.html')


        
        print(status)
        payed =y-amountt
        
        print(payed)
        if status == False:
            if payed>=0:

                waterbalance.balance += amountt             
                billinfo.is_paid=True
                customer.balance =payed
                billinfo.save()
                customer.save()
                waterbalance.save()
                messages.success(
                request, "You paid successfully ")
                #return render(request,'customer/viewwaterbill.html')
                return redirect(request,'viewwaterbill')
                


                # billinfo=WaterBillInfo( 
                #     is_paid =True)
                # cus=Customer(balance=payed)
                # billinfo.save()

                # cus.save() 
            messages.warning(request,'Insufficient balance')
            return render(request,'customer/viewwaterbill.html')
        messages.warning(request,'It is already paid')
        return render(request,'customer/viewwaterbill.html')

        
    
    return render(request, 'customer/payment.html')            
def viewwatercomplain(request):
    x=request.user.username
    print(x)
    # y= WaterCustomer.objects.get(username=x)
    # watercomplaindata = WaterComplain.objects.filter(meter_id_id =y)
    # try:
    #     if WaterCustomer.objects.get(username=x).exists():
    y= WaterCustomer.objects.get(username=x)
    m=y.meter_id
    watercomplaindata = WaterComplain.objects.filter(meter_id_id =y)
    context = {
            'watercomplaindata': watercomplaindata
            
        }
        
    return render(request,'customer/viewwatercomplain.html',context)
    #         return render(request,'customer/customer.html')
    # except Exception as e:
    #     messages.warning(request,'you are not registered for water supply')
    #     return render(request,'customer/customer.html')
    
    
def assignedwatercomplain(request):
    x=request.user.username
    print(x)

    totalcomplain =WaterComplain.objects.all()
    assign=WaterComplain.objects.filter(assigned_to=x)
    context ={
        'assign':assign
    }
    return render(request,'water_technician/viewwatercomplain.html',context)






    


    #///////////////////////
    # 
def compeln_ditel(request, pk):

    updatemytabel=WaterComplain.objects.get(pk=pk)

    updatemytabel.is_solved=True
    updatemytabel.save()
    x=request.user.username
    y= WaterCustomer.objects.get(username=x)
    watercomplaindata = WaterComplain.objects.filter(meter_id_id =y)
    
    context = {
        'watercomplaindata':watercomplaindata
    }
    return render(request,'customer/viewwatercomplain.html',context)
def solve_complain(request,pk):
    x=request.user.username
    y= WaterCustomer.objects.get(username=x)
    updatemytabel=WaterComplain.objects.get(pk=pk)
    watercomplaindata = WaterComplain.objects.filter(meter_id_id =y)
    assigned=updatemytabel.assigned_to_id
    solved=updatemytabel.is_solved
    if solved==True:
        messages.warning(request,'It is solved before')
        return render(request,'customer/viewwatercomplain.html')
        
    if assigned==None:
        messages.warning(request,'It is not assigned yet')
        return render(request,'customer/viewwatercomplain.html')
            
    updatemytabel.is_solved=True
    updatemytabel.save()
    context = {
        'watercomplaindata':watercomplaindata
          }
        
    messages.success(request,'You  confirmed the solution successfully')
    return render(request,'customer/viewwatercomplain.html',context)
   
     
   
def ispaid(request,pk):
    x=request.user.username
    # y=x.balance
    customer =Customer.objects.get(username=x)
    y=customer.balance
    pay=WaterBillInfo.objects.get(pk=pk)
    date=pay.deadline
    waterbalance =WaterBalance.objects.get(id =2)
    billdata=WaterBillInfo.objects.filter(meter_id_id = y)
    amountt=pay.amount
    penality=amountt+50
    penal=y-penality
    payed =y-amountt
    treshold=amountt+50
    if y>=treshold:
         if timezone.now()<date:
            if pay.is_paid ==False:
               waterbalance.balance+=amountt
               pay.is_paid=True
               customer.balance=payed
               customer.save()
               waterbalance.save()
               pay.save()
               context={
                  'billdata':billdata
               }
               messages.success(request,"You paid successfully")
               return render(request,'customer/viewwaterbill.html',context)
            else:
               messages.warning(request,"It is paid before")
               return render(request,'customer/viewwaterbill.html')

         else:
            if pay.is_paid ==False:
               waterbalance.balance+=penality
               pay.is_paid=True
               customer.balance=penal
               customer.save()
               waterbalance.save()
               pay.save()
               context={
                  'billdata':billdata
               }
               messages.success(request,"You paid with penality")
               return render(request,'customer/viewwaterbill.html',context)
            else:
               messages.warning(request,"It is paid before")
               return render(request,'customer/viewwaterbill.html')
    messages.warning(request,"the balance you have is insufficient")
    return render(request,'customer/viewwaterbill.html')

   

   
    

def wateryenepay(request):
    x=request.user.username      
    c=WaterCustomer.objects.get(username=x)
    mm=c.meter_id
    # billinfoo = WaterBillInfo.objects.get(meter_id_id =c)
    # bill=WaterBillInfo.objects.all()
    billinfo= WaterBillInfo.objects.filter(meter_id_id=mm).order_by('-date')[0]
    amountt=billinfo.amount
    status=billinfo.status
    print(status)          
    obj = {
                "process": "Express",
                "successUrl": "http://localhost:8000/success",
                "ipnUrl": "http://localhost:8000/ipn",
                "cancelUrl": "http://localhost:8000/cancel",
                "merchantId": "SB1699",
                "merchantOrderId": billinfo.id,
                "expiresAfter": 24,
                 "itemId": 60,
                "itemName": "Billing",
                "unitPrice": amountt,
                 "quantity": 1,
                "discount": 0.0,
               "handlingFee": 0.0,
              "deliveryFee": 0.0,
              "tax1": 0.0,
              "tax2": 0.0
             }
            # billinfo.is_paid=True
            # billinfo.save()
            # messages.success(
            # request, "You paid successfully ")
    return render(request,'customer/payment.html',{'obj': obj})
    # else:
    #     messages.warning(request,'It is already paid')
    #     return render(request,'customer/viewwaterbill.html')
           
    # return render(request, 'pay/index.html', {'obj': obj})
def waterreaderpage(request):
     return render(request,'water_reader/waterreaderhome.html')             
def success(request):
    x=request.user.username      
    c=WaterCustomer.objects.get(username=x)
    mm=c.meter_id
    # billinfoo = WaterBillInfo.objects.get(meter_id_id =c)
    # bill=WaterBillInfo.objects.all()
    billinfo= WaterBillInfo.objects.filter(meter_id_id=mm).order_by('-date')[0]
    amountt=billinfo.amount
    status=billinfo.status
    print(status)
    ii= request.GET.get('itemId')
    total = request.GET.get('TotalAmount')
    moi = request.GET.get('MerchantOrderId')
    ti = request.GET.get('TransactionId')
    status = request.GET.get('Status')
    TransactionCode=request.GET.get('TransationCode')
    MerchantCode = request.GET.get('MerchantCode')
    BuyerId = request.GET.get('BuyerId')

    url = 'https://testapi.yenepay.com/api/verify/pdt/'
    datax = {
        "requestType": "PDT",
        "pdtToken": "Q1woj27RY1EBsm",
        "transactionId": ti,
        "merchantOrderId": moi
    }
    x = requests.post(url, datax)
    if x.status_code == 200:
        print("It's Paid")
        billinfo.status = True
    else:
        print('Invalid payment process')
    context={
        'total':total,
        'status':status,
        # 'TransactionCode':TransactionCode,
        # 'BuyerId': BuyerId,
        # 'moi':moi,
        # 'MerchantCode':MerchantCode,
        # 'billinfo':billinfo

    }
    
    return render(request, 'customer/success.html',context)

def cancel(request):
    return render(request, 'customer/cancel.html')

def ipn(request):
    return render(request, 'customer/ipn.html')   



# def waternotification(request):
#      x=request.user.username      
   
    
#     billinfoo = WaterBillInfo.objects.get(meter_id_id =c)
#     bill=WaterBillInfo.objects.all()
#     billinfo= WaterBillInfo.objects.filter(meter_id_id=mm).order_by('-date')[0].deadline
#     billinfo.date
#     return HttpResponse(status = 200)

def water_assigned_complain(request):
    x=request.user.username
    print(request.user.username)
    y= WaterTechnician.objects.get(username=x)
    print(y)
    assign=WaterComplain.objects.filter(assigned_to =y)
   
    #print(assign)
    # print(assign.id)
    context={
        'assign':assign
    }
    return render(request,'water_technician/waterassigned.html',context) 
def wtec_reported(request,pk):
    x=request.user.username
    y= WaterTechnician.objects.get(username=x)
    updatemytabel=WaterComplain.objects.get(pk=pk)
    assign = WaterComplain.objects.filter(assigned_to =y)
    assigned=updatemytabel.assigned_to_id
    solved=updatemytabel.tec_reported
    updatemytabel.tec_reported=True
    updatemytabel.save()
    context = {
        'assign':assign
          }
    if solved==True:
        messages.warning(request,'you confirmed it already')
        return render(request,'water_technician/viewwatercomplain.html',context)
        
    # if assigned==None:
    #     messages.warning(request,'It is not assigned yet')
    #     return render(request,'customer/viewwatercomplain.html')
            
    
        
    messages.success(request,'You  confirmed the solution successfully')
    return render(request,'water_technician/viewwatercomplain.html',context)


       

   