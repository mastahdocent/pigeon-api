from django.db import models
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.core.serializers import serialize

User = get_user_model()


class LetterManager(models.Manager):
    def for_user(self, user):
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


class Letter(models.Model):
    # status choices
    DRAFT_STATUS = 0
    SENT_STATUS = 1
    READ_STATUS = 2

    STATUS_CHOICES = (
        (DRAFT_STATUS, 'Draft'),
        (SENT_STATUS, 'Sent'),
        (READ_STATUS, 'Read'),
    )

    # model
    sender = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="+")
    recipient = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="+")
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT_STATUS)
    content = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)
    sent_on = models.DateTimeField(blank=True, null=True)
    read_on = models.DateTimeField(blank=True, null=True)

    recipient_deleted = models.BooleanField(blank=True, default=False)
    recipient_deleted_on = models.DateTimeField(blank=True, null=True)

    sender_deleted = models.BooleanField(blank=True, default=False)
    sender_deleted_on = models.DateTimeField(blank=True, null=True)

    objects = LetterManager()

    def __str__(self):
        return self.content or ""

    def serialize(self):
        return serialize("json", [self])
