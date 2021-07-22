from django.db import models

# Create your models here.

class SignUp(models.Model):
    name     = models.CharField(max_length=45)
    email    = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone_number = models.PositiveIntegerField()
    personal_info = models.TextField(max_length=500)

    class Meta:
        db_table : 'signups'
