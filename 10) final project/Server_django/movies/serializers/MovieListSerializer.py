from rest_framework import serializers

from movies.models import Movie


# 전체 영화 목록
# 만약 영화 리스트 화면에서 보이고 싶은 데이터가 추가적으로 존재하는 경우,
# 여기서 필드에 추가해주면 되겠습니다.
class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'id', 'original_title', )