from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'avatar',
            'last_login',
            'date_joined'
        ]
        read_only_fields = [
            'id',
            'username',
            'email',
            'last_login',
            'date_joined'
        ]

class UserStubSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'avatar'
        ]
        read_only_fields = fields
