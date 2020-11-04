from django.conf.urls import url
from django.urls import path, include
from .api import ProductList, ProductDetail
urlpatterns = [
    path('api/product',ProductList.as_view()),
    path('api/product/<int:pk>',ProductDetail.as_view()),
  
]