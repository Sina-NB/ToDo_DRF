from django.urls import path, include
from .views import IndexView

app_name = "todo"

urlpatterns = [
    path("", IndexView.as_view(), name="index-page"),
    path("todo/api/v1/", include("todo.api.v1.urls")),
]
