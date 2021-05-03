from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField()
    content = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DataTimeField(auto_now=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DataTimeField(auto_now=True)