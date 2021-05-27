from rest_framework import serializers
from board.models import Comment


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data


# 댓글
class CommentSerializer(serializers.ModelSerializer):
    replied_by = RecursiveSerializer(many=True, read_only=True)
    content = serializers.CharField(max_length=100)

    class Meta:
        model = Comment
        fields = ('content', 'replied_by', 'id', 'reply_to', 'user', )
        read_only_fields = ('replied_by', 'reply_to', 'user', )
