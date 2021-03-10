from django.urls import path
from . import views

urlpatterns = [
    # 목록 보여주기
    path('', views.index, name='index'),
    # 1번 학생 정보 보여주기(단일 조회)
    path('<int:pk>/', views.detail, name='detail'),
    # 새로운 데이터 입력용 html(생성 준비단계)
    path('new/', views.new, name='new'),
    # 사용자 입력 데이터 처리
    path('create/', views.create, name='create')
]
