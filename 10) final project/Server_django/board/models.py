from django.db import models
from django.conf import settings
from movies.models import Movie


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    rank = models.IntegerField()  # 이거 1-5점 선택..
    content = models.TextField(verbose_name='Description')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 대댓글
    # 댓글 참조, 값이 비어 있다면, 댓글, 값이 채워져있으면 대댓글
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='replied_by')

