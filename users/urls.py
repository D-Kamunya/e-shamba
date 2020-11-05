from django.conf.urls import url
from django.urls import path, include
from .api import RegisterApi,UserApi,UserDetailApi,ProfileApi,ProfileDetailApi
urlpatterns = [
      path('api/register', RegisterApi.as_view()),
      path('api/user', UserApi.as_view()),
      path('api/user/<int:pk>',UserDetailApi.as_view()),
      path('api/profile', ProfileApi.as_view()),
      path('api/profile/<int:pk>',ProfileDetailApi.as_view()),
]