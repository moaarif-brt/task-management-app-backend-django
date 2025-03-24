from rest_framework import serializers
from .models import User, Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'mobile', 'created_at']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'created_at', 'completed_at', 
                 'task_type', 'status', 'assigned_to']

class TaskAssignmentSerializer(serializers.Serializer):
    task_id = serializers.IntegerField()
    user_ids = serializers.ListField(
        child=serializers.IntegerField()
    )