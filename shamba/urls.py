from django.urls import path
from .api import CropApi,CropDetailApi,UsersCropListApi,ScheduleUpdateApi,ScheduleAPI,PostListApi,PostUpdateApi,ProductList, ProductDetail


urlpatterns = [
    path('api/schedule',ScheduleAPI.as_view()),
    path('api/schedule/<int:pk>',ScheduleUpdateApi.as_view()),
    path('api/crop',CropApi.as_view()),
    path('api/crop/<int:pk>',CropDetailApi.as_view()),
    path('api/crops/user/<int:pk>',UsersCropListApi.as_view()),
    path('api/post',PostListApi.as_view()),
    path('api/post/<int:pk>',PostUpdateApi.as_view()),
    path('api/product',ProductList.as_view()),
    path('api/product/<int:pk>',ProductDetail.as_view()),
]

