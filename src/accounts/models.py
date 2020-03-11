from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    TYPE = (
        (1,"Student"),
        (2,"Teacher"),
    )
    role = models.IntegerField(choices = TYPE)
