from .models import Post
from rest_framework import generics
from rest_framework.response import Response
from .serializer import PostSerializer


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