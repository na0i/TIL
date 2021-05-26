from rest_framework import serializers
from .models import Review, Comment
# from django.conf import settings
from accounts.serializers import UserSerializer


# 대댓글 구현
# 이거 필요 없나봐요..?
class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data


# 댓글
class CommentSerializer(serializers.ModelSerializer):
    replied_by = RecursiveSerializer(many=True, read_only=True)
    # reply_to = serializers.SerializerMethodField()
    content = serializers.CharField(max_length=100)

    class Meta:
        model = Comment
        fields = ('content', 'replied_by', 'id', 'reply_to', 'user', )
        read_only_fields = ('replied_by', 'reply_to', 'user', )


# 댓글 목록 반환
class CommentSetSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = ('comment_set', )
        read_only_fields = ('comment_set', )


# 리뷰 목록
# 영화에서 보여집니다.
class ReviewListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)

    class Meta:
        model = Review
        fields = ('title', 'id',)
        read_only_fields = ('id', )


# 리뷰
class ReviewSerializer(serializers.ModelSerializer):
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
    comment_set = CommentSerializer(many=True, read_only=True)
    like_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'movie_title', 'comment_set', 'user', 'like_users')


# 리뷰 좋아요 사용자
class ReviewLikeUserSerializer(serializers.ModelSerializer):
    like_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = ('like_users', )



