from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .serializers import UserRegistrationSerializers
from django.contrib.auth.models import User
from users.models import Profile
from rest_framework.authtoken.models import Token


class UserRegistrationApi(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
    
    def post(self, request, format=None):
        print('inside view post')
        serializer = UserRegistrationSerializers(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get(user=user).key
            data = {}
            data['token'] = token
            data['username'] = serializer.data['username']
            data['email'] = serializer.data['email']
            return Response(data, status=status.HTTP_201_CREATED)
        print(serializer.errors," ----- ")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


