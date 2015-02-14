from django.db import models

# Create your models here.

class Booking(models.Model):
    month = models.CharField(max_length=20)
    payid = models.CharField(max_length=100)   
    hid = models.IntegerField()
    city_code = models.IntegerField()
    UNIQ = models.CharField(max_length=2) 
    Pending = models.IntegerField()
    Booking = models.IntegerField()
    Mobile = models.IntegerField()
    RoomPrice = models.IntegerField()
    booking_date = models.DateField('booking date')  
    checkin_date = models.DateField('checkin date')   
    checkout_date = models.DateField('checkout date')
    cid_booking = models.IntegerField()
    duration = models.IntegerField()
