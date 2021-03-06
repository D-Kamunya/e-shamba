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


from .models import Prod_rec
from .serializer import ProductRecSerializer

from .models import Crop_prd
from .serializer import CropPrdSerializer

from .models import Post_Comment
from .serializer import PostCommentSerializer

from .models import Crop_activity
from .serializer import CropActivitySerializer
# schedule Create API

class ScheduleAPI(generics.ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer



# schedule Update API
class ScheduleUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class UserScheduleListApi(generics.ListAPIView):
    
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        """
        This view should return a list of all the crops
        for the user.
        """
        queryset = Schedule.objects.all()
        userid = self.request.query_params.get('userid', None)
        if userid is not None:
            queryset = queryset.filter(user_id=userid)
        return queryset 

# Crop List API
class CropApi(generics.ListCreateAPIView):
    
    queryset = Crop.objects.all()
    serializer_class = CropSerializer


class CropDetailApi(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Crop.objects.all()
    serializer_class = CropSerializer



class UsersCropListApi(generics.ListAPIView):
    
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

# Product API
class ProductList(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer 


# Product Recommendation API
class RecList(generics.ListCreateAPIView):
  queryset = Prod_rec.objects.all()
  serializer_class = ProductRecSerializer

class RecDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Prod_rec.objects.all()
  serializer_class = ProductRecSerializer 


# Crop Product API
class CropPrdList(generics.ListCreateAPIView):
  queryset = Crop_prd.objects.all()
  serializer_class = CropPrdSerializer

class CropPrdDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Crop_prd.objects.all()
  serializer_class = CropPrdSerializer



#Post comment API
class PostCommentList(generics.ListCreateAPIView):
  queryset = Post_Comment.objects.all()
  serializer_class = PostCommentSerializer

class PostCommentDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Post_Comment.objects.all()
  serializer_class = PostCommentSerializer




#Crop Activity  API
class CropActivityList(generics.ListCreateAPIView):
  queryset = Crop_activity.objects.all()
  serializer_class = CropActivitySerializer

class CropActivityDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Crop_activity.objects.all()
  serializer_class = CropActivitySerializer 


