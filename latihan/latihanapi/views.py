from .models import PostCategory, Post
from rest_framework import viewsets
from .serializers import PostCategorySerializer, PostSerializer
# from django.shortcuts import get_object_or_404


class PostCategoryViewSet(viewsets.ModelViewSet):
    queryset = PostCategory.objects.all()
    serializer_class = PostCategorySerializer

    def get_queryset(self):
        if self.request.user.is_authenticated():
            return PostCategory.objects.filter(created_by=self.request.user)
        else:
            return PostCategory.objects.filter(created_by=0)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated():
            return Post.objects.filter(created_by=self.request.user)
        else:
            return Post.objects.filter(created_by=0)
