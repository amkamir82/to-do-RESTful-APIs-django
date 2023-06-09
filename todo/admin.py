from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from todo.models import Task
from todo.models import Project

User = get_user_model()


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'email', 'role']
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Project)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
