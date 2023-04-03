from rest_framework import permissions


class IsSuperownerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return (
            request.user.is_superuser
            if not request.method in ("PUT", "DELETE")
            else False
        )


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif not request.method in ("PUT", "DELETE"):
            return request.user.is_superuser

        return obj.owner == request.user
