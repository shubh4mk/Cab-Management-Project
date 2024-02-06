from django.shortcuts import render, redirect
from .models import BookingDetails, availableCab, carsAvailable
from homepage.models import searchTrip
from datetime import datetime

# Create your views here.
def booking(request):
    carsAvail = carsAvailable.objects.all()
    cabBooked = BookingDetails.objects.filter(rideStatus=1).values_list('carID',flat=True)

    for i in carsAvail:
        if i.carID not in cabBooked:
            availableCab(carID=i.carID, carModel=i.carModel, availableCapacity=i.carCapacity).save()
        elif i.carID in cabBooked and i.carID in availableCab.objects.values_list('carID',flat=True):
            delAvailability=availableCab.objects.get(carID=i.carID)
            delAvailability.delete()

    availCab=availableCab.objects.all()

    if request.POST:
        if request.POST['booking']=="search":
            start_location = request.POST['start-location_b']
            end_location = request.POST['end-location_b']
            ride_type = request.POST['ride-type_b']
            capacity = request.POST['carCapacity_b']
            ride_date = request.POST['tripDate_b']
            ride_pay=request.POST['ride-pay_b']
            if ride_pay == "":
                ride_pay = 0
            if (start_location=="Christ University,Pune" and end_location=="Pune Railway Station") or (end_location=="Christ University,Pune" and start_location=="Pune Railway Station") :
                booking_fare=2500
            elif (start_location=="Christ University,Pune" and end_location=="Pune International Airport") or (end_location=="Christ University,Pune" and start_location=="Pune International Airport"):
                booking_fare=3000
            elif (start_location=="Christ University,Pune" and end_location=="Phoenix Mall,Pune") or (end_location=="Christ University,Pune" and start_location=="Phoenix Mall,Pune"):
                booking_fare=2000
            elif (start_location=="Christ University,Pune" and end_location=="Swargate Bus Stop") or (end_location=="Christ University,Pune" and start_location=="Swargate Bus Stop"):
                booking_fare=3000

            if start_location == end_location:
                    return redirect('bookcab')
                
            if start_location != "Christ University,Pune" and end_location != "Christ University,Pune":
                return redirect('bookcab')
            
            searchTrip.objects.all().delete()
            
            searchTrip(ride_type=ride_type,
                        propose_fare=ride_pay,
                        pickup=start_location,
                        drop=end_location,
                        ride_date=ride_date).save()
            rideSearch = searchTrip.objects.all()

            if capacity != "":
                availCab=availableCab.objects.filter(availableCapacity = capacity)
            else:
                availCab=availableCab.objects.all()
            return render(request,'cabBooking/bookings.html',{'cab_available':availCab,'ride_Search':rideSearch,'rideDate':ride_date,'cabFare':booking_fare,'carCapacity':capacity})

        else:
            carID = request.POST['booking']
            rideDate = searchTrip.objects.values_list('ride_date',flat=True).first()
            start_location = searchTrip.objects.values_list('pickup',flat=True).first()
            end_location = searchTrip.objects.values_list('drop',flat=True).first()
            if (start_location=="Christ University,Pune" and end_location=="Pune Railway Station") or (end_location=="Christ University,Pune" and start_location=="Pune Railway Station") :
                booking_fare=2500
            elif (start_location=="Christ University,Pune" and end_location=="Pune International Airport") or (end_location=="Christ University,Pune" and start_location=="Pune International Airport"):
                booking_fare=3000
            elif (start_location=="Christ University,Pune" and end_location=="Phoenix Mall,Pune") or (end_location=="Christ University,Pune" and start_location=="Phoenix Mall,Pune"):
                booking_fare=2000
            elif (start_location=="Christ University,Pune" and end_location=="Swargate Bus Stop") or (end_location=="Christ University,Pune" and start_location=="Swargate Bus Stop"):
                booking_fare=3000
            capacity = carsAvailable.objects.filter(carID=carID).values_list('carCapacity',flat=True).first()
            if capacity == 5:
                booking_fare=booking_fare+500
            elif capacity == 6:
                booking_fare=booking_fare+600
            booking_detail = BookingDetails(carID=carID,
                                            start_location=start_location,
                                            end_location=end_location,
                                            booking_fare=booking_fare,
                                            userID=request.user.id,
                                            rideStatus=1,
                                            trip_date=rideDate)
            active_cab = BookingDetails.objects.filter(rideStatus=1).values_list('carID',flat=True)
            if carID in active_cab:
                pass
            else:
                booking_detail.save()
            booking_detail = BookingDetails.objects.all()
            return render(request,'cabBooking/booking_done.html', context={'booking_details' : booking_detail})
    else:
        rideSearch = searchTrip.objects.all()
        rideDate = searchTrip.objects.values_list('ride_date',flat=True).first()
        start_location = searchTrip.objects.values_list('pickup',flat=True).first()
        end_location = searchTrip.objects.values_list('drop',flat=True).first()
        ride_date = rideDate.strftime("%Y-%m-%d")
        capacity = ""
        if (start_location=="Christ University,Pune" and end_location=="Pune Railway Station") or (end_location=="Christ University,Pune" and start_location=="Pune Railway Station") :
            booking_fare=2500
        elif (start_location=="Christ University,Pune" and end_location=="Pune International Airport") or (end_location=="Christ University,Pune" and start_location=="Pune International Airport"):
            booking_fare=3000
        elif (start_location=="Christ University,Pune" and end_location=="Phoenix Mall,Pune") or (end_location=="Christ University,Pune" and start_location=="Phoenix Mall,Pune"):
            booking_fare=2000
        elif (start_location=="Christ University,Pune" and end_location=="Swargate Bus Stop") or (end_location=="Christ University,Pune" and start_location=="Swargate Bus Stop"):
            booking_fare=3000
        
        return render(request,'cabBooking/bookings.html',{'cab_available':availCab,'ride_Search':rideSearch,'rideDate':ride_date,'cabFare':booking_fare,'carCapacity':capacity})

def booking_done(request):
    return render(request,'cabBooking/booking_done.html')
