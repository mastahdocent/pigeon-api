from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import generics, pagination

from .serializers import UserSerializer

User = get_user_model()

class UsersView(generics.ListAPIView):
    serializer_class = UserSerializer
    search_fields = ('username')
    ordering_fields = ('username')
    queryset = User.objects.filter(is_active=True)

    def get_serializer_context(self):
        return {'request': self.request}

class UserItemView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_active=True)
    lookup_field = 'id'

    def get_serializer_context(self):
        return {'request': self.request}
