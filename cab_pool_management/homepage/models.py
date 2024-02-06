from django.db import models
import datetime
# Create your models here.

class searchTrip(models.Model):
    ride_type = models.TextField(max_length=50, blank=False,default="solo")
    propose_fare = models.IntegerField(blank=False,default=0)
    pickup = models.TextField(max_length=40,blank=False,default="Christ University,Pune")
    drop = models.TextField(max_length=40,blank=False,default="Pune Railway Station")
    ride_date = models.DateField(blank=False,default=datetime.datetime.now())