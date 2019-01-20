from django.db.models import Q
from rest_framework import generics

from .models import Letter
from .permissions import IsLetterRecipient, IsLetterSender, IsLetterSenderOrRecipient
from .serializers import LetterSerializer


class LettersView(generics.ListCreateAPIView):
    serializer_class = LetterSerializer

    def get_queryset(self):
        user = self.request.user
        # return only those letters where:
        # - user is a sender and letter is not deleted
        # - user is a recipient, letter is not unsent and is not delted
        return Letter.objects.filter(
            (
                Q(sender=user) &
                Q(sender_deleted=False)
            ) |
            (
                Q(recipient=user) &
                Q(recipient_deleted=False) &
                Q(status__in=[Letter.SENT_STATUS, Letter.READ_STATUS])
            )
        )

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
    queryset = Letter.objects.all()
    lookup_field = 'id'
