from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import generics

from .models import Product
from .serializer import ProductSerializer

# Create your views here.


class ProductList(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer