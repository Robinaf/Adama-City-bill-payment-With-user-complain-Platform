from multiprocessing import context
from django.db.models import IntegerField
from django.db.models.functions import Cast
from django.shortcuts import render,redirect
from .models import WaterBillInfo,WaterCustomer,WaterComplain


# Create your views here.
def water_admin(request):
    wc=WaterCustomer.objects.all()

    return render(request,'water_admin/index.html',{'WaterCustomer':wc})
def water_reader(request):
    if request.method=="POST":
        meter_id_id =request.POST.get('meter_id_id')
        
        current_reading = request.POST.get('current_reading')
        month = request.POST.get('month')
        year = request.POST.get('year')
        wc = WaterCustomer.objects.get(meter_id=meter_id_id)
        
        # bi= WaterBillInfo.objects.filter(prev_reading=prev_reading)
        # prev_reading=bi.prev_reading
        billinfo = WaterBillInfo(
            meter_id_id = wc.meter_id,
           
             
            current_reading=current_reading,
            month=month,
            year=year,

            # prev_reading = wc.prev_reading,
            amount = int(current_reading) *2

        )
        billinfo.save()
        return redirect ('water_reader')
    
    return render(request,'water_reader/water_reader.html')
# def admin_cheek_bill(request):
#     a=WaterBillInfo.objects.all()
 
#     context ={
#         'a':a
#     }
#     return render(request,'water_admin/water_admin.html',context)
def complain(request):
    if request.method=="POST":
         meter_id_id =request.POST.get('meter_id_id')
         complain =request.POST.get('complain')
         wc=WaterCustomer.objects.get(meter_id=meter_id_id)

         complaindetail = WaterComplain(
             meter_id_id =wc.meter_id,
             complain=complain
         )
         complaindetail.save()
         return render(request,'customer/main.html')
    return render(request,'customer/complain1.html')
