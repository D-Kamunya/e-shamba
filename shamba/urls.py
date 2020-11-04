from django.urls import path
from .api import CropCreateApi,CropApi,CropDetailApi,UsersCropListApi,ScheduleCreateApi, ScheduleUpdateApi, ScheduleDeleteApi,ScheduleAPI,ScheduleUserApi,PostListApi, PostDetailsApi, PostUpdateApi, PostDeleteApi, PostCreateApi


urlpatterns = [
    path('api/schedules/<int:pk>',ScheduleAPI.as_view()),
    path('api/schedule/<int:pk>/update',ScheduleUpdateApi.as_view()),
    path('api/schedule/create',ScheduleCreateApi.as_view()),
    path('api/schedule/user/<int:pk>',ScheduleUserApi.as_view()),
    path('api/schedule/<int:pk>/delete',ScheduleDeleteApi.as_view())
    path('api/crops',CropApi.as_view()),
    path('api/crop/create',CropCreateApi.as_view()),
    path('api/crop/<int:pk>',CropDetailApi.as_view()),
    path('api/crops/user/<int:pk>',UsersCropListApi.as_view()),
    path('api/post',PostListApi.as_view()),
    path('api/post/create',PostCreateApi.as_view()),
    path('api/post/<int:pk>',PostUpdateApi.as_view()),
    path('api/post/<int:pk>', PostDetailsApi.as_view()),
    path('api/post/<int:pk>/delete',PostDeleteApi.as_view()),
]

