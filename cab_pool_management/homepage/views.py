from django.shortcuts import render,redirect
from django.contrib.auth.models import User

# Create your views here.
def homepage(request):
    if request.POST:
        if request.user.is_authenticated and request.user.id != "AnonymousUser":
            ride_type=request.POST['ride-type']
            ride_pay=request.POST['ride-pay']
            pickup=request.POST['start-location']
            drop=request.POST['end-location']
            tripDate=request.POST['tripDate']
            user_id=request.user.id
            trip_search=[ride_type,ride_pay,pickup,drop,tripDate]
            return redirect('bookcab',trip_search)
        else:
            return redirect('signin')
    return render(request,"homepage/index.html")

def aboutus (request):
    return render(request,"aboutUs/aboutUs.html")
    