from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.PositiveIntegerField()
    other_info = models.CharField(max_length=1000)

    class Meta:
        db_table="user_info"