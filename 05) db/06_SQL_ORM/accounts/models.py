from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # AbstractUser 의 class var(db col)가 모두 그대로 있음
    pass
    # 추가하려면
    # address = models.CharField(max_length=100)
