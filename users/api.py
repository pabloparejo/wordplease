from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from users.permissions import UserPermission
from users.serializers import UserSerializer

__author__ = 'parejo'


class UserViewSet(ModelViewSet):
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (UserPermission,)

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def perform_create(self, serializer):
        password = serializer.validated_data.get("password")
        serializer.save(password=make_password(password))