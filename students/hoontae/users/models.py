from django.db import models

# Create your models here.
class User(models.Model):
    name      = models.CharField(max_length=45)
    email     = models.CharField(max_length=300)
    password  = models.CharField(max_length=400)
    phone_num = models.CharField(max_length=20)
    birthday  = models.DateField()

    class Meta:
        db_table = 'users'
    