from django.urls import path
from . import views

urlpatterns = [
    # practice0309에 lotto라고 들어온다면 어디로 가느냐?!
    # /practice0309/lotto/
    path('lotto/<int:no>/', views.lotto),

    # /practice0309/var_route/뭐든지 들어옴/
    path('var_route/<value>/', views.var_route),

    # /practice0309/ping/ => <form> 으로 사용자 입력 받기
    path('ping/', views.ping, name='ping'),
    # /practice0309/pong/ => 처리 결과 보여주기
    path('pong/', views.pong, name='pong'),
]
