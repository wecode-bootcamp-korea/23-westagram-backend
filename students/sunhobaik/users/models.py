from django.db import models
from django.db.models.deletion import CASCADE



class User(models.Model):
    name          = models.CharField(max_length=20)
    email         = models.TextField(max_length=100)
    password      = models.TextField(max_length=20)
    phone_numbers = models.CharField(max_length=20)
    web_site      = models.TextField(max_length=30)
    nick_name     = models.CharField(max_length=20) 
    address       = models.TextField(max_length=100)
    introduce     = models.TextField(max_length=200)
    def Meta(self):
        db_table = 'users'


