from django.db import models

# Create your models here

class User(models.Model):
        name         = models.CharField(max_length=50)
        email        = models.CharField(max_length=320)
        password     = models.CharField(max_length=200)
        phone_number = models.CharField(max_length=50)

        class Meta:
            db_table ='users'


