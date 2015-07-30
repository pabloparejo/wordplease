#encoding:UTF:8
from django.contrib.auth.models import User
from posts.models import Post
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from users.serializers import UserSerializer


class BlogSerializer(ModelSerializer):
    blog = serializers.HyperlinkedIdentityField(view_name="blog",
                                                read_only=True,
                                                lookup_field="username",
                                                source="username")

    class Meta:
        model = User
        fields = ("blog",)


class PostSerializer(ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = Post


class PostListSerializer(PostSerializer):
    class Meta(PostSerializer.Meta):
        fields = ("pk", "title", "image", "summary", "pub_date")
