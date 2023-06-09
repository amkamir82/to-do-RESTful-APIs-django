from django.db import models
from todo.models.project import Project
from todo.models.user import User


class Task(models.Model):
    name = models.CharField(max_length=250, blank=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    assignees = models.ManyToManyField(User, related_name='tasks')
