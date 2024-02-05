from django.db import models
import uuid
import datetime

# Create your models here.
class BookingDetails(models.Model):
    bookingID = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4)
    carID = models.TextField(max_length=10, blank=False)
    start_location = models.TextField(max_length=50, blank=False)
    end_location = models.TextField(max_length=50, blank=False)
    booking_time = models.DateTimeField(default=datetime.datetime.now())
    booking_fare = models.IntegerField(blank=False)
    trip_date = models.DateField(default=datetime.datetime.now())
    userID = models.IntegerField(blank=False, default=0)
    rideStatus = models.IntegerField(blank=False,default=0) #0 Completed, 1 Active

class availableCab(models.Model):
    carID = models.TextField(max_length=10,blank=False, primary_key=True)
    carModel = models.TextField(max_length=10, blank=False)
    availableCapacity = models.IntegerField(blank=False, default=0)

class carsAvailable(models.Model):
    carID = models.TextField(max_length=10,blank=False,primary_key=True)
    carModel = models.TextField(max_length=30,blank=False)
    carCapacity = models.IntegerField(blank=False)
    carNumber = models.TextField(max_length=20,blank=False, default = 0)

class poolRideBooking(models.Model):
    bookingID = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4)
    carID = models.TextField(max_length=10, blank=False)
    start_location = models.TextField(max_length=50, blank=False)
    end_location = models.TextField(max_length=50, blank=False)
    booking_time = models.DateTimeField(default=datetime.datetime.now())
    booking_fare_pu = models.IntegerField(blank=False)
    trip_date = models.DateField(default=datetime.datetime.now())
    userID = models.IntegerField(blank=False, default=0)
    rideStatus = models.IntegerField(blank=False,default=0) #0 Completed, 1 Active
    seats_available = models.IntegerField(blank=False,default=0)