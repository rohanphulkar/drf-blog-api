from django.shortcuts import render
from .serializer import PostSerializer,CommentSerializer
from .models import Post,Comment
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def GetPosts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def AddPost(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors)

@api_view(['GET'])
def GetSinglePost(request, slug):
    post = Post.objects.get(slug=slug)
    if post:
        serializer = PostSerializer(post)
        return Response(serializer.data)
    return Response({"error":"post does not exist"})

@api_view(['UPDATE'])
def UpdatePost(request, id):
    post = Post.objects.get(id=id)
    if post:
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"error":serializer.errors})
    return Response({"error":"post does not exist"})

@api_view(['DELETE'])
def DeletePost(request, id):
    post = Post.objects.get(id=id)
    if post:
        post.delete()
        return Response({"success":"post deleted successfully"})
    return Response({"error":"post does not exist"})

@api_view(['GET'])
def GetComments(request,slug):
    post = Post.objects.filter(slug=slug).first()
    if post:
        comments = Comment.objects.filter(post=post.id)
        serializer = CommentSerializer(comments, many=True)
        if serializer.data:
            return Response(serializer.data)
    return Response({"error":"post does not exist"})