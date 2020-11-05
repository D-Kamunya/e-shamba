from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializer import RegisterSerializer, UserSerializer,ProfileSerializer
from django.contrib.auth.models import User
from .models import Profile
#Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,    context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })




# User Api
class UserApi(generics.ListAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailApi(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer        


# Crop List API
class ProfileApi(generics.ListAPIView):
    
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetailApi(generics.RetrieveUpdateDestroyAPIView):


    serializer_class = ProfileSerializer
    def get_queryset(self):
        """
        This view should return a list of all the crops
        for the user.
        """
        queryset = Profile.objects.all()
        userid = self.request.query_params.get('userid', None)
        if userid is not None:
            queryset = queryset.filter(user_id=userid)
        return queryset 

    


