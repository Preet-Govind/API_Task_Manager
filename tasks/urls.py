from django.urls import path
from .views import TaskCreateView, TaskAssignView, UserTaskListView

urlpatterns = [
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/assign/', TaskAssignView.as_view(), name='task-assign'),
    path('users/<int:user_id>/tasks/', UserTaskListView.as_view(), name='user-tasks'),
]
