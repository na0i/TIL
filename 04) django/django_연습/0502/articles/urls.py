from django.urls import path
from . import views

app_name = 'articles'

url_patterns = [
    path('', views.index, name = 'index'),
    path('create/', views.article_create, name = 'create'),
    path('<int:article_pk>/detail/', views.article_detail, name = 'detail'),
    path('<int:article_pk>/update/', views.article_update, name = 'update'),
    path('<int:article_pk>/delete/', views.article_delete, name = 'delete'),
    path('<int:article_pk>/comments/', views.comments_create, name = 'comments_create'),
    path('<int:article_pk>/comments/<int:comment_pk>', views.)
]