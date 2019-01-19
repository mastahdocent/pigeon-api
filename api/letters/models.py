from enum import Enum

from django.db import models
from django.contrib.auth import get_user_model
from django.core.serializers import serialize

User = get_user_model()

# enums


class LetterStatus(Enum):
    DRAFT = "Draft"
    SENT = "Sent"
    READ = "Read"

# models


class LetterQuerySet(models.QuerySet):
    pass


class LetterManager(models.Manager):
    def get_queryset(self):
        return LetterQuerySet(self.model, using=self._db)


class Letter(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.PROTECT)
    recipient = models.ForeignKey(
        User, on_delete=models.PROTECT)
    status = models.CharField(
        max_length=2,
        choices=[(s, s.value) for s in LetterStatus],
        default=LetterStatus.DRAFT
    )
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
