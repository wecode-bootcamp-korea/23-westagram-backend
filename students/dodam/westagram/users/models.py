from django.db import models


# Create your models here.
class User(models.Model):
	name 		 = models.CharField(max_length=45)
	email	 	 = models.CharField(max_length=200, unique=True)
	password 	 = models.CharField(max_length=200, null=False)
	phone_number = models.CharField(max_length=20)
	birthday	 = models.DateTimeField()

	class Meta:
	   db_table = 'users'