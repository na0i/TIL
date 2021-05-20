from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):    
    nickname = models.CharField(max_length=20)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
