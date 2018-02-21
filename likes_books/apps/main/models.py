from __future__ import unicode_literals
from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    email = models.EmailField()
    # uploaded_books = models.ForeignKey(Book, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
class Book(models.Model):
    name = models.CharField(max_length=225)
    desc = models.CharField(max_length=255)
    uploaded_by_id = models.ForeignKey(User, related_name="uploader")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s" % (self.name, self.desc)