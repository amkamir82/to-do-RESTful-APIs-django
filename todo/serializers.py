from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Project
from .models.task import Task

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = ('manager', 'developers',)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('name', 'project',)


class TaskAssignmentSerializer(serializers.ModelSerializer):
    assignees = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

    class Meta:
        model = Task
        fields = ['assignees']


class DeveloperProjectSerializer(serializers.ModelSerializer):
    projects = serializers.PrimaryKeyRelatedField(many=True, queryset=Project.objects.all())

    class Meta:
        model = User
        fields = ['projects']


class TasksOfProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
