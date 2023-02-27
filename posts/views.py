from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import  Post
from .serializers import PostSerializer


class PostListApiView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

