from django.urls import path, include
from .views import IndexView

app_name = "accounts"

urlpatterns = [
    path("", IndexView.as_view(), name="index-page"),
]
