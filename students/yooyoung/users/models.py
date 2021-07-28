from django.db import models


class User(models.Model):
    name         = models.CharField(max_length=40, null=True)
    email        = models.EmailField(max_length=200, unique=True)
    password     = models.CharField(max_length=200)
    age          = models.PositiveIntegerField(null=True)
    phone_number = models.CharField(max_length=60, null=True)

    class Meta:
        db_table = 'users'
