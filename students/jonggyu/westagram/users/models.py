from django.db                      import models
from phonenumber_field.modelfields  import PhoneNumberField

class User(models.Model):
    name         = models.CharField(max_length=20)
    email        = models.CharField(max_length=200, unique=True)
    password     = models.CharField(max_length=200)
    phone_number = PhoneNumberField(unique=True)
    age          = models.PositiveIntegerField()

    class Meta:
        db_table = "users"