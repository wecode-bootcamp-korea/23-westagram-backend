from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=45)
	email = models.CharField(max_length=200)
	password = models.PositiveIntegerField(max_length=200)
	phone_number = models.PositiveIntegerField(max_length=20)
	etc_inform = models.CharField(max_length=300)

	class Meta:
		db_table = 'Users'