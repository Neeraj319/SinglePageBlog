from home.models import Blog
from home.serializers import BlogSerializer
from django.contrib.auth import login, logout, authenticate
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from .serializers import UserProfileSerializer
# Create your views here.


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(token.key, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


class SignUp(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(username, password)
        user = User(username=username, password=password)
        user.set_password(password)
        user.save()
        if user:
            return Response({'message': 'user created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


class UserProfile(APIView):
    def get_user(self, username):
        try:
            return User.objects.get(username=username)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request,  username):
        user = self.get_user(username=username)
        print(user)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetUsername(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request):

        return Response({'username': request.user.username}, status=status.HTTP_200_OK)


class GetUserBlogs(APIView):
    authentication_classes = [TokenAuthentication]

    def get_queryset(self, user):
        return Blog.objects.filter(user=user)

    def get(self, request):
        blogs = self.get_queryset(user=request.user)
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
