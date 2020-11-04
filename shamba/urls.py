
from django.urls import path, include
from .api import PostListApi, PostDetailsApi, PostUpdateApi, PostDeleteApi, PostCreateApi



urlpatterns = [
    path('api/post',PostListApi.as_view()),
    path('api/post/create',PostCreateApi.as_view()),
    path('api/post/<int:pk>',PostUpdateApi.as_view()),
    path('api/post/<int:pk>', PostDetailsApi.as_view()),
    path('api/post/<int:pk>/delete',PostDeleteApi.as_view()),
]
