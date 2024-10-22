from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(max_length=100, choices=[('BUG', 'Bug'), ('FEATURE', 'Feature')], default='FEATURE')
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[('PENDING', 'Pending'), ('IN_PROGRESS', 'In Progress'), ('COMPLETED', 'Completed')], default='PENDING')
    assigned_users = models.ManyToManyField(User, related_name='tasks')

    def __str__(self):
        return self.name
