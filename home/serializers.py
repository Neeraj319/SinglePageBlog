from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Blog, Comment
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            # 'id'
        ]


class BlogSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    likes = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Blog
        fields = ["id", "title", "body", "likes", "user", "category"]

    def create(self, validated_data):
        user = self.context.get("user")
        validated_data["user"] = user
        blogs = Blog.objects.create(**validated_data)
        return blogs


class AddCommentSerializer(serializers.ModelSerializer):
    blog = BlogSerializer(required=False)
    user = UserSerializer(required=False)

    class Meta:
        model = Comment
        fields = [
            "user",
            "blog",
            "text",
            # "like",
            "id",
        ]

    def create(self, validated_data):
        user = self.context.get("user")
        blog = self.context.get("blog")
        validated_data["blog"] = blog
        validated_data["user"] = user

        validated_data["blog"] = blog
        return Comment.objects.create(**validated_data)


class CommentSerializer(serializers.ModelSerializer):
    like = UserSerializer(read_only=True, many=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "text", "like", "user"]


class BlogLikeSerializer(serializers.ModelSerializer):
    likes = UserSerializer(required=False, many=True)

    class Meta:
        model = Blog
        fields = ["likes"]

    def create(self, validated_data):
        user = self.context.get("user")
        blog = self.context.get("blog")
        if user in blog.likes.all():
            blog.likes.remove(user)
        else:
            blog.likes.add(user)
        return blog.likes.all()
