from home.models import Blog
from home.serializers import BlogSerializer
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserProfileSerializer


class LoginView(APIView):
    """
    This view creates a new token for an authenticated user.

    """

    def post(self, request):
        """
        {"username" : str,
        "password" -> str
        }
        returns a token to if the credentials are valid.
        """
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(token.key, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


class SignUp(APIView):
    """
    This view creates a new user on the database.

    """

    def post(self, request):
        """
        this route creates a new user on the database.
        {
        "username" : str,
        "password" : str
        }

        """
        username = request.data.get("username")
        password = request.data.get("password")
        print(username, password)
        user = User(username=username, password=password)
        user.set_password(password)
        user.save()
        if user:
            return Response(
                {"message": "user created successfully"}, status=status.HTTP_201_CREATED
            )
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


class UserProfile(APIView):
    """
    This view is responsible for updating a user's profile.
    """

    def get_user(self, username):
        """
        returns a user object from the database.
        """
        try:
            return User.objects.get(username=username)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, username):
        """
        returns a user's profile if the user with the given username exists.
        """
        user = self.get_user(username=username)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetUsername(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        """
        returns the username of the user who is currently logged in.
        """
        return Response({"username": request.user.username}, status=status.HTTP_200_OK)


class GetUserBlogs(APIView):
    """
    This view is returns a list of blogs created by the user.

    """

    authentication_classes = [TokenAuthentication]

    def get_queryset(self, user):
        """
        returns a queryset of blogs associated with the user.
        """
        return Blog.objects.filter(user=user)

    def get(self, request):
        """
        returns a list of blogs created by the user.
        """
        blogs = self.get_queryset(user=request.user)
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
