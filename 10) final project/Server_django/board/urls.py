from django.urls import path
import board.views
import movies.views


urlpatterns = [
    # 전체 영화 조회 및 생성 -> 여기서 추천 기반 보내고
    path('', movies.views.movie_list_or_create),
    # 최초 정보 등록 -> get 으로 목록만 불러오기..
    path('initial_data/', movies.views.fetch_initial_datum),
    # 장르 정보 업데이트
    path('genres/', movies.views.get_genre_data),
    # 장르로 추천
    path('genres/<int:genre_pk>/', movies.views.recommend_by_genre),
    # 좋아요 누른 장르 정보 업데이트
    # path('genres/user/<int:user_pk>', movies.views.set_like_genres),
    # 단일 영화 정보
    path('<int:movie_pk>/', movies.views.get_or_create_movie),
    # 영화 사이트 연결
    path('<int:movie_pk>/provider/', movies.views.get_provider_url),
    # 영화 검색
    path('search/', movies.views.search_movie),
    # 영화 좋아요
    path('<int:movie_pk>/likes/', movies.views.like_movie),
    # 리뷰 생성
    path('<int:movie_pk>/review/', board.views.create_review),
    # 리뷰 상세 페이지 (조회, 수정, 삭제) --> 이 페이지에 댓글 생성 & 반환
    path('<int:movie_pk>/review/<int:review_pk>/', board.views.read_or_update_or_delete_review),
    # 리뷰 좋아요
    path('<int:movie_pk>/review/<int:review_pk>/likes/', board.views.like_review),
    # 댓글 생성
    path('<int:movie_pk>/review/<int:review_pk>/comment/', board.views.create_comment),
    # 댓글 수정/ 삭제/ 대댓글 생성
    path('<int:movie_pk>/review/<int:review_pk>/comment/<int:comment_pk>/', board.views.update_or_delete_or_recreate_comment),

]