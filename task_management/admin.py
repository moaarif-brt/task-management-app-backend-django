from django.contrib import admin
from .models import User, Task

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'mobile', 'created_at')
    search_fields = ('name', 'email', 'mobile')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'task_type', 'status', 'created_at')
    list_filter = ('status', 'task_type')
    search_fields = ('name', 'description')
    filter_horizontal = ('assigned_to',)