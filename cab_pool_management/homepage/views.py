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
            user_id=request.user.id
            #return render(request,"homepage/index.html",{'user':user_id})
        else:
            return redirect('signin')
    return render(request,"homepage/index.html")

def aboutus (request):
    return render(request,"aboutUs/aboutUs.html")
    