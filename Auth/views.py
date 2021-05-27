from django.shortcuts import render
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class LoginView(APIView):
    def post(self , request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(username , password)
        user = authenticate(username = username , password = password)
        if user is not None:
            token , _ = Token.objects.get_or_create(user = user)
            return Response(token.key , status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


