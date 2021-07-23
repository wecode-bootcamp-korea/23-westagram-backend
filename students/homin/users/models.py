from django.db import models

class User(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=320)
    password = models.CharField(max_length=45)
    phonenumber = models.CharField(max_length=45)
#    birth_date = models.DateField(null=True, blank=True)
#    time_zone = models.CharField(max_length=45, black=True)
#    regist_date = models.DateField()
    class Meta:
        db_table = 'users'
    def __str__(self):
        return self.name

