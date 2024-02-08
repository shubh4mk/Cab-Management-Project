from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from cab_booking.models import BookingDetails,carsAvailable,poolRideBooking

# Create your views here.

def userIndex(request):
    if request.user and not request.user.is_staff:
        user_id=request.user.id
        userObj=User.objects.get(id=user_id)
        bookingDetail = BookingDetails.objects.filter(userID=user_id)
        amountSpent = BookingDetails.objects.filter(userID=user_id).values_list('booking_fare',flat=True)
        poolBookingDetail = poolRideBooking.objects.filter(userID=user_id)
        amountSpent_pool = poolRideBooking.objects.filter(userID = user_id).values_list('booking_fare_pu',flat=True)
        totalAmount =0
        rideCount=0
        for i in amountSpent:
            totalAmount+=i
            rideCount+=1
        totalpoolamount = 0
        rideCount_pool = 0
        for i in amountSpent_pool:
            totalpoolamount+=i
            rideCount_pool+=1
        availCar = carsAvailable.objects.all()
        return render(request, "user_dashboard/userIndex.html",{'user':userObj,
                                                                'bookings':bookingDetail,
                                                                'cars':availCar,
                                                                'totalAmount':totalAmount,
                                                                'rideCount':rideCount,
                                                                'poolride':poolBookingDetail,
                                                                'totalpoolamount':totalpoolamount,
                                                                'ridepoolcount':rideCount_pool})
    else:
        user_id=request.user.id
        userObj=User.objects.get(id=user_id)
        bookingDetail = BookingDetails.objects.all()
        amountSpent = BookingDetails.objects.values_list('booking_fare',flat=True)
        poolBookingDetail = poolRideBooking.objects.all()
        totalAmount =0
        rideCount=0
        for i in amountSpent:
            totalAmount+=i
            rideCount+=1
        availCar = carsAvailable.objects.all()
        amountSpent_pool = poolRideBooking.objects.values_list('booking_fare_pu',flat=True)
        totalpoolamount = 0
        rideCount_pool = 0
        for i in amountSpent_pool:
            totalpoolamount+=i
            rideCount_pool+=1
        return render(request, "user_dashboard/userIndex.html",{'user':userObj,
                                                                'bookings':bookingDetail,
                                                                'cars':availCar,
                                                                'totalAmount':totalAmount,
                                                                'rideCount':rideCount,
                                                                'poolride':poolBookingDetail,
                                                                'totalpoolamount':totalpoolamount,
                                                                'ridepoolcount':rideCount_pool})
def signout(request):
    return redirect('signout')
