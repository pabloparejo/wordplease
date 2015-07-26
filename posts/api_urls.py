#encoding:UTF-8
from django.conf.urls import patterns, url, include
from posts.api import BlogsAPIView, PostsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostsViewSet, base_name="")

urlpatterns = patterns('',
    # api urls
    url(r'', include(router.urls)),
    url(r'blogs/', BlogsAPIView.as_view()),
    url(r'blogs/(?P<username>[\w.@+-]+)', BlogsAPIView.as_view(), name="blog"),
)