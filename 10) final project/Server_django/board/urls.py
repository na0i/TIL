from django.urls import path
import board.views
import movies.views


urlpatterns = [
    # 전체 영화 조회 및 생성
    path('', movies.views.movie_list_or_create),
    # 최초 정보 등록
    path('initial_data/', movies.views.fetch_initial_datum),
    # 장르 정보 업데이트
    path('genres/', movies.views.get_genre_data),
    # 단일 영화 정보
    path('<int:movie_pk>/', movies.views.get_or_create_movie),
    # 리뷰 생성
    path('<int:movie_pk>/review/', board.views.create_review),
    # 리뷰 상세 페이지 (조회, 수정, 삭제) --> 이 페이지에 댓글 생성 & 반환
    path('<int:movie_pk>/review/<int:review_pk>/', board.views.read_or_update_or_delete_review),
    # 댓글 생성
    path('<int:movie_pk>/review/<int:review_pk>/comment/', board.views.create_comment),
    # 댓글 수정/ 삭제/ 대댓글 생성
    path('<int:movie_pk>/review/<int:review_pk>/comment/<int:comment_pk>/', board.views.update_or_delete_comment),

]