from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from cab_booking.models import BookingDetails,carsAvailable

# Create your views here.

def userIndex(request):
    if request.user:
        user_id=request.user.id
        userObj=User.objects.get(id=user_id)
        bookingDetail = BookingDetails.objects.filter(userID=user_id)
        amountSpent = BookingDetails.objects.filter(userID=user_id).values_list('booking_fare',flat=True)
        totalAmount =0
        rideCount=0
        for i in amountSpent:
            totalAmount+=i
            rideCount+=1
        availCar = carsAvailable.objects.all()
        return render(request, "user_dashboard/userIndex.html",{'user':userObj,'bookings':bookingDetail,'cars':availCar,'totalAmount':totalAmount,'rideCount':rideCount})

def signout(request):
    return redirect('signout')
