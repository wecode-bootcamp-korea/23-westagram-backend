from django.db import models
from django.core.validators import RegexValidator


class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    note = models.TextField(max_length=100, null=True)
    phone = models.CharField(
        max_length=16,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format '+123456789'. Up to 15 digits allowed."
            ),
        ],
    )
    
    class Meta:
        db_table = 'Users'
