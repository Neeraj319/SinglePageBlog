from django.db import models
from rest_framework import serializers
from .models import Blog
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            # 'id'
        ]

class BlogSerializer(serializers.ModelSerializer):
    user = UserSerializer(required = False)
    likes = UserSerializer(read_only = True , many = True)
    class Meta:
        model = Blog
        fields = [
            'title',
            'body',
            'likes',
            'user'
        ]
    def create(self, validated_data):
        user = self.context.get('user')
        # user = user['username']
        validated_data['user'] = user
        blogs = Blog.objects.create(**validated_data)
        return blogs
