from rest_framework.permissions import BasePermission

from todo.models import Task, User


class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "1"


class CanAddTaskToProject(BasePermission):
    def has_permission(self, request, view):
        project_id = request.data.get('project')
        user = request.user
        print(project_id)
        if user.role == "1":
            if user.manager_projects.filter(id=project_id).exists():
                return True
        elif user.role == "2":
            if user.projects.filter(id=project_id).exists():
                return True

        return False


class CanAddProjectToDeveloper(BasePermission):
    def has_permission(self, request, view):
        project_id = view.kwargs.get('project_id')
        user = request.user

        if user.manager_projects.filter(id=project_id).exists():
            return True

        return False


class CanAssignTask(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        assignee = request.data.get("assignees")[0]
        task = Task.objects.all().get(id=int(view.kwargs.get("pk")))

        if user.role == '1':
            if user.manager_projects.filter(id=task.project.id).exists():
                try:
                    developer = User.objects.get(id=int(assignee))
                    if developer.projects.filter(id=task.project.id).exists():
                        return True
                except Exception as e:
                    return False
        elif user.role == '2':
            if int(user.id) != assignee:
                return False
            try:
                developer = User.objects.get(id=int(assignee))
                if developer.projects.filter(id=task.project.id).exists():
                    return True
            except:
                return False
        return False
