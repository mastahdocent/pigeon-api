from rest_framework import generics

from .models import Letter
from .serializers import LetterSerializer


class LettersView(generics.ListCreateAPIView):
    serializer_class = LetterSerializer
    queryset = Letter.objects.all()


class LetterItemView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LetterSerializer
    queryset = Letter.objects.all()
    lookup_field = 'id'
