from rest_framework import serializers
from .models import Letter
from ..serializers import UserStubSerializer

class LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = [
            'id',
            'sender',
            'recipient',
            'sent_on',
            'status',
            'content',
        ]
        read_only_fields = [
            'id',
            'sender',
            'sent_on',
        ]

    def validate_content(self, value):
        if len(value) > 280:
            raise serializers.ValidationError("Content is too long.")
        return value

    def validate_status(self, value):
        #request = self.context["request"]
        new_status = value
        prev_status = self.instance.status

        # status validation depending on current letter state
        if prev_status is not None and new_status is not None:
            if prev_status == Letter.DRAFT_STATUS:
                if new_status not in [Letter.DRAFT_STATUS, Letter.SENT_STATUS]:
                    raise serializers.ValidationError(
                        "Selected status is not allowed in current object state")
            elif prev_status in [Letter.SENT_STATUS, Letter.READ_STATUS]:
                if new_status != [Letter.READ_STATUS]:
                    raise serializers.ValidationError(
                        "Selected status is not allowed in current object state")

        elif new_status is not None:
            # new item is being created
            if new_status not in [Letter.DRAFT_STATUS, Letter.SENT_STATUS]:
                raise serializers.ValidationError(
                        "Selected status is not allowed in current object state")

        return value

class LetterGetSerializer(LetterSerializer):
    sender = UserStubSerializer(read_only=True)
    recipient = UserStubSerializer(read_only=True)