from rest_framework import serializers
from .models import Review, Comment
# from django.conf import settings


# 대댓글 구현
# 이거 필요 없나봐요..?
class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data


# 댓글
class CommentSerializer(serializers.ModelSerializer):
    replied_by = RecursiveSerializer(many=True, read_only=True, allow_null=True)
    # reply_to = serializers.SerializerMethodField()
    content = serializers.CharField(max_length=100)

    class Meta:
        model = Comment
        fields = ('content', )


# 댓글 수정
# class CommentUpdateSerializer(serializers.ModelSerializer):
#     comment = CommentSerializer()
#
#     class Meta:
#         model = Comment
#         fields = ('review', 'user', 'reply_to', 'content', )


# 리뷰 목록
# 영화에서 보여집니다.
class ReviewListSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)

    class Meta:
        model = Review
        fields = ('title',)


# 리뷰
class ReviewSerializer(serializers.ModelSerializer):
    # num_choices = zip(range(0, 5), range(0, 5))

    try:
        from movies.serializers import MovieSerializer
    except ImportError:
        import sys
        MovieSerializer = sys.modules[__package__ + '.MovieSerializer']
    movie = MovieSerializer(read_only=True)
    movie_title = serializers.CharField(max_length=100, source='movie.title', read_only=True)
    title = serializers.CharField(max_length=100)
    content = serializers.CharField(min_length=1)
    rank = serializers.IntegerField()
    # rank = serializers.ChoiceField(choices=num_choices)
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'movie_title', 'comment_set', 'user', 'like_users')



