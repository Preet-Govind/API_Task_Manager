from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from django.contrib.auth.models import User

# API to create a task
class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# API to assign a task to a user
class TaskAssignView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def update(self, request, *args, **kwargs):
        task = self.get_object()
        user_ids = request.data.get('assigned_user_ids', [])
        task.assigned_users.set(user_ids)
        return super().update(request, *args, **kwargs)

# API to get tasks for a specific user
class UserTaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Task.objects.filter(assigned_users__id=user_id)
