from rest_framework import serializers
from accounts.serializers.UserSerializer import UserSerializer

from board.models import Review

from movies.serializers.MovieSerializer import MovieSerializer
from .CommentSerializer import CommentSerializer


# 리뷰
class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    movie_title = serializers.CharField(max_length=100, source='movie.title', read_only=True)
    title = serializers.CharField(max_length=100)
    content = serializers.CharField(min_length=1)
    rank = serializers.IntegerField()
    comment_set = CommentSerializer(many=True, read_only=True)
    like_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'movie_title', 'comment_set', 'user', 'like_users')

