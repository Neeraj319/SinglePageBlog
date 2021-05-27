from django.shortcuts import render
from rest_framework import serializers
from rest_framework import authentication
from .serializers import BlogSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Blog , Comment
from rest_framework import status
from rest_framework.response import Response
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
class AllBolgView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get(self , request):
        blogs = Blog.objects.all().order_by('-date_created')
        serializer = BlogSerializer(blogs,many = True)
        return Response(serializer.data , status = status.HTTP_200_OK)
    def post(self , request):
        serializer = BlogSerializer(data = request.data , context = {"user" : request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            print(serializer)
            print(serializer.errors)
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
