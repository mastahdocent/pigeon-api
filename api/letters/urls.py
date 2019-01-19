from django.urls import path

from .views import (
    LettersView,
    LetterItemView
)

urlpatterns = [
    path('', LettersView.as_view()),
    path('<int:id>/', LetterItemView.as_view()),
]
