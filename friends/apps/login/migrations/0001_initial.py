# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-25 22:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('alias', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('birthday', models.DateField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('friendships', models.ManyToManyField(related_name='_user_friendships_+', to='login.User')),
            ],
        ),
    ]