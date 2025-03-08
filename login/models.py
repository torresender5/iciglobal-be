from django.db import models
from django.contrib.auth.models import AbstractUser,  Permission, Group

# Create your models here.



class User(AbstractUser):
    second_name = models.CharField(max_length=150, default='', null=True)
    second_last_name = models.CharField(max_length=150, default='', null=True)

    def __str__(self):
        return self.username
    
# class Permission(Permission):
    
