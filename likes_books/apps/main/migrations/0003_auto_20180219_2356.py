# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-19 23:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_user_uploaded_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='uploaded_by_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploader', to='main.User'),
        ),
    ]
