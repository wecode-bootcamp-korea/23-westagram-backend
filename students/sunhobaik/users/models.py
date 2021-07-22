from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import TextField, IntegerField


class User(models.Model):
    name         =models.TextField(max_length=20)
    email        =models.TextField(max_length=100)
    password     =models.TextField(max_length=20)
    phone_numbers=models.IntegerField()
    privacy      =models.TextField(max_length=200)
    
    def Meta(self):
        db_table = 'users'


