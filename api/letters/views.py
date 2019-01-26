from django.db.models import Q
from django.utils import timezone
from rest_framework import generics, pagination

from .models import Letter
from .permissions import IsLetterRecipient, IsLetterSender, IsLetterSenderOrRecipient
from .serializers import LetterSerializer


class LettersView(generics.ListCreateAPIView):
    serializer_class = LetterSerializer
    search_fields = ('recipient__username', 'content')
    ordering_fields = ('recipient__username', 'created_on', 'sent_on')

    def get_queryset(self):
        return Letter.objects.for_user(self.request.user)

    def get_serializer_context(self):
        return {'request': self.request}

    def perform_create(self, serializer):
        # authenticated user can only send letters on his own behalf
        serializer.save(sender=self.request.user)


class LetterItemView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsLetterSenderOrRecipient |
        IsLetterSender |
        IsLetterRecipient
    ]

    serializer_class = LetterSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Letter.objects.for_user(self.request.user)

    def get_serializer_context(self):
        return {'request': self.request}

    def perform_destroy(self, instance):
        if self.request.user == instance.sender:
            obj = Letter.objects.get(id=instance.id)
            obj.sender_deleted = True
            obj.sender_deleted_on = timezone.now()
            obj.save()
        elif self.request.user == instance.recipient:
            obj = Letter.objects.get(id=instance.id)
            obj.recipient_deleted = True
            obj.recipient_deleted_on = timezone.now()
            obj.save()