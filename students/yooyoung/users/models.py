from django.db import models


class User(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=80)
    note = models.TextField(max_length=100, null=True)
    phone = models.CharField(max_length=16, null=True)

    class Meta:
        db_table = 'users'
