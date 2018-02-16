from __future__ import unicode_literals
from django.db import models

	# Create your models here.

	# class Base(models.Model):
	#     created_at = models.DateTimeField(auto_now_add=True)
	#     updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	notes = models.TextField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.last_name

class Book(models.Model):
	name = models.CharField(max_length=255)
	desc = models.TextField(max_length=1000)
	author = models.ManyToManyField(Author)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

# from apps.main.models import *
# Book.objects.all()
# >>> <QuerySet [<Book: C Sharp>, <Book: Java>, <Book: Python>, <Book: Ruby>, <Book: PHP>]>
# Author.objects.all()
# >>> <QuerySet [<Author: Sharpe>, <Author: Speros>, <Author: John>, <Author: Jadee>, <Author: Jay>]>
# CLang = Book.objects.get(id=1)
# >>> CLang.name = "C#"
# >>> CLang.save()
# Book.objects.get(id=1)
# >>><Book: C#>
# new_name = Author.objects.get(id=5)
# >>> new_name.first_name ="Ketul"
# >>> new_name.save()
# CLang.author.add(Author.objects.get(id=1))
# Java = Book.objects.get(id=2)
# Java.author.add(Author.objects.get(id=1))
# Ruby = Book.objects.get(id=4)
# >>> CLang.author.add(Author.objects.get(id=3))
# >>> Java.author.add(Author.objects.get(id=3))
# >>> Python.author.add(Author.objects.get(id=3))
# >>> Ruby.author.add(Author.objects.get(id=3))
# CLang.author.add(Author.objects.get(id=4))
# >>> Java.author.add(Author.objects.get(id=4))
# >>> Python.author.add(Author.objects.get(id=4))
# >>> Ruby.author.add(Author.objects.get(id=4))
# >>> PHP = Book.objects.get(id=5)
# >>> PHP.author.add(Author.objects.get(id=4))
# Book.objects.get(id=3).author.all()
# Python.author.remove(Author.objects.first())
# PHP.author.add(Author.objects.get(id=5))
# Book.objects.filter(author = Author.objects.get(first_name="Jack"))
# Book.objects.filter(author = Author.objects.get(first_name="James"))