from django.db import models

class User(models.Model):
    name     = models.CharField(max_length=45)
    email    = models.CharField(max_length=100)
    password = models.CharField(max_length=45)
    phone    = models.CharField(max_length=20)
    birth    = models.DateField()

    class Meta:
        db_table = "users"
