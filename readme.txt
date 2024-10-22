# Task Management API

## Overview
A RESTful API built with Django and Django Rest Framework for managing tasks, assigning them to users, and retrieving tasks based on user assignments.

## Features
- Create tasks with a name and description.
- Assign tasks to one or multiple users.
- Retrieve all tasks assigned to a specific user.

## Requirements
- Python 3.x
- Django 3.x or higher
- Django Rest Framework

## Setup

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd task_management

## Install dependencies
```
pip install -r requirements.txt
```
## Apply migrations
```
python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

```
superuser username : admin
mail : admin@mail.com
password : admin

## Python shell 
	- To add user, apart from super user
	```
	from django.contrib.auth.models import User
	# Create a new user
	User.objects.create_user(username='testuser', password='testpass', email='testuser@example.com')	
	
	```

## Check users 	
```
	# Check if user with ID 2 exists
	user = User.objects.filter(id=2).first()
	print(user)  # This should print the user details or None if it doesn't exist
```

	
## Run server 
```
python manage.py runserver

```

## API Endpoints

    -Create a Task
        -Endpoint: /api/tasks/create/
        -Method: POST
        -Request Body:
		```
		{
			"name": "Task Name",
			"description": "Task Description",
			"task_type": "BUG",
			"assigned_user_ids": [1, 2]  // User IDs
		}
```
	-Assign a Task to Users
		-Endpoint: /api/tasks/<task_id>/assign/
		-Method: PUT
		-Request Body:
		```
		{
			"assigned_user_ids": [1, 2]
		}
		```
	-Get Tasks for a Specific User
		-Endpoint: /api/users/<user_id>/tasks/
		-Method: GET
		