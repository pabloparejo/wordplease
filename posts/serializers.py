#encoding:UTF:8
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class BlogSerializer(ModelSerializer):
    blog = serializers.HyperlinkedIdentityField(view_name="blog",
                                                    read_only=True,
                                                    lookup_field="username",
                                                    source="username")

    class Meta:
        model = User
        fields = ("blog",)
