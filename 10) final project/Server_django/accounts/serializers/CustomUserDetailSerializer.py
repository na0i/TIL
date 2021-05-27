from rest_auth.serializers import serializers
from rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model

from board.serializers.ReviewForUserSerializer import ReviewForUserSerializer
from movies.serializers.MovieForUserSerializer import MovieForUserSerializer

User = get_user_model()

# 이거 profile에서 사용할 정보들
class CustomUserDetailsSerializer(UserDetailsSerializer):
    nickname = serializers.CharField(max_length=10)
    # 좋아요 누른 리뷰
    like_reviews = ReviewForUserSerializer(many=True, required=False)
    # 내가 작성한 리뷰 역참조 -> related_name
    my_reviews = ReviewForUserSerializer(many=True, required=False)
    # 좋아요 누른 영화
    like_movies = MovieForUserSerializer(many=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'nickname', 'username', 'like_reviews', 'my_reviews', 'like_movies', 'like_genres')

