
from django.conf.urls import include, url
from posts import views


urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/$', views.PostListView.as_view(), name="posts"),
    url(r'^posts/(?P<username>[\w.@+-]+)/(?P<pk>[0-9]+)$', views.PostListView.as_view(), name="post")
]
