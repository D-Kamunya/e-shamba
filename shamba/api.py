from rest_framework.response import Response
from rest_framework import generics
from .serializer import CropSerializer
from .models import Crop

# Crop Create API
class CropCreateApi(generics.CreateAPIView):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer


# Crop List API
class CropApi(generics.ListAPIView):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer


class CropDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer