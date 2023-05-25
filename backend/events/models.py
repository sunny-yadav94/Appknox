from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.TextField(null=True)
    maxSeat = models.IntegerField(null=True)
    availableSeat = models.IntegerField(null=True)
    startDate = models.DateTimeField(null=True)
    endDate = models.DateTimeField(null=True)
    location= models.TextField(null=True)
    mode = models.TextField(null=True)

class UserRegistered(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    seatBooked = models.IntegerField(null=True)
    registeredOn = models.DateTimeField(auto_now_add=True)   

