from rest_framework import serializers

from movies.serializers.GenreSerializer import GenreSerializer
from accounts.serializers.UserSerializer import UserSerializer
from board.serializers.ReviewListSerializer import ReviewListSerializer

from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    overview = serializers.CharField(min_length=1, required=False, allow_blank=True)
    release_date = serializers.DateField(required=False)
    poster_path = serializers.CharField(max_length=200, required=False, allow_blank=True)
    backdrop_path = serializers.CharField(max_length=200, required=False, allow_null=True, allow_blank=True)
    original_language = serializers.CharField(max_length=50, required=False, allow_blank=True)
    genres = GenreSerializer(many=True, required=False, read_only=True)
    like_users = UserSerializer(many=True, read_only=True)
    reviews = ReviewListSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        # fields = ('id', 'title', 'overview', 'release_date', 'poster_path', 'review_set')
        fields = '__all__'
