from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

__author__ = 'parejo'



class UserSerializer(ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "username", "email", "password")