from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Task
from .serializers import UserSerializer, TaskSerializer, TaskAssignmentSerializer
from django.shortcuts import get_object_or_404

class CreateTaskView(APIView):
    """API to create a new task"""
    
    @swagger_auto_schema(
        request_body=TaskSerializer,
        operation_description="Creates a new task with the provided details",
        responses={
            201: openapi.Response('Created', TaskSerializer),
            400: openapi.Response('Bad Request')
        },
        tags=['Tasks']
    )
    def post(self, request):
        """
        Create a new task with provided details.
        """
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssignTaskView(APIView):
    """API to assign a task to one or multiple users"""
    
    @swagger_auto_schema(
        request_body=TaskAssignmentSerializer,
        operation_description="Assigns a task to one or multiple users",
        responses={
            200: openapi.Response('Success', TaskSerializer),
            400: openapi.Response('Bad Request'),
            404: openapi.Response('Not Found')
        },
        tags=['Tasks']
    )
    def post(self, request):
        """
        Assign a task to one or multiple users.
        """
        serializer = TaskAssignmentSerializer(data=request.data)
        if serializer.is_valid():
            task_id = serializer.validated_data['task_id']
            user_ids = serializer.validated_data['user_ids']
            
            try:
                task = Task.objects.get(id=task_id)
            except Task.DoesNotExist:
                return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
            
            # Clear existing assignments and add new ones
            task.assigned_to.clear()
            
            for user_id in user_ids:
                try:
                    user = User.objects.get(id=user_id)
                    task.assigned_to.add(user)
                except User.DoesNotExist:
                    return Response({"error": f"User with id {user_id} not found"}, 
                                   status=status.HTTP_404_NOT_FOUND)
            
            return Response(TaskSerializer(task).data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserTasksView(APIView):
    """API to get tasks with their details for a specific user"""
    
    @swagger_auto_schema(
        operation_description="Retrieves all tasks assigned to a specific user",
        responses={
            200: openapi.Response('Success', TaskSerializer(many=True)),
            404: openapi.Response('User Not Found')
        },
        tags=['Users']
    )
    def get(self, request, user_id):
        """
        Retrieve all tasks assigned to a specific user.
        """
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        tasks = user.assigned_tasks.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)