from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Task

class TaskAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_create_task(self):
        url = reverse('task-create')
        data = {
            "name": "Fix login bug",
            "description": "Resolve the issue preventing users from logging in.",
            "task_type": "BUG",
            "assigned_user_ids": [self.user.id]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_assign_task(self):
        task = Task.objects.create(name="Sample Task", description="Just a sample")
        url = reverse('task-assign', args=[task.id])
        data = {
            "assigned_user_ids": [self.user.id]
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_tasks(self):
        task = Task.objects.create(name="Sample Task", description="Just a sample")
        task.assigned_users.add(self.user)
        url = reverse('user-tasks', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
