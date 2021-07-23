from django.db import models


class User(models.Model):
    name          = models.CharField(max_length=45)
    email         = models.CharField(max_length=200)
    password      = models.CharField(max_length=45)
    phone_number  = models.CharField(max_length=45)
    web_site      = models.CharField(max_length=200)
    nick_name     = models.CharField(max_length=45) 
    address       = models.CharField(max_length=200)
    introduce     = models.TextField()

    class Meta:
        db_table = 'users'


