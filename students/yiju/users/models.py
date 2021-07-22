from django.db import models

class User(models.Model) :
	name          = models.CharField(max_length=45)
	email         = models.CharField(max_length=100, unique=True)
	password      = models.CharField(max_length=100)
	

	class Meta :
		db_table = 'users'

class Information(models.Model) :
	contact_point = models.CharField(max_length=100, null=True)
	sex            = models.CharField(max_length=3, null=True)
	age            = models.PositiveIntegerField(null=True)
	user           = models.ForeignKey('User',on_delete = models.CASCADE)

	class Meta :
		db_table = 'information'