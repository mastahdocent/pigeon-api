from rest_framework import serializers
from .models import Letter


class LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = [
            'id',
            'content',
        ]

    def validate_content(self, value):
        if len(value) > 280:
            raise serializers.ValidationError("Content is too long.")
        return value
