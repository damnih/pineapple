from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    name = models.TextField()
    age = models.IntegerField()
    nationality = models.TextField()
    
    USERNAME_FIELD = 'username'
