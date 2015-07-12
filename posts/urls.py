
from django.conf.urls import include, url
from posts import views


urlpatterns = [
    url(r'^$', views.BlogListView.as_view(), name="blogs"),
    url(r'^new-post/$', views.NewPostFormView.as_view(), name="new-post"),
    url(r'^(?P<username>[\w.@+-]+)/$', views.PostListView.as_view(), name="blog"),
    url(r'^(?P<username>[\w.@+-]+)/(?P<pk>[0-9]+)$', views.PostDetailView.as_view(), name="post")
]
