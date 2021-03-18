from django.urls import path, include

urlpatterns = [
    path('new/', views.new, name='new'),
    path('', views.index, name='index'),
    path('<int:board_pk>/', views.detail, name='detail'),
    path('<int:board_pk>/edit/', views.edit, name='edit'),
    path('<int:board_pk>/delete', views.delete, name='delete')
]
