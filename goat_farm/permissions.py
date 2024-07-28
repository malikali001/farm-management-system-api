from rest_framework import permissions


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser


class IsManager(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and not request.user.is_superuser


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and obj == request.user


class IsAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.user_type == 'admin':
            return True
        return obj.manager == request.user
