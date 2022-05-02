from django.shortcuts import render,redirect
from .models import WaterBillInfo,WaterCustomer


# Create your views here.
def addemployee(request):
    return render(request,'admin_home.html')
def water_reader(request):
    if request.method=="POST":
        meter_id_id =request.POST.get('meter_id_id')
        current_reading = request.POST.get('current_reading')
        wc = WaterCustomer.objects.get(meter_id=meter_id_id)
        billinfo = WaterBillInfo(
            meter_id_id = wc.meter_id,
            current_reading=current_reading

        )
        billinfo.save()
        return redirect ('water_reader')
    
    return render(request,'water_reader/water_reader.html')
# def water_complain(request):
#     if request.method=== "POST":
