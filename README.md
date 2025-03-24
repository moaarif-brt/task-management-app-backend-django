# task-management-app-backend-django
A Django-based RESTful API for managing tasks and user assignments.

Task Management API
A REST API built with Django and Django REST Framework that allows users to create tasks, assign tasks to users, and retrieve tasks assigned to specific users.
Features

Create tasks with name, description, type, and status
Assign tasks to one or multiple users
Retrieve all tasks assigned to a specific user
API documentation with Swagger UI

Setup Instructions
Prerequisites

Python 3.8 or higher
pip (Python package manager)

Installation

Clone the repository:

Copy git clone <repository-url>
cd task-management-project

Create and activate a virtual environment:

Copy python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:

Copy pip install -r requirements.txt

Apply migrations:

Copy python manage.py makemigrations
python manage.py migrate

Create a superuser (optional, for admin access):

Copy python manage.py createsuperuser

Run the development server:

Copy python manage.py runserver
The API will be available at http://127.0.0.1:8000/
API Documentation
Swagger UI
Swagger documentation is available at:

Swagger UI: http://127.0.0.1:8000/swagger/
ReDoc UI: http://127.0.0.1:8000/redoc/

These interfaces provide interactive documentation where you can:

See all available endpoints
View request/response formats
Test API endpoints directly from the browser

API Endpoints
1. Create a Task
Endpoint: POST /api/tasks/create/
Request Body:
jsonCopy{
  "name": "Implement login feature",
  "description": "Create a login form with email and password fields",
  "task_type": "feature",
  "status": "pending"
}
Response:
jsonCopy{
  "id": 1,
  "name": "Implement login feature",
  "description": "Create a login form with email and password fields",
  "created_at": "2025-03-24T10:00:00Z",
  "completed_at": null,
  "task_type": "feature",
  "status": "pending",
  "assigned_to": []
}
2. Assign a Task to Users
Endpoint: POST /api/tasks/assign/
Request Body:
jsonCopy{
  "task_id": 1,
  "user_ids": [1, 2]
}
Response:
jsonCopy{
  "id": 1,
  "name": "Implement login feature",
  "description": "Create a login form with email and password fields",
  "created_at": "2025-03-24T10:00:00Z",
  "completed_at": null,
  "task_type": "feature",
  "status": "pending",
  "assigned_to": [1, 2]
}
3. Get Tasks for a Specific User
Endpoint: GET /api/users/{user_id}/tasks/
Response:
jsonCopy[
  {
    "id": 1,
    "name": "Implement login feature",
    "description": "Create a login form with email and password fields",
    "created_at": "2025-03-24T10:00:00Z",
    "completed_at": null,
    "task_type": "feature",
    "status": "pending",
    "assigned_to": [1, 2]
  }
]
Test Data
You can create test users through the Django admin interface or by using the following management command:
Copy python manage.py shell
Copy from task_management.models import User

# Create test users
user1 = User.objects.create(name="John Doe", email="john@example.com", mobile="1234567890")
user2 = User.objects.create(name="Jane Smith", email="jane@example.com", mobile="0987654321")

print(f"Created users with IDs: {user1.id}, {user2.id}")



Technologies Used

Django 4.2+
Django REST Framework 3.14+
drf-yasg (Swagger/OpenAPI documentation)
SQLite (for development)