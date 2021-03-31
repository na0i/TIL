from django.urls import path
from . import views

app_name = 'board'
comment_prefix = '<int:article_pk>/comments'

# '/board/'
urlpatterns = [
    #  /board/create/, /board/, /board/1/, /board/1/update/, /board/1/delete/
    path('create/', views.create_article, name='create_article'), # article create
    path('', views.article_index, name='article_index'),
    path('<int:article_pk>/', views.article_detail, name='article_detail'),
    path('<int:article_pk>/update/', views.update_article, name='update_article'),
    path('<int:article_pk>/delete/', views.delete_article, name='delete_article'),

    # /board/1/comments/create/
    path(f'{comment_prefix}/create/', views.create_comment, name='create_comment'),  # CREATE comment
    # /board/1/ => READ comment
    # /board/1/comments/1/update/ => UPDATE comment
    path(f'{comment_prefix}/<int:comment_pk>/update/', views.update_comment, name='update_comment'),
    # /board/1/comments/1/delete/ => DELETE comment
    path(f'{comment_prefix}/<int:comment_pk>/delete/', views.delete_comment, name='delete_comment'),
]

