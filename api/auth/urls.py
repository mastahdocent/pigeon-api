from django.urls import path, include

from .views import LoginView, RegisterView

urlpatterns = [
    path('', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
]
