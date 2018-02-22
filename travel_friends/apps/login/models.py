from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from dateutil.relativedelta import relativedelta
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def reg_validation(self, postData):
        errors = []
        if len(postData['name']) < 2:
            errors.append("Your name is too short")

        if len(postData['user_name']) < 2:
            errors.append("Your username is too short")

        if not EMAIL_REGEX.match(postData['email']):
            errors.append('You must submit a valid email')
        else:	
			emails = User.objects.filter(email=postData['email'])
			if len(emails) != 0:	
				errors.append("This email is invalid")
        if postData['password'] != postData['confirm_password']:
            errors.append("Your passwords do not match")

        if postData['password'] < 8:
            errors.append("Your password is too short")
        # else:
        #     hashed = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())

        try:
            if datetime.strptime(postData['birthday'], '%Y-%m-%d') > datetime.now() - relativedelta(years = 13):
                errors.append("You must be at least 13 years old to register")
        except ValueError:
            errors.append("Please enter a valid date")

        if len(errors) > 0:
			return errors
        else:
            new_user = User.objects.create(
                name = postData['name'], 
                username = postData['user_name'],
                email = postData['email'],
                password = postData['password'],
                # password = hashed, 
                birthday = postData['birthday'],
            )
            return (True, new_user[0])	
    
    def login_validation(self, postData):    
        errors = []
        if len(postData['user_name']) < 2:
            errors.append("Your username is too short")
        if len(postData['password']) < 2:
            errors.append("Your password is too short")

        if len(errors) > 0:
            return (False, errors)
        else:
            user_exists = User.objects.filter(username=postData['user_name'])
            # QuerySet[<User Obj>]
            if user_exists: # check to see if i got a user based on username
                print "found a user", 0
                if user_exists[0].password == postData['password']: 
                    # if true, username and password matches what is in DB
                    return (True, user_exists[0]) # <User Obj>    
                else:
                    errors.append("Password is incorrect") 
                    return(False, errors)
            else:
                print "did not find user"
                errors.append("No user exists with this username.") 
                return(False, errors)
                
        # users = User.objects.filter(username=postData['user_name'])
        # password = User.objects.get(password=postData['password'])
        # if len(postData['user_name']) < 2:
		# 	errors.append("Username is too short")
        # elif bcrypt.checkpw(password.encode('utf-8'), users[0].password.encode()) == False:
		# 	return "Incorrect password"
        # else:	
		# 	return users[0]


class User(models.Model):
    name = models.CharField(max_length=25)
    username = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    password = models.SlugField(max_length=50)
    birthday = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return self.name

# current date
# born before current date - 13 years
# datetime.now() - relativedelta(years = 13)
# convert str to datetime object in python
# print strptime(postData['birthday'], '%Y-%m-%d')