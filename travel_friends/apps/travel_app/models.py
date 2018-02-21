from __future__ import unicode_literals

from django.db import models
from ..login.models import User
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Create your models here.

class TripManager(models.Manager):
    def trip_validation(self, postData):
        errors = []
        
        if len(postData['destination']) < 2:
            errors.append("Your destination must have a title")
        if len(postData['description']) < 2:
            errors.append("Your trip must have a description")
        # if postData['start_date'] < now:
		# 	    errors.append("You cannot start in the past")
        try:
            if datetime.strptime(postData['end_date'], '%Y-%m-%d') < datetime.strptime(postData['start_date'], '%Y-%m-%d'):
                errors.append("Check end date. Time travel not allowed.")
        except ValueError:
            errors.append("Please enter a valid start and end date")
        
        if len(errors) > 0:
			return (False, errors)
        else:
            uploader = User.objects.get(id=postData['user'])
            new_trip = Trip.objects.create(
                destination = postData['destination'], 
                description = postData['description'],
                start_date = postData['start_date'],
                end_date = datetime.strptime(postData['end_date'], '%Y-%m-%d'),
                uploader = uploader,
            )
            # new_trip.user_trips.add()
            return (True, new_trip)

    
    # def join(self):
    #     join_trip = User.objects.get(id=)
    #     pass

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=True)

    uploader = models.ForeignKey(User)
    members = models.ManyToManyField(User, related_name="travelers")
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = TripManager()

    def __str__(self):
        return self.destination