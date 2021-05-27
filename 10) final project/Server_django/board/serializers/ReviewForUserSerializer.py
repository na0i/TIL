from rest_auth.serializers import serializers

from movies.serializers.MovieForUserSerializer import MovieForUserSerializer

from board.models import Review


# user 프로필에서 보여질 정보
class ReviewForUserSerializer(serializers.ModelSerializer):
    movie = MovieForUserSerializer()

    class Meta:
        model = Review
        fields = ('id', 'title', 'movie', )