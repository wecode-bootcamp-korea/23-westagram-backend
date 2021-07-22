from django.db import models

class User(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    phone = models.PositiveIntegerField()
    birth = models.DateField(null=True)

    class Meta:
        db_table = "users"
