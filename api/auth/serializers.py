from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    message = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
            'password',
            'password2',
            'message'
        ]

    def validate_username(self, value):
        qs = get_user_model().objects.filter(username__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(
                "This username is already registered")
        return value

    def validate_email(self, value):
        qs = get_user_model().objects.filter(email__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(
                "This e-mail is already registered")
        return value

    def validate(self, data):
        if data.get('password') != data.get('password2'):
            raise serializers.ValidationError("Password don't match")
        return data

    def create(self, validated_data):
        vd = validated_data
        user = get_user_model()(
            username=vd.get('username'),
            email=vd.get('email')
        )
        user.set_password(vd.get('password'))
        user.avatar = None
        #user.is_active = False
        user.save()
        return user

    def get_message(self, obj):
        return "Registration was successful"
