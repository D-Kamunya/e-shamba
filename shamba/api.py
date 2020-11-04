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