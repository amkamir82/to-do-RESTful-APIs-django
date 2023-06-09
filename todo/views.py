from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer, TaskSerializer
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.views import APIView
from .serializers import ProjectSerializer
from .models import Project
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import logout
from .permissions import IsManager, CanAddTaskToProject, CanAddProjectToDeveloper, CanAssignTask
from .models import Task, User
from .serializers import DeveloperProjectSerializer, TasksOfProjectSerializer, TaskAssignmentSerializer


class UserSignupView(generics.CreateAPIView):
    serializer_class = UserSerializer


class AddProjectView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsManager,)

    def perform_create(self, serializer):
        serializer.save(manager=self.request.user)


class AddProjectToDeveloperView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = DeveloperProjectSerializer
    permission_classes = (IsManager, CanAddProjectToDeveloper)


class AddTaskView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, CanAddTaskToProject,)


class AssignTaskView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskAssignmentSerializer
    permission_classes = (IsAuthenticated, CanAssignTask,)


class ProjectTaskListView(generics.ListAPIView):
    serializer_class = TasksOfProjectSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return Task.objects.filter(project_id=project_id)


class UserProjectTaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        project_id = self.kwargs['project_id']
        return Task.objects.filter(project_id=project_id, assignees=user)


class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if request.user and user == request.user:
            return JsonResponse({'error': 'Already logged in'}, status=status.HTTP_200_OK)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserLogoutView(APIView):
    def post(self, request):
        try:
            logout(request)
            return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
