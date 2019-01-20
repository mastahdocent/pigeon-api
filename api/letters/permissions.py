from rest_framework import permissions
from .models import Letter

class IsLetterSender(permissions.BasePermission):
    message = "This operation is restricted to this letter's sender only."

    def has_object_permission(self, request, view, obj):
        if obj.sender == request.user:
            # authenticated user is the letter's sender
            if request.method in ["GET", "DELETE"]:
                return True
            if request.method in ["PUT", "PATCH"]:
                # allow only if the letter is still an unsent draft
                return obj.status == Letter.DRAFT_STATUS
        return False

class IsLetterRecipient(permissions.BasePermission):
    message = "This operation is restricted to this letter's recipient only."

    def has_object_permission(self, request, view, obj):
        if obj.recipient == request.user:
            # authenticated user is the letter's recipient
            if request.method == "GET":
                # allow only if the letter is no longer an unsent draft
                return obj.status != Letter.DRAFT_STATUS
        return False

class IsLetterSenderOrRecipient(permissions.BasePermission):
    message = "This operation is restricted to either party of this letter."

    def has_object_permission(self, request, view, obj):
        if obj.recipient == request.user or obj.sender == request.user:
            # authenticated user is the letter's sender or recipient
            if request.method == "DELETE":
                return True
        return False