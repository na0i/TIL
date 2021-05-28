# from django.contrib.auth.models import AbstractUser
# from django.conf import settings
# from django.db import models
# from imagekit.models import ProcessedImageField
# from imagekit.processors import ResizeToFill
#
# from movies.models import Genre
#
# email, nickname, like_genres,
#
#
#
#
# class User(AbstractUser):
#     followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
#
#
# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     is_profile_set = models.BooleanField()
#     nickname = models.CharField(max_length=10, blank=True)
#     like_genre = models.ManyToManyField(Genre)
#     image = ProcessedImageField(
#         blank=True,
#         upload_to='profile/images',
#         processors=[ResizeToFill(300, 300)],
#         format='JPEG',
#         options={'quality': 90},
#     )

from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Genre


class User(AbstractUser):
    username = models.CharField(max_length=10, unique=True)
    nickname = models.CharField(max_length=10)
    email = models.EmailField(blank=True, null=True)
    like_genres = models.ManyToManyField(Genre, related_name='like_users')






