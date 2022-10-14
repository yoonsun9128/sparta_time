from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=40, blank=False)
    address = models.CharField(max_length=50 blank=False)