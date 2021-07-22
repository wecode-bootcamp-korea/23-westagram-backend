from django.db                      import models
from phonenumber_field.modelfields  import PhoneNumberField

class User(models.Model):
    name         = models.CharField(max_length=20)
    email        = models.CharField(max_length=50, unique=True)
    password     = models.CharField(max_length=45)
    phone_number = PhoneNumberField(unique=True)
    age          = models.PositiveIntegerField(max_length=3)

    class Meta:
        db_table = "users"