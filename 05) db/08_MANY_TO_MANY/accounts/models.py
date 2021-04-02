from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    stars = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='fans')
    friends = models.ManyToManyField('self'), symmetrical = False)

    def __str__(self):
        return f'{self.pk}: {self.username}'
    