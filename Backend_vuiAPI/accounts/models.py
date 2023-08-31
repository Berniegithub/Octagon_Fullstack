from django.db import models
from django.contrib.auth.models import User 


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Login(models.Model):
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    password = models.CharField(max_length=128)  

    def __str__(self):
        return self.phone_number
    
class Register(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"





