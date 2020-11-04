from django.conf.urls import url
from django.urls import path, include
from .api import CropCreateApi,CropApi,CropDetailApi,UsersCropListApi


urlpatterns = [
    path('api/crops',CropApi.as_view()),
    path('api/crop/create',CropCreateApi.as_view()),
    path('api/crop/<int:pk>',CropDetailApi.as_view()),
    path('api/crops/user/<int:pk>',UsersCropListApi.as_view()),
]