from django.urls import path
from . import views

urlpatterns = [
    # path('test/', views.test)
    path('articles/', include('articles.urls'))
]