from django.urls import path
from .api import ScheduleCreateApi,  ScheduleUpdateApi, ScheduleDeleteApi
urlpatterns = [
    path('api',ScheduleUpdateApi.as_view()),
    path('api/create',ScheduleCreateApi.as_view()),
    
    path('api/<int:pk>/delete',ScheduleDeleteApi.as_view())
]