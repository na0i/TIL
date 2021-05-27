from rest_framework import serializers
from board.models import Review


# 리뷰 목록
# 영화에서 보여집니다.
class ReviewListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)

    class Meta:
        model = Review
        fields = ('title', 'id',)
        read_only_fields = ('id', )