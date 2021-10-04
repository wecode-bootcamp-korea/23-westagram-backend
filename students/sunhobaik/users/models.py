from django.db import models


class User(models.Model):
    name          = models.CharField(max_length=45, null=True)
    email         = models.CharField(max_length=200)
    password      = models.CharField(max_length=500)
    phone_number  = models.CharField(max_length=200, null=True)
    web_site      = models.CharField(max_length=200, null=True)
    nick_name     = models.CharField(max_length=45, null=True) 
    address       = models.CharField(max_length=200, null=True)
    introduce     = models.TextField(null=True, default='')

    class Meta:
        db_table = 'users'




