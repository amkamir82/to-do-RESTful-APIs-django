from django.db import models
from todo.models import user


class Project(models.Model):
    name = models.CharField(max_length=250, blank=False)
    manager = models.ForeignKey(user.User, on_delete=models.CASCADE, related_name='manager_projects')
    developers = models.ManyToManyField(user.User, related_name='projects', default=list)
