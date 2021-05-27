from rest_framework import serializers
from board.models import Review
from .CommentSerializer import CommentSerializer


# 댓글 목록 반환
class CommentSetSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = ('comment_set', )
        read_only_fields = ('comment_set', )