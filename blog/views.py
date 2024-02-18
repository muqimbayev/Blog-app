from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from blog.models import CustomUser, Blog, Like, Comment
from rest_framework.permissions import IsAuthenticated
from blog.serializers import CommentSerializer, CustomUserSerializer, BlogSerializer, LikeSerializer
# Create your views here.

class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_class = [IsAuthenticated]

class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer