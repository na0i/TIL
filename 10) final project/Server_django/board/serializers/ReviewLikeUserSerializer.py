from rest_framework import serializers

from accounts.serializers.UserSerializer import UserSerializer

from board.models import Review


# 리뷰 좋아요 사용자
class ReviewLikeUserSerializer(serializers.ModelSerializer):
    like_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = ('like_users', )
