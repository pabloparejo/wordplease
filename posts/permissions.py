#encoding:UTF:8
from django.utils import timezone
from rest_framework.permissions import BasePermission


class PostPermissions(BasePermission):
    def has_permission(self, request, view):
        if view.action and view.action.upper() == "CREATE":
            return request.user.is_authenticated()

        return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or obj.author == request.user:
            return True
        elif view.action:
            if view.action.upper() == "RETRIEVE":
                return obj.pub_date >= timezone.now()

        return False
