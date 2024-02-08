from django.shortcuts import render, redirect
from .models import BookingDetails, availableCab, carsAvailable, poolRideBooking
from homepage.models import searchTrip
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models import F

# Create your views here.
def booking(request):
    user_id=request.user.id
    userObj=User.objects.get(id=user_id)
    ride_date=searchTrip.objects.values_list('ride_date',flat=True).first()
    if userObj.is_staff==0: #IF User is Normal User
        carsAvail = carsAvailable.objects.all()
        cabBooked = BookingDetails.objects.filter(rideStatus=1).filter(trip_date=ride_date).values_list('carID',flat=True)
        poolCabBooked = poolRideBooking.objects.filter(rideStatus=1).filter(trip_date=ride_date).values_list('carID',flat=True)

        #Update Available Cab Table
        for i in carsAvail:
            if i.carID not in cabBooked and i.carID not in poolCabBooked:
                availableCab(carID=i.carID, carModel=i.carModel, availableCapacity=i.carCapacity).save()
            elif ((i.carID in cabBooked and i.carID in availableCab.objects.values_list('carID',flat=True)) 
                  or
                  (i.carID in poolCabBooked and i.carID in availableCab.objects.values_list('carID',flat=True))):
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
                ride_type= searchTrip.objects.values_list('ride_type',flat=True).first()
                if capacity != "":
                    availCab=availableCab.objects.filter(availableCapacity = capacity)
                else:
                    availCab=availableCab.objects.all()
                availPoolRides = poolRideBooking.objects.filter(rideStatus=1,seats_booked__lt=F('carCapacity')).filter(start_location=start_location).filter(end_location=end_location)
                return render(request,'cabBooking/bookings.html',{'cab_available':availCab,
                                                                      'availPoolRides':availPoolRides,
                                                                      'ride_Search':rideSearch,
                                                                      'rideDate':ride_date,
                                                                      'cabFare':booking_fare,
                                                                      'carCapacity':capacity,
                                                                      'rideType':ride_type,'carsAvail':carsAvail})
            else: #When Cab is getting booked
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
                ride_type=searchTrip.objects.values_list('ride_type',flat=True).first()
                
                if  ride_type == "solo":
                    booking_detail = BookingDetails(carID=carID,
                                                    start_location=start_location,
                                                    end_location=end_location,
                                                    booking_fare=booking_fare,
                                                    userID=request.user.id,
                                                    rideStatus=1,
                                                    trip_date=rideDate)
                    active_cab = BookingDetails.objects.filter(rideStatus=1,trip_date=ride_date).values_list('carID',flat=True)
                    if carID in active_cab:
                        pass
                    else:
                        booking_detail.save()
                    booking_detail = BookingDetails.objects.filter(userID=request.user.id).filter(carID=carID).filter(rideStatus=1)
                elif ride_type == "pool":
                    booking_fare=booking_fare/capacity
                    if poolRideBooking.objects.filter(carID=carID).filter(rideStatus=1).filter(trip_date=ride_date):
                        poolRideBooking.objects.filter(carID=carID).filter(rideStatus=1).filter(trip_date=ride_date).update(seats_booked=F('seats_booked') + 1)
                        seats_booked = poolRideBooking.objects.filter(carID=carID).filter(rideStatus=1).filter(trip_date=ride_date).values_list('seats_booked',flat=True).first()
                    else:
                        seats_booked=1
                    poolBook = poolRideBooking(carID=carID,
                                                start_location=start_location,
                                                end_location=end_location,
                                                booking_fare_pu=booking_fare,
                                                userID=request.user.id,
                                                rideStatus=1, carCapacity=capacity,seats_booked=seats_booked,
                                                trip_date=rideDate)
                    active_cab = poolRideBooking.objects.filter(rideStatus=1,trip_date=ride_date,userID=user_id).values_list('carID',flat=True)
                    if carID in active_cab:
                        pass
                    else:
                        poolBook.save()
                    booking_detail = poolRideBooking.objects.filter(userID=request.user.id,trip_date=ride_date).filter(carID=carID).filter(rideStatus=1)

                return render(request,'cabBooking/booking_done.html',{'booking_details' : booking_detail,'rideType':ride_type})
        else:
            rideSearch = searchTrip.objects.all()
            ride_type = searchTrip.objects.values_list('ride_type',flat=True).first()
            rideDate = searchTrip.objects.values_list('ride_date',flat=True).first()
            start_location = searchTrip.objects.values_list('pickup',flat=True).first()
            end_location = searchTrip.objects.values_list('drop',flat=True).first()
            if rideDate is None:
                rideDate=datetime.now()
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
            availPoolRides = poolRideBooking.objects.filter(rideStatus=1,seats_booked__lt=F('carCapacity')).filter(start_location=start_location,end_location=end_location)
            return render(request,'cabBooking/bookings.html',{'cab_available':availCab,
                                                              'availPoolRides':availPoolRides,
                                                              'ride_Search':rideSearch,
                                                              'rideDate':ride_date,
                                                              'cabFare':booking_fare,
                                                              'carCapacity':capacity,
                                                              'rideType':ride_type,'carsAvail':carsAvail})
    
    elif userObj.is_staff==1:
        if request.POST:
            carID_tripDate = request.POST["booking"]
            carID = carID_tripDate.split(";")[0]
            tripDate = carID_tripDate.split(";")[1]
            date_obj = datetime.strptime(tripDate, "%b. %d, %Y")
            ride_date = date_obj.strftime("%Y-%m-%d")
            carID_solo =  BookingDetails.objects.filter(carID=carID).filter(rideStatus=1)
            carID_pool = poolRideBooking.objects.filter(carID=carID).filter(rideStatus=1)
            BookingDetails.objects.filter(carID=carID).filter(rideStatus=1).filter(trip_date=ride_date).update(rideStatus=0)
            poolRideBooking.objects.filter(carID=carID).filter(rideStatus=1).filter(trip_date=ride_date).update(rideStatus=0)
        activeBookings = BookingDetails.objects.filter(rideStatus=1)
        activepoolBookings = poolRideBooking.objects.filter(rideStatus=1)
        carsAvail = carsAvailable.objects.all()
        return render(request,'cabBooking/bookings.html',{'cab_available':activeBookings,'carsAvail':carsAvail,'pool_cab_available':activepoolBookings})


def booking_done(request):
    return render(request,'cabBooking/booking_done.html')
