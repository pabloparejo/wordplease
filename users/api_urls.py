#encoding:UTF-8
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from users.api import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = patterns('',
    # api urls
    url(r'', include(router.urls)),
)