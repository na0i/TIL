from bs4 import BeautifulSoup
import requests
import re

from django.shortcuts import get_object_or_404
from .models import Movie
from movies.serializers.MovieSerializer import MovieSerializer



URL = 'https://api.themoviedb.org/3'
api_key = '1f6f8f7d643eea003df9f19e38d13c3d'


# 영화 장르 가져오기
def get_genre():
    genre_url = 'https://api.themoviedb.org/3/genre/movie/list?api_key=1f6f8f7d643eea003df9f19e38d13c3d&language=ko-kr'
    response = requests.get(genre_url).json()['genres']

    return response


# 영화 추천
def recommend_movies(condition, page=1):
    '''
    인기 영화 = popular
    top_rated = top_rated
    개봉예정 = upcoming
    상영중 = now_playing
    '''

    recommend_URL = f'https://api.themoviedb.org/3/movie/{condition}?api_key=1f6f8f7d643eea003df9f19e38d13c3d&language=ko-KR&page={page}&region=KR'
    response = requests.get(recommend_URL).json()
    response = response['results']

    return response


# 개별 영화 상세 정보
def get_movie_info(movie_id):

    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=1f6f8f7d643eea003df9f19e38d13c3d&language=ko-KR&page=1'
    response = requests.get(url).json()

    return response


# tmdb 검색
def search_tmdb(query, page=1, include_adult=True, region='ko', primary_release_year=''):
    if primary_release_year:
        primary_release_year = f'&year=year&primary_release_year={primary_release_year}'

    url = f'https://api.themoviedb.org/3/search/movie?api_key=1f6f8f7d643eea003df9f19e38d13c3d&language=ko-KR&query={query}&page={page}&include_adult={include_adult}&region={region}{primary_release_year}'

    response = requests.get(url).json()['results']

    return response


# 시청 사이트 연결
def get_providers(movie_id, method, provider):
    url = f'https://www.themoviedb.org/movie/{movie_id}/watch?language=ko'

    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    methods = ['flatrate', 'rent', 'buy']

    link = ''
    for i in range(3):
        if method == methods[i]:
            datum = soup.select(f'#ott_offers_window > section > div.header_poster_wrapper > div > div:nth-child({i+4}) > div > ul > li.ott_filter_best_price a')
            for data in datum:
                if provider in data.attrs["title"]:
                    link = data.attrs["href"]
                    break

    return link


# 장르 리스트 불러오기
# 사용 X
def get_genre_list(genres):
    genre = re.compile(r'\d+')
    genres = genre.findall(genres)

    return genres


# db에 없는 영화 저장
def save_movie(data):
    movie_pk = data['id']
    serializer = MovieSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        movie = get_object_or_404(Movie, pk=movie_pk)

        # 전체 검색을 통해 불러오는 경우
        if data.get('genre_ids'):
            genres = data['genre_ids']
            for genre in genres:
                movie.genres.add(genre)

        # 영화 상세 검색
        else:
            genres = data['genres']
            for genre in genres:
                movie.genres.add(genre['id'])

        return serializer.data


### fetch initial datum
# 최초로 불러오는 영화 정보
def fetch_datum():
    # 평점 높은 순으로 50/
    # 최신영화 50/
    for i in range(50):
        recommend_movies('popular', page=i)

    for i in range(50):
        recommend_movies('top_rated', page=i)

    for i in range(50):
        recommend_movies('latest', page=i)









