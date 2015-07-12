#encoding:UTF:8
from django.contrib.auth.models import User
from posts.serializers import BlogSerializer
from rest_framework.generics import ListAPIView


class BlogsAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = BlogSerializer