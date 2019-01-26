from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    message = "This operation is restricted to this user only."

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user