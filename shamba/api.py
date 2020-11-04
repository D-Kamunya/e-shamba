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

class ScheduleAPI(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class ScheduleCreateApi(generics.CreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
# schedule List API

# schedule Update API
class ScheduleUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
# Schedule Delete API
class ScheduleDeleteApi(generics.DestroyAPIView):
   queryset = Schedule.objects.all()
   serializer_class = ScheduleSerializer


# Crop Create API
class CropCreateApi(generics.CreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Crop.objects.all()
    serializer_class = CropSerializer


# Crop List API
class CropApi(generics.ListAPIView):
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
      
      
# Post Create API
class PostCreateApi(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
# Post List API
class PostListApi(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
# Post Update API
class PostUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
# Post Delete API
class PostDeleteApi(generics.DestroyAPIView):
   queryset = Post.objects.all()
   serializer_class = PostSerializer
# Post Details API
class PostDetailsApi(generics.DestroyAPIView):
   queryset = Post.objects.all()
   serializer_class = PostSerializer

  
class ProductList(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer  

