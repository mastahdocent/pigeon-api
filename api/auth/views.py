from django.contrib.auth import get_user_model
from django.contrib.auth.models import update_last_login
from django.db.models import Q

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings

from .serializers import UserRegisterSerializer

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER
JWT_RESPONSE_PAYLOAD_HANDLER = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({'message': 'You are already authenticated'}, status=400)
        
        username = request.data.get('username')
        password = request.data.get('password')

        # authenticate via either username or email
        qs = get_user_model().objects.filter(
            Q(username__iexact=username)|
            Q(email__iexact=username)
        ).distinct()

        if qs.count() == 1:
            user = qs.first()
            if user.check_password(password):
                # authentication successful
                update_last_login(None, user) # is it the best way?
                # return the username and its jwt
                payload = JWT_PAYLOAD_HANDLER(user)
                token = JWT_ENCODE_HANDLER(payload)
                response = JWT_RESPONSE_PAYLOAD_HANDLER(token, user, request=request)
                return Response(response)

        return Response({'message': 'Invalid credentials supplied'}, status=401)


class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_context(self):
        return {'request': self.request}
