from django.shortcuts import render
from .models import BookingDetails, availableCab, carsAvailable

# Create your views here.
def booking(request,trip_search):

    carsAvail = carsAvailable.objects.all()
    cabBooked = BookingDetails.objects.filter(rideStatus=0).values_list('carID',flat=True)

    for i in carsAvail:
        if i.carID not in cabBooked:
            availableCab(carID=i.carID, carModel=i.carModel, availableCapacity=i.carCapacity).save()
        else:
            delAvailability=carsAvailable.objects.get(carID=i.carID)
            delAvailability.delete()
    
    availCab=availableCab.objects.all()

    if request.POST:
        if (start_location=="Christ University,Pune" and end_location=="Pune Railway Station") or (end_location=="Christ University,Pune" and start_location=="Pune Railway Station") :
            booking_fare=2500
        elif (start_location=="Christ University,Pune" and end_location=="Pune Internation Airport") or (end_location=="Christ University,Pune" and start_location=="Pune Internation Airport"):
            booking_fare=3000
        elif (start_location=="Christ University,Pune" and end_location=="Phoenix Mall,Pune") or (end_location=="Christ University,Pune" and start_location=="Phoenix Mall,Pune"):
            booking_fare=2000
        elif (start_location=="Christ University,Pune" and end_location=="Swargate Bus Stop") or (end_location=="Christ University,Pune" and start_location=="Swargate Bus Stop"):
            booking_fare=3000
        carID = request.POST['carID']
        propose_fare = request.POST['propose_fare']
        start_location = request.POST['start_location']
        end_location = request.POST['end_location']
        trip_date = request.POST['trip_date']

        booking_detail = BookingDetails(carID=carID,start_location=start_location,end_location=end_location)
        booking_detail.save()
        booking_detail = BookingDetails.objects.all()
        return render(request,'bookings_done.html', context={'booking_details' : booking_detail})
    return render(request,'cabBooking/bookings.html',{'cab_available':availCab})
