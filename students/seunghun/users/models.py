from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Essential_User(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=20)
    phone_num = models.CharField(max_length=20)

    class Meta:
        db_table = 'essential_users'

class Select_User(models.Model):
    name = models.ForeignKey('Essential_User', on_delete=CASCADE)
    address = models.CharField(max_length=50, null=True)
    date_of_birth = models.DateField(null=True)
    nickname = models.CharField(max_length=10,null=True)

    class Meta:
        db_table = 'select_users'
