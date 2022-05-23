from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_user = models.BooleanField('Is user', default=False)
    is_staff = models.BooleanField('Is staff', default=False)

class Data(models.Model):
    name = models.CharField(blank=False,max_length=25)
    picture = models.ImageField(upload_to = "images/staff/")
    age = models.IntegerField()
    similiar = models.ImageField(blank=True,upload_to = "images/users/")
    location = models.CharField(blank=True,max_length=50)
    accuracy = models.DecimalField(blank=True,default=0,max_digits=5,decimal_places=2)
    found = models.BooleanField(default=False)