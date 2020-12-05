from django.db import models

# Create your models here.
'''
#管理员账号密码


class Admin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)



    def __str__(self):
        return self.username
'''


#admin1 1234
#admin2 1234
#admin3 1234


class Reservation(models.Model):
    id = models.IntegerField(primary_key=True)
    phone = models.CharField(max_length=16)
    service_type = models.CharField(max_length=10)
    to_agenda = models.BooleanField(default=False)
    dele = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)



