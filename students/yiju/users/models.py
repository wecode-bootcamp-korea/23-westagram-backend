from django.db import models

class User(models.Model) :
	name = models.CharField(max_length=45)
	email = models.CharField(max_length=100, unique=True)
	password = models.CharField(max_length=100)
	contact_point = models.CharField(max_length=100)

	class Meta :
		db_table = 'users'

class Information(models.Model) :
	content = models.CharField(max_length=1000)
	user = models.ForeignKey('User')

	class Meta :
		db_table = 'information'