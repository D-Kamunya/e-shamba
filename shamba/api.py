from rest_framework.response import Response
from rest_framework import generics,permissions

from .serializer import CropSerializer
from .models import Crop

from .serializer import ScheduleSerializer
from .models import Schedule

from .serializer import PostSerializer
from .models import Post

from .models import Product
from .serializer import ProductSerializer
# schedule Create API

class ScheduleAPI(generics.ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer



# schedule Update API
class ScheduleUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer



# Crop List API
class CropApi(generics.ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Crop.objects.all()
    serializer_class = CropSerializer


class CropDetailApi(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Crop.objects.all()
    serializer_class = CropSerializer



class UsersCropListApi(generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = CropSerializer

    def get_queryset(self):
        """
        This view should return a list of all the crops
        for the user.
        """
        queryset = Crop.objects.all()
        userid = self.request.query_params.get('userid', None)
        if userid is not None:
            queryset = queryset.filter(user_id=userid)
        return queryset 
      
      

# Post List API
class PostListApi(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
# Post Update API
class PostUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

  
class ProductList(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer  

