from django.urls import path
from .views import create_post, post_list, like_post, delete_post

urlpatterns = [
    path("create/", create_post, name="create_post"),
    path("", post_list, name="post_list"),
    path('like/<int:post_id>/', like_post, name='like_post'),
    path('post/delete/<int:post_id>/', delete_post, name='delete_post'),
]
