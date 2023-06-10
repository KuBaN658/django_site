from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog),
    path('posts/', views.posts),
    path('posts/<int:num>', views.get_by_num),
    path('posts/guinnessworldrecords', views.get_guinness_world_records),
    path('posts/<name_post>', views.get_by_name),
]