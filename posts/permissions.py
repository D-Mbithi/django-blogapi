from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Custom API permission to allow only author to delete and edit."""

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
