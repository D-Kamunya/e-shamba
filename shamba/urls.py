from .api import CreatePostApi, PostApi, PostUpdateApi, PostDetailsApi
from django.urls import path, include
#from .api import CropCreateApi,CropApi,CropUpdateApi,CropDeleteApi

urlpatterns = [
    createPost, PostDetails, PostList, UpdatePost, DeletePost
    #path('api/crops',CropApi.as_view()),
    #path('api/crop/create',CropCreateApi.as_view()),
    #path('api/crop/<int:pk>/update',CropUpdateApi.as_view()),
    #path('api/crop/<int:pk>/delete',CropDeleteApi.as_view()),
]

urlpatterns = [
    path('api',PostListApi.as_view()),
    path('api/create',PostCreateApi.as_view()),
    path('api/<int:pk>',PostUpdateApi.as_view()),
    path('api/<int:pk>', PostDetailsApi.as.view()),
    path('api/<int:pk>/delete',PostDeleteApi.as_view()),
]