#encoding:UTF:8
from django.contrib.auth.models import User
from posts.models import Post
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from users.serializers import UserSerializer


class BlogSerializer(ModelSerializer):
    blog = serializers.HyperlinkedIdentityField(view_name="api-posts-list",
                                                read_only=True,
                                                lookup_field="username")

    class Meta:
        model = User
        fields = ("blog",)


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        exclude = ("author",)

class PostDetailSerializer(PostSerializer):
    author = UserSerializer(read_only=True)
    categories = serializers.SlugRelatedField("title", read_only=True, many=True)


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("pk", "title", "image", "summary", "pub_date")
