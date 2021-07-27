from django.db import models

# Create your models here.

class User(models.Model):
    name          = models.CharField(max_length=45)
    email         = models.CharField(max_length=100)
    password      = models.CharField(max_length=200)
    phone_number  = models.CharField(max_length=45)
    age           = models.PositiveIntegerField()

    class Meta:
        db_table = "users"
