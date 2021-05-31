from rest_auth.serializers import serializers
from movies.models import Movie

# user 프로필에서 보여질 정보
class MovieForUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path', 'vote_average', 'release_date')