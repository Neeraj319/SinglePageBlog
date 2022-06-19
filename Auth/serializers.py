from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    """
    serializer for UserProfile model
    """

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email"]
