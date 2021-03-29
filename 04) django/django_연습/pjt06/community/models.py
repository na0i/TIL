from django.db import models
from django.conf import settings

# Create your models here.
class Review(models.Model):
    # settings / models.CAS'C'ADE
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # user = models.ForeignKey(setting.AUTH_USER_MODEL, on_delete=CASADE)
    title = models.CharField(max_length = 100)
    movie_title = models.CharField(max_length = 50)
    rank = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.CharField(max_length = 100)

    # def __str__(self):
    def __str__(self):
        return self.content
    