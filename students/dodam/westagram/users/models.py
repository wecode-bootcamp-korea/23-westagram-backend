from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=45)
	email = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	phone_number = models.CharField(max_length=20)
	birthday = models.DateTimeField('date published')

	class Meta:
		db_table = 'users'