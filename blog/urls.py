from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog),
    path('posts/', views.posts),
    path('posts/<name_post>', views.info_post),
]