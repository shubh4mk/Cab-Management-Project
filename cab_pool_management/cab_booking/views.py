from django.shortcuts import render
from .models import BookingDetails

# Create your views here.
def booking(request):
    if request.POST:
        car_model = request.POST['car_model']
        propose_fare = request.POST['propose_fare']
        start_location = request.POST['start_location']
        end_location = request.POST['end_location']
        booking_detail = BookingDetails(car_model=car_model,propose_fare=propose_fare,start_location=start_location,end_location=end_location)
        booking_detail.save()
        booking_detail = BookingDetails.objects.all()
        return render(request,'bookings_done.html', context={'booking_details' : booking_detail})