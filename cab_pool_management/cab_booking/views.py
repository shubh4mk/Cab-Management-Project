from django.shortcuts import render
from .models import BookingDetails, availableCab, carsAvailable

# Create your views here.
def booking(request):

    carsAvail = carsAvailable.objects.all()
    cabBooked = BookingDetails.objects.values_list('carID',flat=True)

    for i in carsAvail:
        if i.carID not in cabBooked:
            availableCab(carID=i.carID, carModel=i.carModel, availableCapacity=i.carCapacity).save()
        else:
            delAvailability=carsAvailable.objects.get(carID=i.carID)
            delAvailability.delete()
    
    availCab=availableCab.objects.all()

    if request.POST:
        car_model = request.POST['car_model']
        propose_fare = request.POST['propose_fare']
        start_location = request.POST['start_location']
        end_location = request.POST['end_location']
        booking_detail = BookingDetails(car_model=car_model,propose_fare=propose_fare,start_location=start_location,end_location=end_location)
        booking_detail.save()
        booking_detail = BookingDetails.objects.all()
        return render(request,'bookings_done.html', context={'booking_details' : booking_detail})
    return render(request,'cabBooking/bookings.html',{'cab_available':availCab})
