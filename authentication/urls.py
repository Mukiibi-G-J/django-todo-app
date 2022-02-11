from django.urls import path

from .views import RegsiterAPIView, LoginAPIView


urlpatterns = [
    path('register', RegsiterAPIView.as_view(), name="register"),
    path("login", LoginAPIView.as_view(), name="login")
]
