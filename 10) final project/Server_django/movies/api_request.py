import pprint
import requests
import re

from bs4 import BeautifulSoup

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


def recommend_movies(condition, page=1):
    '''
    인기 영화 = popular
    top_rated = top_rated

    // 페이지 한개 밖에 없는 듯 //
    개봉예정 = upcoming
    상영중 = now_playing
    '''

    recommend_URL = f'https://api.themoviedb.org/3/movie/{condition}?api_key=1f6f8f7d643eea003df9f19e38d13c3d&language=ko-KR&page={page}&region=KR'
    response = requests.get(recommend_URL).json()
    # print(response)
    # print(recommend_URL)
    response = response['results']

    return response



# def get_movie_info(movie_id, condition='', page=1):
def get_movie_info(movie_id):
    # cast&crew/ 비슷한 영화 추천/ 영화 볼 수 있는 사이트정보
    # similar 의 경우에만 페이지 들어갑니다..!
    # if condition == 'credits':
    #     condition = '/' + condition
    # elif condition == 'similar':
    #     condition = '/' + condition
    # elif condition == 'watch':
    #     condition = '/watch/providers'

    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=1f6f8f7d643eea003df9f19e38d13c3d&language=ko-KR&page=1'
    response = requests.get(url).json()

    # if condition == '/watch/providers':
    #     response = response['results']['KR']
    # elif condition == 'credits' or condition == 'similar':
    #     response = response['results']

    return response


def search_tmdb(query, page=1, include_adult=True, region='ko', primary_release_year=''):
    if primary_release_year:
        primary_release_year = f'&year=year&primary_release_year={primary_release_year}'

    url = f'https://api.themoviedb.org/3/search/movie?api_key=1f6f8f7d643eea003df9f19e38d13c3d&language=ko-KR&query={query}&page={page}&include_adult={include_adult}&region={region}{primary_release_year}'

    response = requests.get(url).json()['results']

    pprint.pprint(response)

    return response


def get_providers(movie_id):
    url = f'https://www.themoviedb.org/movie/{movie_id}/watch?language=ko'
    # https: // www.themoviedb.org / movie / 496243 / watch?language = ko

    isprovidedby = get_movie_info(movie_id, 'provider')

    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    streaming = ''
    buy = ''
    rent = ''

    if isprovidedby['flatrate']:
        datum = soup.select('#ott_offers_window > section > div.header_poster_wrapper > div > div:nth-child(4) > div > ul > li.ott_filter_best_price a')
        streaming = []
        for data in datum:
            each = {'link': data.attrs["href"], 'site': data.attrs["title"].split('on ')[1]}
            streaming.append(each)

    if isprovidedby['buy']:
        datum = soup.select('#ott_offers_window > section > div.header_poster_wrapper > div > div:nth-child(6) > div > ul > li.ott_filter_best_price a')
        buy = []
        for data in datum:
            each = {'link': data.attrs["href"], 'site': data.attrs["title"].split('on ')[1]}
            buy.append(each)

    if isprovidedby['rent']:
        datum = soup.select('#ott_offers_window > section > div.header_poster_wrapper > div > div:nth-child(5) > div > ul > li.ott_filter_best_price a')
        rent = []
        for data in datum:
            each = {'link': data.attrs["href"], 'site': data.attrs["title"].split('on ')[1]}
            rent.append(each)

    providers = {
        'streaming': streaming,
        'buy': buy,
        'rent': rent,
    }

    return providers


def get_genre_list(genres):
    genre = re.compile(r'\d+')
    genres = genre.findall(genres)

    return genres


def save_movie(data):
    pprint.pprint(data)
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
def fetch_datum():
    # 평점 높은 순으로 50/
    # 최신영화 50/
    for i in range(50):
        recommend_movies('popular', page=i)

    for i in range(50):
        recommend_movies('top_rated', page=i)

    for i in range(50):
        recommend_movies('latest', page=i)









