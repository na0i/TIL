from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('articles/', views.article_list_or_create),
    path('articles/<int:article_pk>', views.article_detail_or_update_or_delete),
    path('articles/<int:article_pk>/comments/', views.create_comment),
    path('articles/<int:article_pk>/comments/<int:comment_pk>', views.update_or_delete_comment)
]
