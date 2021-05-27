from rest_framework import serializers

from accounts.serializers.UserSerializer import UserSerializer

from movies.models import Movie


# 단일 영화
class MovieLikeUserSerializer(serializers.ModelSerializer):
    like_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('like_users', )