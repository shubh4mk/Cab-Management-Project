from django.db import models
import uuid
import datetime

# Create your models here.
class BookingDetails(models.Model):
    bookingID = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4)
    car_model = models.TextField(max_length=20, blank=False)
    start_location = models.TextField(max_length=50, blank=False)
    end_location = models.TextField(max_length=50, blank=False)
    booking_time = models.DateTimeField(default=datetime.datetime.now())
    booking_fare = models.IntegerField(blank=False)

class availableCab(models.Model):
    cabID = models.TextField(max_length=10, blank=False)
    cabModel = models.TextField(max_length=10, blank=False)
    cabCapacity = models.IntegerField(blank=False)
    
