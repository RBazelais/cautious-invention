from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.first_name

# from apps.main.models import *
# User.objects.all()
# User.objects.create(first_name='William', last_name='Croft', email_address='will@mohun.com', age=15)
# User.objects.create(first_name='Hannibal', last_name='Croft', email_address='hanny@mohun.com', age=15)
# User.objects.create(first_name='Poogie', last_name='Pig', email_address='poggie@mohun.com', age=10)
# User.objects.first() - William
# User.objects.last() - Poogie
# User.objects.order_by("first_name")
# User.objects.get(id=3)
# Poo = User.objects.get(id=3)
#  Poo.last_name = "Piglet"
#  Poo.save()
# User.objects.get(id=3)
# User.objects.create(first_name='Random', last_name='Person', email_address='none@mohun.com', age=12)
# User.objects.all()
# rando = User.objects.get(id=4)
# rando.delete()