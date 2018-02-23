from __future__ import unicode_literals

from django.db import models
import re
from datetime import datetime
from dateutil.relativedelta import relativedelta
import bcrypt


# Create your models here.
class UserManager(models.Manager):

    def register_valdiation(self, postData):
        print postData
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        errors = []
        if len(postData['first_name']) < 2:
            errors.append("Your first name is too short")
        if len(postData['last_name']) < 2:
            errors.append("Your last name is too short")
        if not EMAIL_REGEX.match(postData['email']):
            errors.append("You must submit a valid email")
        if postData['password'] != postData['confirm_password']:
            errors.append("Your passwords do not match")
        try:
             if datetime.strptime(postData["birthday"], '%Y-%m-%d') > datetime.now():
                errors.append("I know you weren't born yesterday")
        except ValueError:
            errors.append("You must enter a valid date")

        if len(errors) > 0:
            return (False, errors)
        else:
            hashed = bcrypt.hashpw(postData['password'].encode('utf8'), bcrypt.gensalt())
            user = User.objects.create(first_name=postData['first_name'], last_name=postData['last_name'], email=postData['email'], password=hashed, birthday = postData['birthday'])
            return (True, user)
    
    def login_validation(self, postData):
        errors = []
        if len(postData['email']) < 2:
            errors.append("email is too short")
        if len(postData['password']) == 0:
            errors.append("Password must not be blank")
        
        if len(errors) > 0:
            return (False, errors)
        else:
            user = User.objects.filter(email=postData['email'])
            print user
            if user:
                if bcrypt.checkpw(postData['password'].encode('utf8'), user[0].password.encode('utf8')):
                    return (True, user)
                else: 
                    errors.append("Password is invalid")
            else:
                errors.append("Email is invalid")
            return (False, errors)
    pass
        
class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    birthday = models.DateField(auto_now=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()


