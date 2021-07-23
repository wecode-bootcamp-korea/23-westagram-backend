from django.db import models
from django.db.models.deletion import CASCADE



class User(models.Model):
    name          = models.CharField(max_length=45)
    email         = models.TextField(max_length=200)
    password      = models.TextField(max_length=45)
    phone_number  = models.CharField(max_length=45)
    web_site      = models.TextField(max_length=200)
    nick_name     = models.CharField(max_length=45) 
    address       = models.TextField(max_length=200)
    introduce     = models.CharField(max_length=4000)

    class Meta:
        db_table = 'users'


