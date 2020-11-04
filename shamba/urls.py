from django.urls import path
from .api import ScheduleCreateApi, ScheduleUpdateApi, ScheduleDeleteApi,ScheduleAPI
urlpatterns = [
    path('api/schedules',ScheduleAPI.as_view()),
    path('api/schedule/<int:pk>/update',ScheduleUpdateApi.as_view()),
    path('api/schedule/create',ScheduleCreateApi.as_view()),
    
    path('api/schedule/<int:pk>/delete',ScheduleDeleteApi.as_view())
]