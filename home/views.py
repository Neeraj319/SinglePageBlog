from django.shortcuts import render
from django.urls.conf import path
from rest_framework import serializers
from rest_framework import authentication
from rest_framework import response
from .serializers import (
    BlogSerializer,
    AddCommentSerializer,
    CommentSerializer,
    BlogLikeSerializer,
)
from django.db.models import Q
from rest_framework.views import APIView
from .models import Blog, Comment
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class AllBlogView(APIView):

    authentication_classes = [TokenAuthentication]

    def get(self, request):
        blogs = Blog.objects.all().order_by("-date_created")
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BlogSerializer(data=request.data, context={"user": request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer)
            print(serializer.errors)
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


class PostComment(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self, id):
        post = Blog.objects.get(id=id)
        print(post)
        return post

    def post(self, request, id):
        blog = self.get_queryset(id=id)
        serializer = AddCommentSerializer(
            data=request.data, context={"user": request.user, "blog": blog}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShowCommentsView(APIView):
    def get_queryset(self, id):
        blog = Blog.objects.get(id=id)

        return Comment.objects.filter(blog=blog)

    def get(self, request, id):
        blog = self.get_queryset(id=id)
        serializer = CommentSerializer(blog, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddLikeToBlog(APIView):
    """
    you can check if the user has liked or not by using this endpoint by hitting get request here :)
    """

    authentication_classes = [TokenAuthentication]

    def get_queryset(self, id):
        return Blog.objects.get(id=id)

    def get(self, request, id):
        blog = self.get_queryset(id=id)
        if request.user in blog.likes.all():
            return Response({"liked": True, "likes": len(blog.likes.all())})
        else:
            return Response({"liked": False, "likes": len(blog.likes.all())})

    def post(self, request, id):
        blog = self.get_queryset(id=id)
        serializer = BlogLikeSerializer(
            data=request.data, context={"user": request.user, "blog": blog}
        )
        if serializer.is_valid():
            # print(serializer.data)
            serializer.save()
            if request.user in blog.likes.all():
                return Response({"liked": True, "likes": len(blog.likes.all())})
            else:
                return Response({"liked": False, "likes": len(blog.likes.all())})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FilterSearch(APIView):
    def get_queryset(self, query):
        return Blog.objects.filter(
            Q(category__contains=query) | Q(title__contains=query)
        )

    def get(self, request):
        query = request.GET["query"]
        blogs = self.get_queryset(query=query)
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DetailBlog(APIView):
    def get_queryset(self, id):
        return Blog.objects.get(id=id)

    def get(self, request, id):
        blog = self.get_queryset(id=id)
        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)
