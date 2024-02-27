from django.urls import path

from .views import TaskListApiView, TaskDetailApiView

app_name = "api-v1"

urlpatterns = [
    path("task-list/", TaskListApiView.as_view(), name="task_list"),
    path(
        "task-detail/<int:pk>/",
        TaskDetailApiView.as_view(),
        name="task_detail",
    ),
]
