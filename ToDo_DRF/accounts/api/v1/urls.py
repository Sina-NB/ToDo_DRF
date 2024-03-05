from django.urls import path
from .views import LoginApiView, RegisterApiView, LogoutApiView

app_name = "api-v1"

urlpatterns = [
    path("register", RegisterApiView.as_view(), name="register-api"),
    path("login", LoginApiView.as_view(), name="login-api"),
    path("logout", LogoutApiView.as_view(), name="logout-api"),
]
