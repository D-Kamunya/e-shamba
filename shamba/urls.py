from django.urls import path
from .api import CropApi,CropDetailApi,UsersCropListApi,ScheduleUpdateApi,ScheduleAPI,PostListApi,PostUpdateApi,ProductList, ProductDetail,RecList,RecDetail,CropPrdList,CropPrdDetail,PostCommentList,PostCommentDetail,CropActivityList,CropActivityDetail


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
    path('api/product_recommendations',RecList.as_view()),
    path('api/product_recommendations/<int:pk>',RecDetail.as_view()),
    path('api/crop_product', CropPrdList.as_view()),
    path('api/crop_product/<int:pk>',CropPrdDetail.as_view()),
    path('api/post_comment', PostCommentList.as_view()),
    path('api/post_comment/<int:pk>',PostCommentDetail.as_view()),
    path('api/crop_activity', CropActivityList.as_view()),
    path('api/crop_activity/<int:pk>',CropActivityDetail.as_view()),
]

