#encoding:UTF-8
from django.conf.urls import patterns, url, include
from posts.api import BlogsAPIView, PostsViewSet, NewPostApi
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts/(?P<username>[\w.@+-]+)', PostsViewSet, base_name="api-posts")

urlpatterns = patterns('',
    # api urls
    url(r'', include(router.urls)),
    url(r'blogs/$', BlogsAPIView.as_view()),
    url(r'new_post/$', NewPostApi.as_view()),
)