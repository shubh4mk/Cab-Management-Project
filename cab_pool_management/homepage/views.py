from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import searchTrip
import datetime

# Create your views here.
def homepage(request):

    searchTrip.objects.all().delete()

    if request.POST:
        if request.user.is_authenticated and request.user.id != "AnonymousUser":
            ride_type=request.POST['ride-type']
            ride_pay=request.POST['ride-pay']
            if ride_pay == "":
                ride_pay = 0
            pickup=request.POST['start-location']
            drop=request.POST['end-location']
            if pickup == drop:
                return render(request,"homepage/index.html",{'location_error_message': "Pick and Drop Can't be Same"})
            
            if pickup != "Christ University,Pune" and drop != "Christ University,Pune":
                return render(request,"homepage/index.html",{'location_error_message': "Sorry! Pick or Drop must at Christ University"})
            
            tripDate=request.POST['tripDate']
            if tripDate =="":
                tripDate = datetime.datetime.now()
            searchTrip(ride_type=ride_type,
                       propose_fare=ride_pay,
                       pickup=pickup,
                       drop=drop,
                       ride_date=tripDate).save()
            # return render(request,"cabBooking/bookings.html",{'trip_search':trip_search})
            return redirect('bookcab')
        else:
            return redirect('signin')
    return render(request,"homepage/index.html")

def aboutus (request):
    return render(request,"aboutUs/aboutUs.html")
    