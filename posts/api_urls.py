#encoding:UTF-8
from django.conf.urls import patterns, url, include
from posts.api import BlogsAPIView
from rest_framework.routers import DefaultRouter

urlpatterns = patterns('',
    # api urls
    url(r'blogs/', BlogsAPIView.as_view()),
    url(r'blogs/(?P<username>[\w.@+-]+)', BlogsAPIView.as_view(), name="api_blog"),
)