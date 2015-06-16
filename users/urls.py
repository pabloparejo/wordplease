from django.conf.urls import include, url
from users import views


urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name="login"),
    url(r'^logout/$', 'users.views.logout', name="logout"),
    url(r'^signup/$', views.SignupView.as_view(), name="signup"),
]
