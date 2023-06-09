from django.urls import path
from .views import UserSignupView, UserLoginView, UserLogoutView
from .views import AddProjectView, AddTaskView, AssignTaskView
from .views import AddProjectToDeveloperView
from .views import ProjectTaskListView, UserProjectTaskListView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='user_signup'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('add_project/', AddProjectView.as_view(), name='add_project'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('add_task/', AddTaskView.as_view(), name='add_task'),
    path('assign_task/<int:pk>/', AssignTaskView.as_view(), name='assign_task'),
    path('add_project_to_developer/<int:pk>/', AddProjectToDeveloperView.as_view(), name='add_project_to_developer'),
    path('projects/<int:project_id>/tasks/', ProjectTaskListView.as_view(), name='project_task_list'),
    path('projects/<int:project_id>/user_tasks/', UserProjectTaskListView.as_view(), name='user_project_task_list'),
]
