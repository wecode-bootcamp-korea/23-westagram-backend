from django.db import models

class User(models.Model):
    name       = models.CharField(max_length=100)
    email      = models.CharField(max_length=200, unique=True)
    password   = models.CharField(max_length=45)
    cellphone  = models.CharField(max_length=45)
    age        = models.PositiveIntegerField()
    gender     = models.CharField(max_length=45)
    birth_date = models.DateField()

    class Meta:
        db_table = 'users'