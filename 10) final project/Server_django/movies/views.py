from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import get_user_model

import pprint
import requests

from .models import Movie, Genre
from .api_request import get_genre, save_movie, recommend_movies, get_movie_info, search_tmdb, get_providers, get_genre_list
from movies.serializers.GenreSerializer import GenreSerializer
from movies.serializers.MovieSerializer import MovieSerializer
from movies.serializers.MovieListSerializer import MovieListSerializer
from movies.serializers.MovieLikeUserSerializer import MovieLikeUserSerializer
from movies.serializers.MovieForUserSerializer import MovieForUserSerializer

from accounts.serializers.CustomUserDetailSerializer import CustomUserDetailsSerializer


@api_view(['POST', 'GET'])
def get_genre_data(request):
    # 영화 장르 정보 불러오기
    if request.method == 'POST':
        datum = get_genre()

        results = {
            'saved': 0,
            'failed': 0,
        }

        for data in datum:
            if not Genre.objects.all().filter(pk=data['id']).exists():
                serializer = GenreSerializer(data=data)
                # if serializer.is_valid(raise_exception=True):
                if serializer.is_valid():
                    serializer.save()
                    results['saved'] += 1
                else:
                    results['failed'] += 1

        return Response(data=results)

    # 영화 장르 정보 뷰에 저장
    elif request.method == 'GET':
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)


### fetch initial datum
@api_view(['POST', 'GET'])
def fetch_initial_datum(request):

    # 관리자의 경우에만 최초 데이터 불러오기 가능
    # if request.user.is_superuser:

    # DB에 자료 저장
    if request.method == 'POST':
        conditions = ['popular', 'top_rated']  # top_rated

        results = {
            'success': 0,
            'failed': [
                0,
                {
                    'title': []
                }
            ]
        }

        # 인기순 100/
        # 평점 높은 순 100/
        for condition in conditions:
            for i in range(1, 201):
                datum = recommend_movies(condition, page=i)
                for data in datum:
                    if data['popularity'] < 10:
                        continue

                    if data['vote_count'] < 30:
                        continue

                    movie_pk = data['id']
                    if not Movie.objects.all().filter(pk=movie_pk):
                        save_movie(data)
                        results['success'] += 1
                    else:
                        results['failed'][0] += 1
                        results['failed'][1]['title'].append(data['title'])

        return Response(data=results)

    # vue에서 초기 목록 요청
    elif request.method == 'GET':
        movies = Movie.objects.all()

        top_rated = movies.filter(vote_count__gt=300).order_by('-vote_average')[:24]
        tr_serializer = MovieSerializer(top_rated, many=True)
        popular = movies.order_by('-popularity')[:24]
        pop_serializer = MovieSerializer(popular, many=True)
        ko_top_rated = movies.filter(original_language='ko').order_by('-vote_average')[:24]
        ko_serializer = MovieSerializer(ko_top_rated, many=True)
        classic = movies.filter(release_date__range=["1970-01-01", "1998-01-01"]).order_by('-vote_average')[:24]
        classic_serializer = MovieSerializer(classic, many=True)

        data = [tr_serializer.data, pop_serializer.data, ko_serializer.data, classic_serializer.data]

        content = {
            'status': 1,
            'responseCode': status.HTTP_200_OK,
            'data': data,
        }
        return Response(content)


# 영화 생성 혹은 영화 전체 리스트
@api_view(['GET', 'POST'])
def movie_list_or_create(request):

    # 단일 영화 생성
    if request.method == 'POST':
        # print(request.data['condition'])
        '''
        # recommend_movies(condition, page=1)
        인기 영화 = popular
        top_rated = top_rated

        // 페이지 한개 밖에 없는 듯 //
        개봉예정 = upcoming
        상영중 = now_playing
        '''
        results = {
            'success': [],
            'failed': []
        }

        # condition 이 들어서 요청이 왔다면,
        if request.data.get('condition'):
            # 들어온 조건으로 요청을 보내서 데이터를 받아온 다음에
            datum = recommend_movies(request.data['condition'])
            for data in datum:
                movie_pk = data['id']
                if not Movie.objects.all().filter(pk=movie_pk):
                    results['success'].append(save_movie(data))
                else:
                    results['failed'].append(data['title'])
        else:
            if not Movie.objects.all().filter(pk=request.data['id']):
                save_movie(request.data)



        return Response(data=results)

    # 전체 영화 리스트
    elif request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 단일 영화 상세 페이지
'''
이거 없다면 추가하는 건 일단 다른 함수든 연결해야 할 것 같습니다. 
애초에 영화 데이터 자체를 어드민만 추가할 수 있는게 명세라서 좀 더 고민이 필요해 보입니다. 
'''
@api_view(['GET', 'POST'])
def get_or_create_movie(request, movie_pk):
    # DB에 없다면,
    if not Movie.objects.all().filter(pk=movie_pk):
        movie = get_movie_info(movie_pk)
        saved = save_movie(movie)
        return Response(saved)

    # DB에 있다면,
    else:
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


# 영화 좋아요
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user

    # 좋아요 취소
    if movie.like_users.filter(username=user).exists():
        movie.like_users.remove(user)

    # 좋아요
    else:
        movie.like_users.add(user)

    serializer = MovieLikeUserSerializer(movie)
    return Response(serializer.data)


# @api_view(['GET'])
def search_movie(request):
    movies = Movie.objects.all()
    results = movies.filter(title__contains=request.data)

    # 검색 결과가 있다면,
    if results:
        serializer = MovieSerializer(results, many=True)
        return Response(serializer.data)

    # 검색 결과가 없다면,
    else:
        return search_tmdb(request.data)



# tmdb 크롤링
@api_view(['GET'])
def get_provider_url(request, movie_pk):
    # <QueryDict: {'method': ['flatrate'], 'provider': ['wavve']}>
    # print(request.GET['method']) flatrate
    method = request.GET['method']
    provider = request.GET['provider']

    link = get_providers(movie_pk, method, provider)

    # if request.GET.method == 'flatrate':
    # elif request.GET.method == 'buy':
    #     link = get_providers(movie_pk, method, provider)
    # elif request.GET.method == 'rent':
    #     pass

    data = {
        'link': link
    }
    return Response(data)


# 장르 정보 가지고 추천
@api_view(['GET'])
def recommend_by_genre(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)

    movies = Movie.objects.all().filter(genres__movie__genres=genre)[:6]

    serializer = MovieSerializer(movies, many=True)

    return Response(serializer.data)





# 혹시 프로필 수정해서 좋아하는 장르 수정되면 이거 사용해주면 됩니다...
# def set_like_genres(request, user_pk):
#     user = get_object_or_404(get_user_model(), pk=user_pk)
#     genres = request.data['like_genres']
#
#     for genre in genres:
#         if not user.like_genres.filter(id=genre['id']).exists():
#             user.like_genres.add(genre)
#             user.save()
#
#     serializer = CustomUserDetailsSerializer(user)
#     return Response(serializer.data)

