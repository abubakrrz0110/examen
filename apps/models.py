from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    about = models.TextField()
    image = models.ImageField(upload_to='users/', blank=True, null = True)
    address = models.CharField(max_length=500)