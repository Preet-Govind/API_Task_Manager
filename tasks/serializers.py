from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class TaskSerializer(serializers.ModelSerializer):
    assigned_users = UserSerializer(many=True, read_only=True)
    assigned_user_ids = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True, many=True)

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'created_at', 'task_type', 'completed_at', 'status', 'assigned_users', 'assigned_user_ids']

    def create(self, validated_data):
        assigned_users = validated_data.pop('assigned_user_ids')
        task = Task.objects.create(**validated_data)
        task.assigned_users.set(assigned_users)
        return task
