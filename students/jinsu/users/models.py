from django.db import models

# Create your models here.
class User(models.Model):
    name     = models.CharField(max_length=20)
    email    = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=32)
    contact  = models.CharField(max_length=20)
    age      = models.PositiveIntegerField()

    class Meta:
        db_table = 'users'



    
