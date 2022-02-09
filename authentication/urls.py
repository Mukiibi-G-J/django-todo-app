from django.urls import path

from .views import RegsiterAPIView


urlpatterns = [
    path('register', RegsiterAPIView.as_view(), name="register")
]
