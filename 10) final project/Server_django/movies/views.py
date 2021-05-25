from django.shortcuts import get_object_or_404, HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import pprint
import requests

from .models import Movie, Genre
from .api_request import get_genre, save_movie, recommend_movies, get_movie_info, search, get_providers, get_genre_list
from .serializers import GenreSerializer, MovieSerializer, MovieListSerializer


# 영화 장르 정보 가져오기
@api_view(['POST'])
def get_genre_data(request):
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


### fetch initial datum
@api_view(['POST'])
def fetch_initial_datum(request):

    # 관리자의 경우에만 최초 데이터 불러오기 가능
    if request.user.is_superuser:

        conditions = ['popular', 'top_rated']

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
                    movie_pk = data['id']
                    if not Movie.objects.all().filter(pk=movie_pk):
                        save_movie(data)
                        results['success'] += 1
                    else:
                        results['failed'][0] += 1
                        results['failed'][1]['title'].append(data['title'])

        return Response(data=results)

    # 관리자가 아닌 경우에는, 메인으로 이동
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/')


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

        # 영화 각각에 대해서 실행..
        # for data in datum:
        #     movie_pk = data['id']
        #     if not Movie.objects.all().filter(pk=movie_pk):
        #         serializer = MovieSerializer(data=data)
        #         if serializer.is_valid(raise_exception=True):
        #             serializer.save()
        #             movie = get_object_or_404(Movie, pk=movie_pk)
        #             genres = data['genre_ids']
        #             # genres = get_genre_list(data['genre_ids'])
        #             for genre in genres:
        #                 movie.genres.add(genre)
        #                 movie.save()
        #             results['success'].append(serializer.data)
                # return Response(serializer.data, status=status.HTTP_201_CREATED)

            # movie_pk = request.data['id']
            # if not Movie.objects.all().filter(pk=movie_pk):
            #     serializer = MovieSerializer(data=request.data)
            #     if serializer.is_valid(raise_exception=True):
            #         serializer.save()
            #         movie = get_object_or_404(Movie, pk=movie_pk)
            #         genres = get_genre_list(request.data['genre_ids'])
            #         for genre in genres:
            #             movie.genres.add(genre)
            #             movie.save()
            #         return Response(serializer.data, status=status.HTTP_201_CREATED)

            # 이미 있는 영화

        return Response(data=results)

    # 전체 영화 리스트
    elif request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 단일 영화 상세 페이지
@api_view(['GET'])
def get_or_create_movie(request, movie_pk):
    # DB에 없다면,
    if not Movie.objects.all().filter(pk=movie_pk):
        movie = get_movie_info(movie_pk)
        return Response(save_movie(movie))

    # DB에 있다면,
    else:
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
