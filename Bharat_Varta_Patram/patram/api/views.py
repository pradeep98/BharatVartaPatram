from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .serializers import PostSerializers
from patram.models import Post
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

class PostList(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get(self, request, format=None):
        post = Post.objects.all()
        serializer = PostSerializers(post, many=True)
        return Response(serializer.data)

class PostDetail(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializers(post)
        return Response(serializer.data)

class PostEdit(APIView):
    permission_classes = [IsAuthenticated,]
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        post = self.get_object(pk)

        if post.author != request.user:
            return Response({'message':'Permission Denied!'})

        serializer = PostSerializers(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        
        if post.author != request.user:
            return Response({'message':'Permission Denied!'})

        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PostCreate(APIView):
    permission_classes = [IsAuthenticated,]
    def post(self, request, format=None):
        post = Post(author=request.user)

        serializer = PostSerializers(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
